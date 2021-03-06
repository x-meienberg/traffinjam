# main.py
# This is the main execution file for the aplaca algorithmic trading program

# Import all libraries
import access_alpaca
import read_stocks
import print_data

api2 = access_alpaca.api_2
api1 = access_alpaca.api_1

input_stocks = ['AAPL', 'GOOG', 'FB', 'TSLA', 'ABB', 'NVS', 'DOW']
intervals = 90  # Day intervals
ma_interval = 10  # Moving Average Intervals


# Check if stock market is open
# read_stocks.is_open(api2)

# Check the data for all input_stocks
for i in input_stocks:

    stock_prices = read_stocks.read_market_data(api1, i, intervals, ma_interval)
    print_data.show_time_plot(stock_prices, i, intervals, ma_interval)

    