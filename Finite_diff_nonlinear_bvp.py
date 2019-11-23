import numpy as np 
from numpy.linalg import inv


h=0.25
alpha=1
beta=2
a=0
b=1
N=int((b-a)/h)
y=np.zeros((N+1,1))                   # intializing y vector to zeros

for i in range(N+1):
	y[i]=alpha+(beta-alpha)*i/N       # intializing y with straight line formula



def g(y,i):                           # this function calculates value of gi for a given y vector 
	if i==0:
		return y[0]-alpha
	elif i==N:
		return y[N]-beta
	return -(y[i+1]-2*y[i]+y[i-1])+(h**2)*(1-((y[i+1]-y[i-1])/2*h)**2)

def d(y,i):                              # calculates di for a given i and y
	return 2

def u(y,i):								 # calculates ui for a given i and y
	return -1-(y[i+1]-y[i-1])/2

def l(y,i):								 # calculates li for a given i and y
	return -1+(y[i+1]-y[i-1])/2

G=np.zeros((N+1,1))                      # intializing G(function values) vector with zeros
for i in range(N+1):					 # updating G with intial y vector 
	G[i]=g(y,i)

J=np.zeros((N+1,N+1))					 # intializng J (jacobian) with zeros  
J[0][0]=1								 # because g0=y0-alpha
J[N][N]=1								 # because gN=yN-beta
for i in range(1,N):                     # updating J with li,di and ui for given i and y
	J[i][i-1]=l(y,i)
	J[i][i]=d(y,i)
	J[i][i+1]=u(y,i)

n=100                                     # number of steps for newton ralphson 
for i in range(n):                      # iterative over n for newton ralphson
	v=-1*np.dot(inv(J),G)				# calculating v by finding inverse of J
	y=y+v 								# updating y vector by adding y 
	for j in range(1,N):				# calculating new value of J vector for updated y
		J[j][j-1]=l(y,j)
		J[j][j]=d(y,j)
		J[j][j+1]=u(y,j)
	for j in range(N+1):				# calculating new value of G vector for updated y 
		G[j]=g(y,j)

print(y)
print('done')
