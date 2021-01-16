
import matplotlib
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 


def show_time_plot(data):

	t = []
	y = []
	b = []
	mean_price = []
	sma = []
	t_momentum_up = []
	t_momentum_down = []
	y_momentum_up = []
	y_momentum_down = []

	horizon=len(data)

	for i in range(horizon):

		t.append(data[i].t)

	for i in range(horizon):

		y.append(data[i].h)
		b.append(data[i].l)
		mean_price.append((b[i]+y[i])/2)

	sma.append((y[0]+b[0])/2)	

	for j in range(1,horizon):

		sma.append(sma[j-1]+1/(j+1)*((y[j]+b[j])/2-sma[j-1]))

	for i in range(3, horizon):

		if (y[i]+b[i])/2> sma[i] and (y[i-3]+b[i-3])/2< sma[i]:

			t_momentum_up.append(t[i])
			y_momentum_up.append(sma[i]-3/100*sma[i])

		elif (y[i]+b[i])/2 < sma[i] and (y[i-3]+b[i-3])/2 > sma[i]:

			t_momentum_down.append(t[i])
			y_momentum_down.append(sma[i]+3/100*sma[i])	
			


	fig, ax = plt.subplots()

	ax.plot(t, mean_price)
	ax.plot(t,sma)
	ax.scatter(t_momentum_up,y_momentum_up, marker="^", color="green")
	ax.scatter(t_momentum_down,y_momentum_down, marker="v", color="red")
	


	labels = ["Mean Stock Price","SMA", "Momentum Up", "Momentum Down"]

	ax.set(xlabel= 'Date', ylabel = 'Price [USD]')
	ax.legend(labels)

	ax.grid()
	plt.show()	


