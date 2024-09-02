import requests

def search(email):
    try:
        url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key=YOUR_API_KEY"
        response = requests.get(url)
        email_info = response.json()
        print(email_info)
    except Exception as e:
        print(f"Error: {e}")

