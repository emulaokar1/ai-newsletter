import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("NEWSAPI_KEY")

def fetch_ai_news():
    url = "https://eventregistry.org/api/v1/article/getArticles"

    payload = {
        "action": "getArticles",
        "keyword": ["AI", "GPU", "Machine Learning", " Artificial Intelligence", "Nvidia"],
        "keywordOper": "or",  
        "conceptUri": ["http://en.wikipedia.org/wiki/Nvidia"],
        "articlesPage": 1,
        "articlesCount": 100,
        "articlesSortBy": "date",
        "articlesSortByAsc": False,
        "dataType": ["news", "pr"],
        "forceMaxDataTimeWindow": 7,
        "resultType": "articles",
        "includeArticleBody": True,
        "includeArticleTitle": True,
        "includeSourceTitle": True,
        "includeArticleExtractedDates": True,
        "includeArticleSocialScore": True,
        "lang": ["eng"],
        "apiKey": API_KEY
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", {}).get("results", [])
        print(f"\n✅ Retrieved {len(articles)} articles:\n")

        target_indices = {1, 2, 3, 99, 100}
        """
        for i, article in enumerate(articles, 1):  
            if i in target_indices:
                print(f"Article {i}")
                print("Title:", article.get("title"))
                print("Date:", article.get("date"))
                print("Source:", article.get("source", {}).get("title"))
                print("URL:", article.get("url"))
                print()
        """    
    else:
        print(f"❌ Request failed with status {response.status_code}")
        print("Response:", response.text)

if __name__ == "__main__":
    fetch_ai_news()
