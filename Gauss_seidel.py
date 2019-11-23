import matplotlib.pyplot as plt
import numpy as np


# Gauss siedel method
x=2.41
y=3.0
h=0.1
nx=int(x/h)
ny=int(y/h)

Tg=np.zeros((ny,nx))
for i in range(ny):
	for j in range(nx):
		Tg[i][j]=500

for i in range(nx):
	Tg[0][i]=50
for i in range(nx):
	Tg[ny-1][i]=300
for i in range(ny):
	Tg[i][0]=75
for i in range(ny):
	Tg[i][nx-1]=100

steps=1000

for s in range(steps):
	for i in range(1,ny-1):
		for j in range(1,nx-1):
			Tg[i][j]=0.25*(Tg[i+1][j]+Tg[i][j+1]+Tg[i-1][j]+Tg[i][j-1])


from mpl_toolkits.mplot3d import Axes3D 
from matplotlib import cm 
from matplotlib.ticker import LinearLocator, FormatStrFormatter 
fig = plt.figure() 
ax = fig.gca(projection='3d')
X=np.arange(0,2.4,h)
Y=np.arange(0,3.0,h)
X,Y=np.meshgrid(X,Y)

surf = ax.plot_surface(X,Y,Tg, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_xlabel('x') 
ax.set_ylabel('y') 
ax.set_zlabel('T [$^o$C]')
plt.show()