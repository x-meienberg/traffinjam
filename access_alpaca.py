import json
import requests
import config
import alpaca_trade_api as tradeapi

CLIENT_ID = config.client_id
CLIENT_Secret = config.client_secret

#AUTH_URL = 'https://paper-api.alpaca.markets'
BASE_URL = 'https://paper-api.alpaca.markets'

#Instantiate REST API
api = tradeapi.REST(CLIENT_ID, CLIENT_Secret, BASE_URL, api_version='v2')

#Obtain account information
account = api.get_account()

print(account)