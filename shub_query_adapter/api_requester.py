import requests

API_ENDPOINT = 'http://storage.scrapinghub.com'

def get_items_request(path_param, params, api_key):
    params['format'] = 'json'
    
    url = f"{API_ENDPOINT}/items/{path_param}"
    response = requests.get(url, params=params, auth=(api_key, ''))
    
    if response.status_code == 200:
        return response.json()
    else:
        return f'Error {response.status_code}: {response.text}'
    
def get_job_stats_request(path_param, api_key):
    url = f"{API_ENDPOINT}/jobs/{path_param}"
    response = requests.get(url, auth=(api_key, ''))
    
    if response.status_code == 200:
        return response.json()
    else:
        return f'Error {response.status_code}: {response.text}'
