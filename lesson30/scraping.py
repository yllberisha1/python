import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

def get_page_content(url):
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        return r.content
    except Exception as e:
        print(f"Request failed for {url}: {e}")
        return None


def extract_article(content, base_url=""):
    soup = BeautifulSoup(content, "html.parser")
    articles = []

    for article in soup.find_all('div', class_='search-item'):
        title_div = article.find('div', class_='search-txt')

        title = "no title found"
        link = "no link found"
        date = "no date found"
        description = "no description found"

        if title_div:
            title_tag = title_div.find('a')
            if title_tag:
                title = title_tag.get_text(strip=True)

                href = title_tag.get("href", "").strip()
                link = urljoin(base_url, href)

        date_tag = article.find('div', class_='search-date')
        if date_tag:
            date = date_tag.get_text(strip=True)

        desc_tag = article.find('div', class_='search-desc')
        if desc_tag:
            description = desc_tag.get_text(strip=True)

        articles.append({
            "title": title,
            "link": link,
            "date": date,
            "description": description
        })

    return articles


def scrape_multiple_page(base_url, num_pages):
    all_articles = []
    for page in range(1, num_pages + 1):
        page_url = f"{base_url}?page={page}"
        print(f"Scraping page {page}: {page_url}")

        content = get_page_content(page_url)
        if not content:
            continue

        articles = extract_article(content, base_url)
        all_articles.extend(articles)

    return all_articles



base_url = 'https://www.technewsworld.com/'
num_pages = 5

all_articles = scrape_multiple_page(base_url, num_pages)


df = pd.DataFrame(all_articles)


df.to_csv('technewsworld_articles.csv', index=False)

print("Articles have been saved to technewsworld_articles.csv")


