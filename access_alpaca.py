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
api_2 = tradeapi.REST(CLIENT_ID, CLIENT_Secret, BASE_URL, api_version='v2')
api_1 = tradeapi.REST(CLIENT_ID, CLIENT_Secret, BASE_URL, api_version='v1')


def print_account():

	#Obtain account information
	account = api_2.get_account()
	print(account)


def status():

	#You can access status variables easily via the variable command
	status = api_2.get_account().status 
	print(status)


def open_positions():

	positions = api_2.list_positions()
	print('Open Positions:')
	print(positions)





