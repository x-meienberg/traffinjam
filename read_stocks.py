# read_stocks.py
# Read the current data of the stock market and show them if need be

def read_stocks(api):
	
	import matplotlib.pyplot as plt 
	import numpy as np 
	import pandas as pd 
	import alpaca_trade_api as tradeapi 


	clock = api.get_clock()
	
	print('The market is {}'.format('open.' if clock.is_open else 'closed.'))




