
import matplotlib
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 


def show_time_plot(data,name_of_stock, days):

	t = []
	high = []
	low = []
	open_price = []
	closing_price = []
	mean_price = []
	sma = []
	volume = []
	t_momentum_up = []
	t_momentum_down = []
	y_momentum_up = []
	y_momentum_down = []
	isMomentumUpDown = 0

	#Define time horizon index
	horizon=len(data)

	for i in range(horizon):

		t.append(data[i].t) #Define time
		high.append(data[i].h) #Define highs
		low.append(data[i].l) #Define lows
		volume.append(data[i].v) #Define volume
		closing_price.append(data[i].c) #Closing price
		open_price.append(data[i].o) #Opening prices
		mean_price.append((low[i]+high[i])/2) #Calculate mean

	#Calculate the first simple moving average
	sma.append(closing_price[0])	

	
	#Calculate the simple moving average
	for j in range(1,horizon):

		sma.append(sma[j-1]+1/(j+1)*(closing_price[j]-sma[j-1]))


	# Calculate exponential moving average
	
	alpha = 2/(horizon+1) #Define alpha value

	weightedCount = [0]
	weigthedSum = [0]
	EMA = [(high[0]+low[0])/2]

	for j in range(1,horizon):

		weightedCount.append((1-(1-alpha)**j)/(1-(1-alpha)))	
		weigthedSum.append(closing_price[j-1]+(1-alpha)*weigthedSum[j-1])
		EMA.append(weigthedSum[j]/weightedCount[j])	
			

	#Find momentum changes within data (historical data)
	for i in range(3, horizon):

		if isMomentumUpDown == -1 or isMomentumUpDown == 0: 

			if closing_price[i]> EMA[i] and closing_price[i] - closing_price[i-1] >= 0:

				t_momentum_up.append(t[i])
				y_momentum_up.append(EMA[i])
				isMomentumUpDown = 1

		elif isMomentumUpDown == 1 or isMomentumUpDown == 0:		

			if closing_price[i] < EMA[i] and closing_price[i] - closing_price[i-1] <= 0 :

				t_momentum_down.append(t[i])
				y_momentum_down.append(EMA[i])	
				isMomentumUpDown = -1

	
	#Define plots
	fig, ax = plt.subplots()

	ax.plot(t,closing_price)
	ax.plot(t,sma)
	ax.plot(t,EMA)
	ax.scatter(t_momentum_up,y_momentum_up, marker="^", color="green")
	ax.scatter(t_momentum_down,y_momentum_down, marker="v", color="red")
	


	labels = ["Closing Stock Price","SMA","EMA", "Momentum Up", "Momentum Down"]

	ax.set(xlabel= 'Date', ylabel = 'Price [USD]')
	ax.legend(labels)

	ax.grid()
	name_of_stock = str(name_of_stock)
	days = str(days)
	ax.set_title('Historical Data of '+name_of_stock+' over last '+days+' days')
	fig.autofmt_xdate()
	fig.savefig('results/'+name_of_stock+'_stock.svg')



