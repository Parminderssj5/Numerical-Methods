from sklearn.datasets import make_spd_matrix
import numpy as np
from numpy.linalg import eig,norm
import pickle

# fxn to calculate value of given fxn at Q,b,x
def fx(Q,b,x):
	return 0.5*np.dot(np.dot(x.T,Q),x)-np.dot(b.T,x)

# fxn to calculate value of derivative of given fxn at Q,b,x
def d_fx(Q,b,x):
	return np.dot(Q,x)-b

# This fxn will return optimal x, value of fxn at optimal and number of steps taken for exact algorithm
def exact_sd(Q,b,x_old,eps):
	steps=0
	d=-1*d_fx(Q,b,x_old)
	alpha=np.dot(d.T,d)/np.dot(np.dot(d.T,Q),d)
	x_new=x_old+alpha*d
	steps+=1
	while((norm(fx(Q,b,x_old)-fx(Q,b,x_new))/norm(fx(Q,b,x_old)))>eps):
		x_old=x_new
		d=-1*d_fx(Q,b,x_old)
		alpha=np.dot(d.T,d)/np.dot(np.dot(d.T,Q),d)
		x_new=x_old+alpha*d
		steps+=1
	return x_new,fx(Q,b,x_new),steps

# This fxn will return optimal x, value of fxn at optimal and number of steps taken for inexact algorithm
def inexact_sd(Q,b,x_old,eps,gamma,beta):
	steps=0
	t=1
	d=-1*d_fx(Q,b,x_old)
	while(fx(Q,b,x_old+t*d)>fx(Q,b,x_old)+gamma*t*np.dot(d_fx(Q,b,x_old).T,d)):
		t=beta*t
	x_new=x_old+t*d
	steps+=1
	while((norm(fx(Q,b,x_old)-fx(Q,b,x_new))/norm(fx(Q,b,x_old)))>eps):
		x_old=x_new
		d=-1*d_fx(Q,b,x_old)
		while(fx(Q,b,x_old+t*d)>fx(Q,b,x_old)+gamma*t*np.dot(d_fx(Q,b,x_old).T,d)):
			t=beta*t
		x_new=x_old+t*d
		steps+=1
	return x_new,fx(Q,b,x_new),steps

n_values=[10,50,100,200,500]                
g_values=[0.1,0.2,0.4,0.6,0.8]
b_values=[0.2,0.3,0.5,0.7,0.9]
print("started")
for n in n_values:
	d1={}
	d2={}
	x_in=np.random.rand(n,1)
	eps=1e-4
	# gamma=1/5
	# beta=1/2
	for gamma in g_values:
		for beta in b_values:
			for i in range(10):
				Q=make_spd_matrix(n)
				b=np.random.rand(n,1)
				# scaling the matrices because random generator generates small values 
				Q=(i+1)*Q
				b=(i+1)*b

				f_in=fx(Q,b,x_in)
				eigs=eig(Q)
				lmda1,lmdan=min(eigs[0]),max(eigs[0])
				
				# exact line steepest descent
				opti_x,f_val,steps=exact_sd(Q,b,x_in,eps)
				d1[i]=(f_in,f_val,steps,lmda1,lmdan)

				# inexact line steepest descent
				opti_x,f_val,steps=inexact_sd(Q,b,x_in,eps,gamma,beta)
				d2[i]=(f_in,f_val,steps,lmda1,lmdan)

			print("computed for n = "+str(n)+"  gamma = "+str(gamma)+"  beta = "+str(beta))
			# storing data for all computations for exact as well as inexact algo applied for same Q,b,x_in
			with open('exact_info_'+str(n)+"_"+str(gamma)+"_"+str(beta)+'.pickle', 'wb') as handle:
				pickle.dump(d1, handle)
			with open('inexact_info_'+str(n)+"_"+str(gamma)+"_"+str(beta)+'.pickle', 'wb') as handle:
				pickle.dump(d2, handle)

print("done")