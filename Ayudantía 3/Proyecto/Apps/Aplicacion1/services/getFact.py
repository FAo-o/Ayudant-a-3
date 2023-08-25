import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_fact(params={}):
    response = generate_request('https://catfact.ninja/fact', params)
    if response:
       fact_response = response.get('fact')
       length_response = response.get('length')
       return {'fact_text': fact_response, 'length': length_response}
    return False