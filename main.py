#main.py
#This is the main execution file for the aplaca algorithmic trading program

import access_alpaca 
import read_stocks

api2 = access_alpaca.api_2
api1 = access_alpaca.api_1



read_stocks.is_open(api2)

read_stocks.read_market_data(api1)
