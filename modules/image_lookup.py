import requests

def lookup(image_path):
    url = "https://www.google.com/searchbyimage/upload"
    files = {'encoded_image': (image_path, open(image_path, 'rb')), 'image_content': ''}
    try:
        response = requests.post(url, files=files)
        if response.status_code == 200:
            print(f"Image search results: {response.url}")
        else:
            print("No results found for this image.")
    except Exception as e:
        print(f"Error: {e}")

