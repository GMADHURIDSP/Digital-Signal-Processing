import numpy as np
from matplotlib import pyplot as plt
import cmath as cm
p=float(input('enter the pass bandgain'))
s=float(input('enter the stopband gain'))
w=float(input('enter the passband freqoency'))
w2=float(input('enter the stop band frequency'))
wp=w
ws=w2
a=np.log10(((1/p**2)-1)/((1/s**2)-1))
b=np.log10(wp/ws)
p=0.5*(a/b)
print (p)
n=np.ceil(p)
c=((1/p**2)-1)**(1/2*n)
wc=wp/c
print(wc)
xmag=[]
k=np.arange(0,10000)
f=10000
for i in range(f):
	d=cm.sqrt(1+((i/wc)**(2*n)))
	e=(1/d)
	xmag.append(np.abs(e))
print (xmag)
plt.plot(k,xmag)
plt.show()
	


