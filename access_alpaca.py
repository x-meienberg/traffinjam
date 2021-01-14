# This program controls the access to the alpaca paper trading API
# The rate limit on trading is set to 200 requests per minute per API key
#If HTTP status code 429, then rate limit is exceeded

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

positions = api.list_positions()
print('Open Positions:')
print(positions)

#You can access status variables easily via the variable command
status = account.status

print(status)

#This is a comment for testing
