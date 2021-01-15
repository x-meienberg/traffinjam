# read_stocks.py
# Read the current data of the stock market and show them if need be

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import alpaca_trade_api as tradeapi 


def is_open(api):
		
	#Check if market is closed
	clock = api.get_clock()
	print('The market is {}'.format('open.' if clock.is_open else 'closed.'))


### Please check again here 
def read_market_data(api):

	barset = api.get_barset('AAPL','day', limit = 5)




