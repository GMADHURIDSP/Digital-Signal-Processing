import numpy as np
from matplotlib import pyplot as plot
t=np.arange(0,500,1)
f=5
fs=500
g=np.sin(2*np.pi*f*t/fs)
s=np.random.rand(g.shape[0])
a=g+s
p=input("enter the order")
l=[]
y=0
for i in range(0,500,1):
	for k in range(0,int(p)-1):
		y=y+a[i-k]
		print (y)
	x=float((y)/int(p))
	l.append(x)
	y=0
plot.subplot(413)
plot.plot(t,a,'r')
plot.subplot(412)
plot.plot(t,s,'g')
plot.subplot(411)
plot.plot(t,g,'k')
plot.subplot(414)
plot.plot(t,l,'g')
plot.show()
