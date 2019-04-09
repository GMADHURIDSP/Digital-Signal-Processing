import numpy as np
from matplotlib import pyplot as plot
#def sine1(a,w,p):
	#s=np.cos(2)+p)
	#c=a*s
	#return c
t=np.arange(0,500,1)
f=5
fs=500
#l=sine1(4,150,0)
g=np.sin(2*np.pi*f*t/fs)
#plt.stem(t,g)
plot.subplot(411)
plot.plot(t,g,'k')
s=np.random.rand(g.shape[0])
plot.subplot(412)
plot.plot(t,s,'g')
a=g+s
plot.subplot(413)
plot.plot(t,a,'r')
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
plot.subplot(414)
plot.plot(t,l,'g')
plot.show()

