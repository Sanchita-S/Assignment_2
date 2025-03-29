# %%
from transformers import pipeline  # Ensures pipeline is defined first
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime, timedelta

# %%
# Step 1: Scraping Medium articles using BeautifulSoup
articles = []
headers = {
    "User-Agent": "Mozilla/5.0"
}

date = datetime.today()
max_articles = 100

while len(articles) < max_articles:
    date_str = date.strftime('%Y/%m/%d')
    url = f"https://medium.com/tag/artificial-intelligence/archive/{date_str}"
    print(f"Scraping {url}...")

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        date -= timedelta(days=1)
        continue

    soup = BeautifulSoup(response.text, 'html.parser')
    posts = soup.find_all('div', class_='postArticle')

    for post in posts:
        title_tag = post.find('h3')
        link_tag = post.find('a', {'data-post-id': True})
        date_text = date.strftime('%Y-%m-%d')

        title = title_tag.get_text(strip=True) if title_tag else "N/A"
        link = link_tag['href'].split('?')[0] if link_tag else "N/A"

        if title != "N/A" and link.startswith("https"):
            articles.append({
                'title': title,
                'link': link,
                'date': date_text
            })

    date -= timedelta(days=1)
    time.sleep(1)

# %%
# Trim to 100
articles = articles[:100]
df = pd.DataFrame(articles)

# %%
# Step 2: Extract article content using BeautifulSoup
def extract_content(url):
    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code != 200:
            return ""
        soup = BeautifulSoup(res.text, 'html.parser')
        paragraphs = soup.find_all('p')
        return ' '.join([p.get_text(strip=True) for p in paragraphs])
    except:
        return ""

df['content'] = df['link'].apply(extract_content)
df = df[df['content'].str.strip() != ""]

# %%
# Step 3: Text Analysis using transformers
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_text(text):
    try:
        summary = summarizer(text[:1024])[0]['summary_text']
        sentiment = sentiment_analyzer(summary)[0]
        label = sentiment['label']
        score = sentiment['score'] if label == 'POSITIVE' else -sentiment['score']
        direction = 'Positive' if label == 'POSITIVE' else 'Negative'
        return pd.Series([summary, score, direction])
    except:
        return pd.Series(["", 0, "Neutral"])

df[['summary', 'importance_score', 'direction']] = df['content'].apply(analyze_text)

# %%
# Save to CSV
output_file = "ai_articles_medium_analyzed3.csv"
df.to_csv(output_file, index=False)
print(f"✅ Done! Results saved to {output_file}")
print(df[['title', 'summary', 'importance_score', 'direction']].head())

# %%
