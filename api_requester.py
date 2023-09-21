import requests
import os

API_ENDPOINT = 'http://storage.scrapinghub.com/items/'
API_KEY = os.environ["API_KEY"]

def send_request(path_param, params):
    headers = {
        'Authorization': f"Basic {API_KEY}"
    }
    
    params['format'] = 'json'
    
    url = f"{API_ENDPOINT}{path_param}"
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error {response.status_code}: {response.text}"
