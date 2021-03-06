# read_stocks.py
# Read the current data of the stock market and show them if need be
 
def is_open(api):
		
	#Check if market is closed
	clock = api.get_clock()
	print('The market is {}'.format('open.' if clock.is_open else 'closed.'))


### Please check again here 
def read_market_data(api,input_stocks,intervals,ma_interval):


		barset = api.get_barset(input_stocks,'day', limit = intervals+ma_interval) #acquire additional data for moving average (add extra ma_interval)
		stock_bars = barset[input_stocks]

		week_open = stock_bars[intervals+ma_interval-5].o
		week_close = stock_bars[-1].c


		percent_change = (week_close-week_open)/week_open*100

		# Print if how stocks have evolved over last couple of days
		print(input_stocks,' moved {}% over the last 5 days'.format(percent_change))

		# convert time in datetime
	

		return stock_bars

