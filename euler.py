import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from math import exp 
x0=0
xf=5
y0=1

# This code calculate value according to euler method for all h at once and store all the values in different csv files

h_vals=[0.01,0.1,0.2,0.5]
for h in h_vals:		# loop for all values of h
	n=int((xf-x0)/	h)  # finding the number of steps
	x_val=[]			# creating list for values of x
	y_pred=[]			# creating list predictions 
	y_true=[]			# creating list true values
	err=[]				# creating list for relative error
	
	# Euler method
	x=x0
	y=y0
	for i in range(n):  # loop for all steps
		x=x+h       	# incrementing x
		y=y+h*(-30*y)   # incrementing y according to euler method
		x_val.append(x)	
		y_pred.append(y)
		y_true.append(exp(-30*x))     # calculating true value
		err.append(float(abs(y_true[-1]-y_pred[-1]))/abs(y_true[-1]))   # calculating relative error
	
	# Method ends here	


	# The following lines are to make a csv file for the results and save it and print the reults
	df=pd.DataFrame(np.array(x_val),columns=['x_val'])
	df['y_pred']=y_pred
	df['y_true']=y_true
	df['rel_error']=err
	df.to_csv("euler_"+str(h)+".csv",index=False)
	print("h = "+str(h))
	print(y_pred[-1])