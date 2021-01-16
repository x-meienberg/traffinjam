#main.py
#This is the main execution file for the aplaca algorithmic trading program

import access_alpaca 
import read_stocks
import print_data

api2 = access_alpaca.api_2
api1 = access_alpaca.api_1

input_stocks = ['AAPL','GOOG','FB']
days = 365


# read_stocks.is_open(api2)

for i in input_stocks:

	aapl_bars = read_stocks.read_market_data(api1, i, days)
	print_data.show_time_plot(aapl_bars)





