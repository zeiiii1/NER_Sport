# scraping_articles.py

import requests
from bs4 import BeautifulSoup
import os
import time
from fake_useragent import UserAgent

BASE_URL = "https://www.lequipe.fr"
UA = UserAgent()

# Chemin vers TP2/data/raw_articles depuis ce script
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # = TP2/scripts/
TP2_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
DATA_DIR = os.path.join(TP2_DIR, "data", "raw_articles")

def get_article_links(page_url):
    headers = {'User-Agent': UA.random}
    resp = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(resp.content, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.startswith('/Football/') or href.startswith('/Tennis/'):
            full_url = BASE_URL + href
            links.append(full_url)
    return list(set(links))

def scrape_article(url):
    headers = {'User-Agent': UA.random}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.content, 'html.parser')
    paragraphs = soup.find_all('p')
    content = '\n'.join([p.get_text() for p in paragraphs if p.get_text()])
    return content.strip()

def save_article(content, filename):
    os.makedirs(DATA_DIR, exist_ok=True)
    file_path = os.path.join(DATA_DIR, f"{filename}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    links = get_article_links("https://www.lequipe.fr/")
    for i, link in enumerate(links[:10]):  # scrape les 10 premiers articles
        print(f"Scraping: {link}")
        try:
            content = scrape_article(link)
            if content:
                save_article(content, f"article_{i}")
            time.sleep(1)  # respect du site
        except Exception as e:
            print(f"Erreur avec {link} : {e}")

if __name__ == "__main__":
    main()
