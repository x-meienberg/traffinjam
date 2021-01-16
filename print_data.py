
import matplotlib
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 


def show_time_plot(data):

	t = []
	y = []
	b = []
	sma = []

	horizon=len(data)

	for i in range(horizon):

		t.append(data[i].t)

	for i in range(horizon):

		y.append(data[i].h)
		b.append(data[i].l)

	sma.append((y[0]+b[0])/2)	

	for j in range(1,horizon):

		sma.append(sma[j-1]+1/(j+1)*((y[j]+b[j])/2-sma[j-1]))




	fig, ax = plt.subplots()

	ax.plot(t,y)
	ax.plot(t,b)
	ax.plot(t,sma)

	ax.set(xlabel= 'Date', ylabel = 'Price [USD]')

	ax.grid()
	plt.show()	