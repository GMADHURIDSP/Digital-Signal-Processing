import numpy as np
from matplotlib import pyplot as plt
import cmath as cm
p=float(input('enter the passband gain'))
s=float(input('enter the stopband gain'))
wp=float(input('enter the passband gain f'))
ws=float(input('enter the stopband gain f'))
l=(1/p**2)-1
m=(1/s**2)-1
e=cm.sqrt(l)
x=ws/wp
g=np.arccosh((m/l)**(0.5))/(np.arccosh(x))
z=np.arccosh((m)**0.5/e)/np.arccosh(x)
n=np.ceil(g)
print(n)
print(z)
f=10000
xmag=[]
for i in range(f):
	c=np.cos(n*(np.arccos(i/wp)))
	h=(1/(1+e**2*(c**2))**0.5)
	xmag.append(np.abs(h))
print(xmag)
w=np.arange(0,10000)
plt.plot(w,xmag)
plt.show()

