import numpy as np
import matplotlib.pyplot as plt
from numpy import arange, meshgrid, sqrt
delta = 0.025
x, y = meshgrid(
    arange(-10, 10, delta),
    arange(-10, 10, delta)
)

t=np.zeros((x.shape))

# code for surface plots

def f(x,y):
	z=complex(x,y)
	cn=z-1                  # calculation of complex number
	ccn=np.conj(z-1)	   # calculation of complex conjugate
	return cn*ccn-1
	
for i in range(x.shape[0]):
	for j in range(x.shape[1]):
		t[i][j]=f(x[i][j],y[i][j])

plt.contourf(x,y,t,0,cmap='gray')	
plt.gca().spines['left'].set_position('zero')
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['top'].set_color('none')
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.show()


# code for contour plots

def f(x,y):
	z=complex(x,y)
	# cn=np.square(np.square(z)/2 + z +1)
	# ccn=np.conj(np.square(np.square(z)/2 + z +1))
	return max(abs(z-1)-1,0)

for i in range(x.shape[0]):
	for j in range(x.shape[1]):
		t[i][j]=f(x[i][j],y[i][j])

plt.contour(x,y,t,0)
plt.contour(x,y,t,20)
plt.gca().spines['left'].set_position('zero')
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['top'].set_color('none')
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.show()