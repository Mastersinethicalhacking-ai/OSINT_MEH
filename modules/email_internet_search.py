import requests
from bs4 import BeautifulSoup
import urllib.parse
import time

def search(email):
    try:
        query = f'"{email}"'
        url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('div', class_='g')

        print(f"\nSearch results for '{email}':\n")

        if results:
            for i, result in enumerate(results[:5], start=1):  # Limit to the first 5 results for simplicity
                title = result.find('h3')
                if title:
                    link = result.find('a')['href']
                    snippet = result.find('span', class_='st')
                    print(f"{i}. {title.text}\nLink: {link}\nSnippet: {snippet.text if snippet else 'No snippet available'}\n")
        else:
            print("No results found.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(2)  # Add a delay to avoid triggering Google’s rate limits


