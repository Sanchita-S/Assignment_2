
# %%
import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime, timedelta

articles = []
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Start from a recent date and go backward
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

# Trim to 100
articles = articles[:100]

# Save to CSV
with open('ai_articles_medium.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'link', 'date'])
    writer.writeheader()
    writer.writerows(articles)

print(f"✅ Done! {len(articles)} AI articles saved to ai_articles_medium.csv")

# %%
