import argparse
import requests
import csv
from bs4 import BeautifulSoup

def scr_quotesbytag(tag):
    url =  f"http://quotes.toscrape.com/tag/{tag}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Could not retrieve quotes")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    if not quotes:
        print(f"No quotes found for {tag}")
        return
    
    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        print(f"\"{text}\" - {author}")
        print()

def main():
    parser = argparse.ArgumentParser(description="Scrape quotes by tag.")
    parser.add_argument("--tag", required=True, help="the tag you want the quotes for(e.g., life, inspirational)")

    args = parser.parse_args()
    scr_quotesbytag(args.tag)

if __name__ == "__main__":
    main()


