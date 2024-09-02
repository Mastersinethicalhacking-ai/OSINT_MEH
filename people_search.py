import requests
from bs4 import BeautifulSoup
import re

def search(name, email=None):
    query = name
    if email:
        query += f" {email}"
    
    url = f"https://www.google.com/search?q={query}"
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all result links
        links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            # Filter out unnecessary links
            if 'url?q=' in href:
                clean_url = re.sub(r'^/url\?q=', '', href)
                clean_url = re.split('&', clean_url)[0]  # Remove tracking parameters
                if clean_url.startswith('http'):
                    links.add(clean_url)
        
        # Display formatted results
        if links:
            print(f"Search results for '{query}':\n")
            for link in links:
                print(link)
        else:
            print(f"No results found for '{query}'.")
    
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    search("John Doe", "john.doe@example.com")

