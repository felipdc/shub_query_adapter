import requests

API_ENDPOINT = 'http://storage.scrapinghub.com/items/'

def send_request(path_param, params, api_key):
    params['format'] = 'json'
    
    url = f"{API_ENDPOINT}{path_param}"
    response = requests.get(url, params=params, auth=(api_key, ''))

    if response.status_code == 200:
        return response.json()
    else:
        return f'Error {response.status_code}: {response.text}'
