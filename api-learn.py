from requests import Request, Session
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'slug':'bitcoin',
    'convert':'USD'
}

headers = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':'7e2409f0-13bf-43c3-ab6d-b3c689752de4'
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)

print(response.text)
