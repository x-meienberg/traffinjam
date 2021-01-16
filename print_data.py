
import matplotlib
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 


def show_time_plot(data,name_of_stock, days):

	t = []
	high = []
	low = []
	mean_price = []
	sma = []
	t_momentum_up = []
	t_momentum_down = []
	y_momentum_up = []
	y_momentum_down = []

	#Define time horizon index
	horizon=len(data)

	for i in range(horizon):

		t.append(data[i].t) #Define time
		high.append(data[i].h) #Define highs
		low.append(data[i].l) #Define lows
		mean_price.append((low[i]+high[i])/2) #Calculate mean

	#Calculate the first simple moving average
	sma.append((high[0]+low[0])/2)	

	
	#Calculate the simple moving average
	for j in range(1,horizon):

		sma.append(sma[j-1]+1/(j+1)*((high[j]+low[j])/2-sma[j-1]))

	#Find momentum changes within data (historical data)
	for i in range(3, horizon):

		if (high[i]+low[i])/2> sma[i] and (high[i-3]+low[i-3])/2< sma[i]:

			t_momentum_up.append(t[i])
			y_momentum_up.append(sma[i]-3/100*sma[i])

		elif (high[i]+low[i])/2 < sma[i] and (high[i-3]+low[i-3])/2 > sma[i]:

			t_momentum_down.append(t[i])
			y_momentum_down.append(sma[i]+3/100*sma[i])	
			


	#Define plots
	fig, ax = plt.subplots()

	ax.plot(t, mean_price)
	ax.plot(t,sma)
	ax.scatter(t_momentum_up,y_momentum_up, marker="^", color="green")
	ax.scatter(t_momentum_down,y_momentum_down, marker="v", color="red")
	


	labels = ["Mean Stock Price","SMA", "Momentum Up", "Momentum Down"]

	ax.set(xlabel= 'Date', ylabel = 'Price [USD]')
	ax.legend(labels)

	ax.grid()
	name_of_stock = str(name_of_stock)
	days = str(days)
	ax.set_title('Historical Data of '+name_of_stock+' over last '+days+' days')
	fig.autofmt_xdate()
	fig.savefig('results/'+name_of_stock+'_stock.svg')


