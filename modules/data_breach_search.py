import requests
from bs4 import BeautifulSoup

def search(email):
    url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            print(soup.prettify())
        else:
            print("No breaches found.")
    except Exception as e:
        print(f"Error: {e}")

