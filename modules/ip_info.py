import requests
from requests.exceptions import ConnectionError, Timeout, RequestException

def lookup(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=5)
        ip_info = response.json()

        if ip_info['status'] == 'fail':
            print(f"Error: {ip_info['message']}")
            return

        print("\nIP Information Lookup Result:")
        print(f"IP Address: {ip_info.get('query', 'N/A')}")
        print(f"Country: {ip_info.get('country', 'N/A')} ({ip_info.get('countryCode', 'N/A')})")
        print(f"Region: {ip_info.get('regionName', 'N/A')} ({ip_info.get('region', 'N/A')})")
        print(f"City: {ip_info.get('city', 'N/A')}")
        print(f"ZIP Code: {ip_info.get('zip', 'N/A')}")
        print(f"Latitude: {ip_info.get('lat', 'N/A')}")
        print(f"Longitude: {ip_info.get('lon', 'N/A')}")
        print(f"ISP: {ip_info.get('isp', 'N/A')}")
        print(f"Organization: {ip_info.get('org', 'N/A')}")
        print(f"AS: {ip_info.get('as', 'N/A')}")
        
    except ConnectionError:
        print("Error: Failed to establish a connection. Please check your internet connection and try again.")
    except Timeout:
        print("Error: The request timed out. The server might be busy. Please try again later.")
    except RequestException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

