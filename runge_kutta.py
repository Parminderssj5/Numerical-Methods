import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from math import exp 
x0=0
xf=5
y0=1

h_vals=[0.01,0.1,0.2,0.5]

# function to calculate dy/dx
def fx(x,y):
	return -30*y


for h in h_vals:		# loop for all values of h
	n=int((xf-x0)/	h)  # finding the number of steps
	x_val=[]			# creating list for values of x
	y_pred=[]			# creating list predictions 
	y_true=[]			# creating list true values
	err=[]				# creating list for relative error


	# Runge kutta method
	x=x0
	y=y0
	for i in range(n):  # loop for all steps
		# calculating values of k's for 4th order RK method
		k1=h*fx(x,y)
		k2=h*fx(x+0.5*h,y+0.5*k1)
		k3=h*fx(x+0.5*h,y+0.5*k2)
		k4=h*fx(x+h,y+k3)
		y=y+(1.0/6.0)*(k1+2*k2+2*k3+k4)
		x_val.append(x+h)
		y_pred.append(y)
		y_true.append(exp(-30*(x+h)))     # calculating true value
		err.append(float(abs(y_true[-1]-y_pred[-1]))/abs(y_true[-1]))   # calculating relative error
		x=x+h
	# method ends here


	# The following lines are to make a csv file for the results and save it and print the reults
	df=pd.DataFrame(np.array(x_val),columns=['x_val'])
	df['y_pred']=y_pred
	df['y_true']=y_true
	df['rel_error']=err
	df.to_csv("runge_kutta_"+str(h)+".csv",index=False)
	print("h = "+str(h))
	print(y_pred[-1])