import requests
import os
import urllib.parse

API_ENDPOINT = 'http://storage.scrapinghub.com/items/'
API_KEY = os.environ["API_KEY"]

def send_request(path_param, params):
    headers = {
        'Authorization': f"Basic {API_KEY}"
    }
    # Add format=json to params
    params['format'] = 'json'
    # Use path_param in the URL
    url = f"{API_ENDPOINT}{path_param}"
    response = requests.get(url, params=params, headers=headers)
    
    print(response.url)
    print(urllib.parse.unquote_plus(response.url))
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error {response.status_code}: {response.text}"
