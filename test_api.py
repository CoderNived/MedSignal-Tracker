import requests

base_url = "https://clinicaltrials.gov/api/v2"

params= {
    'query.term': 'paracetamol',
    'pageSize': 25,
    'sort': 'ResultsFirstPostDate'
}

response = requests.get(base_url + '/studies', params=params)
studies = response.json()['studies']
print(studies)