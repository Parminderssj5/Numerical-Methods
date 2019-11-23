from math import sin,log
import matplotlib.pyplot as plt

# Taking p,q,r in the general equation as follows
# These fxns are continous in given range and hence bounded
# The q fxn is positive so solution is unique

def p(x):
	return -2/x

def q(x):
	return 2/(x*x)

def r(x):
	return sin(log(x))/(x*x)

# setting intial and final values 
a=1					# intial value of x
b=2					# final value of x
s1=1				# intial value of y 
s2=2				# final value of y
n=100				# No. of steps for RK-4

h=(b-a)/n 			# Value of step size
u1=s1
u2=0
v1=0
v2=1

# creating  u and v matries of zeros for storing values of y and y' at every step
u=[[0 for i in range(n+1)] for j in range(2)]
v=[[0 for i in range(n+1)] for j in range(2)]


# implementing RK-4 method for system of equations
for i in range(1,n+1):
	x=a+(i-1)*h
	t=x+0.5*h
	k11=h*u2
	k12=h*(p(x)*u2+q(x)*u1+r(x))
	k21=h*(u2+0.5*k12)
	k22=h*(p(t)*(u2+0.5*k12)+q(t)*(u1+0.5*k11)+r(t))
	k31=h*(u2+0.5*k22)
	k32=h*(p(t)*(u2+0.5*k22)+q(t)*(u1+0.5*k21)+r(t))
	t=x+h
	k41=h*(u2+k32)
	k42=h*(p(t)*(u2+k32)+q(t)*(u1+k31)+r(t))
	u1=u1+(k11+2*(k21+k31)+k41)/6
	u2=u2+(k12+2*(k22+k32)+k42)/6
	k11=h*v2
	k12=h*(p(x)*v2+q(x)*v1)
	t=x+0.5*h
	k21=h*(v2+0.5*k12)
	k22=h*(p(t)*(v2+0.5*k12)+q(t)*(v1+0.5*k11))
	k31=h*(v2+0.5*k22)
	k32=h*(p(t)*(v2+0.5*k22)+q(t)*(v1+0.5*k21))
	t=x+h
	k41=h*(v2+k32)
	k42=h*(p(t)*(v2+k32)+q(t)*(v1+k31))
	v1=v1+(k11+2*(k21+k31)+k41)/6
	v2=v2+(k12+2*(k22+k32)+k42)/6
	u[0][i]=u1
	u[1][i]=u2
	v[0][i]=v1
	v[1][i]=v2


w1=s1
# calculating value of constant such that y(x)=u(x)+c*v(x)
z=(s2-u[0][n])/v[0][n]
x=a

# creating lists for storing values of x and y at each step
x_val=[]
y_val=[]

# calculating values at each step
print("x = "+str(1)+"  value of y = "+str(1))
for i in range(1,n+1):
	x=a+i*h
	y=u[0][i]+z*v[0][i]
	x_val.append(x)
	y_val.append(y)
	print("x = "+str(x)+"  value of y = "+str(y))

# plotting values of x and y
plt.plot(y_val,label='Value of y')
plt.xlabel('No. of Steps')
plt.ylabel("y")
plt.title("Shooting Method")
plt.legend()
plt.show()

