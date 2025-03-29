# 📚 CSIS 4260 – Assignment 2  
## Web Scraping & Text Analysis: Medium Articles on Artificial Intelligence

**Student:** Sanchita  
**Date:** 28 March, 2025  

---

## 🧩 Assignment Overview

This project is divided into two parts:

### 🔹 Part 1: Web Scraping
- Researched and compared popular web scraping libraries.
- Chose **BeautifulSoup** with `requests` for its simplicity, ease of use, and flexibility.
- Scraped 100 recent articles from Medium tagged with **Artificial Intelligence**.
- Output is saved to `ai_articles_medium.csv`.

### 🔹 Part 2: Text Analysis
- Used Hugging Face's `transformers` pipelines for **summarization** and **sentiment analysis**.
- Models used:
  - `facebook/bart-large-cnn` for summarization.
  - `distilbert-base-uncased-finetuned-sst-2-english` for sentiment analysis.
- Each article was summarized and assigned an **importance score** (positive or negative sentiment).

---

## 🛠️ Setup & Dependencies

Install the required Python packages:

```bash
pip install requests beautifulsoup4 pandas transformers
 pandas transformers


🚀 How to Run the Code
1️⃣ assign2.py – Web Scraping

python assign2.py
Scrapes 100 recent Medium articles on AI.

Saves data to ai_articles_medium.csv.

2️⃣ assign22a.py – Text Analysis

python assign22a.py
Extracts full article content from scraped URLs.

Applies summarization and sentiment analysis.

Saves results to ai_articles_medium_analyzed3.csv.

📌 File List
assign2.py – Web scraping logic using BeautifulSoup.

assign22a.py – Text extraction, summarization & sentiment analysis.

ai_articles_medium.csv – Raw scraped article metadata.

ai_articles_medium_analyzed3.csv – Final output with summaries and sentiment scores.

README.md – Instructions and analysis.


📊 What the Analysis Revealed
After processing 100 AI-related articles from Medium, I extracted summaries and analyzed their overall sentiment to better understand how artificial intelligence is being discussed online.

🔹 Sentiment Breakdown
🟢 Positive Tone: 61 articles

🔴 Negative Tone: 39 articles

This suggests that most content leaned in a positive direction—highlighting growth, creativity, and innovation in AI tools and platforms. However, a good portion still expressed concern, especially around the ethical and societal impacts of these technologies.

🧭 What Topics Came Up the Most?
Tone	Common Themes
Positive	ChatGPT, GPT-4, OpenAI, AI for productivity, programming tools, learning platforms
Negative	Job loss, misinformation, ethical concerns, AI misuse, deepfakes
The more optimistic posts focused on what AI can do—its usefulness in coding, writing, design, and general problem-solving. The more critical ones warned about issues like automation replacing human jobs or the risks of unchecked AI tools.

🔍 Interesting Examples
Top Positive Example:
ChatGPT Just Works – This article was one of the most highly rated for positive sentiment, with a score of 0.9994. It emphasized how intuitive and reliable the tool is in daily use.

Top Negative Example:
Naive Bayes – Scored -0.9994, pointing to some frustrations or limitations with outdated machine learning techniques or misunderstandings around AI models.

Balanced Perspective:
Mental Health and AI – With a positive score of 0.7904, this article acknowledged the helpful side of AI in supporting mental health, but didn’t ignore the need for careful implementation.

📌 Final Thoughts
Overall, this snapshot of recent AI content reflects both excitement and caution. Many writers are inspired by the pace of innovation, but they’re also raising valid concerns about how these tools are used and what it means for the future of work and society.

This type of analysis could be expanded in the future to compare different time periods or platforms, helping track how public perception of AI shifts over time
