import requests

API_ENDPOINT = 'http://storage.scrapinghub.com/items/'

def send_request(path_param, params, api_key):
    headers = {
        'Authorization': f"Basic {api_key}"
    }
    
    params['format'] = 'json'
    
    url = f"{API_ENDPOINT}{path_param}"
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error {response.status_code}: {response.text}"
