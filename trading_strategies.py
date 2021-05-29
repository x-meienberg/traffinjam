# This is the part of the program where a trading strategy can be implemented

import matplotlib.pyplot as plt 
import numpy as np

#Relative return
def trading_strategy_1(data, name_of_stock, days, ma_interval):

	#initialise values
	t = []
	high = []
	low = []
	open_price = []
	closing_price = []
	mean_price = []
	volume = []
	r_relative = []
	r_log = []
	c_cum = []

	#define time horizon of time series
	horizon = len(data)

	for i in range(horizon):

		t.append(data[i].t)
		high.append(data[i].h) #Define highs
		low.append(data[i].l) #Define lows
		volume.append(data[i].v) #Define volume
		closing_price.append(data[i].c) #Closing price
		open_price.append(data[i].o) #Opening prices
		mean_price.append((low[i]+high[i])/2) #Calculate mean

		r_relative.append((mean_price[i]-mean_price[i-1]) / mean_price[i-1]) #calculate the relative returns
		r_log.append(np.log(mean_price[i-1]/mean_price[i])) #calculate the log-returns
	
	# !!!! Do not Forget to Add a Section here for the cumulative log-returns !!!! -> c_cum

	#create plots
	fig, ax = plt.subplots()

	#plot each relevant time series
	ax.plot(t[ma_interval:], r_relative[ma_interval:])
	ax.plot(t[ma_interval:], r_log[ma_interval:])

	labels = ["Relative Return", "Log-Returns"]
	ax.set(xlabel='Date', ylabel = 'Price [USD]')
	ax.legend(labels)

	#look and feel
	ax.grid()
	name_of_stock = str(name_of_stock)
	days = str(days)
	ax.set_title('Relative Returs of '+name_of_stock+ 'over last' + days + ' days')
	fig.autofmt_xdate()
	fig.savefig('results/' + name_of_stock + '_relativeReturn_stock.svg')

#Quantitattive momentum strategy
#def trading_strategy_2():


#Quantitive value strategy
#def trading_strategy_3():
