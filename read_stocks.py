# read_stocks.py
# Read the current data of the stock market and show them if need be

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import alpaca_trade_api as tradeapi 
import datetime


def is_open(api):
		
	#Check if market is closed
	clock = api.get_clock()
	print('The market is {}'.format('open.' if clock.is_open else 'closed.'))


### Please check again here 
def read_market_data(api,input_stocks,days):


		barset = api.get_barset(input_stocks,'day', limit = days)
		stock_bars = barset[input_stocks]

		week_open = stock_bars[0].o
		week_close = stock_bars[-1].c


		percent_change = (week_close-week_open)/week_open*100

		# Print if how stocks have evolved over last couple of days
		print(input_stocks,' moved {}% over the last 5 days'.format(percent_change))

		# convert time in datetime
	

		return stock_bars

