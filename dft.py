import numpy as np
import matplotlib.pyplot as plot
import cmath as cm
j=cm.sqrt(-1)
x=[4,5,8,1,3,9,10,25,33,20,3]
u=input("enter the N to find N pt DFT:")
c=input("no of zeroes to be added:")
N=len(x)
q=N+c
w=np.arange(0,q)
v=np.arange(0,u)
X=[]
Y=[]
while (N<q):
	x.append(0)
	N+=1
for i in range(0,u):
       s=0
       for k in range(0,N):
            s+=(x[k]*np.exp(-k*2*np.pi*i/N*j))
       X.append(s)
for i in range(0,q):
       s=0
       for k in range(0,len(x)):
            s+=(x[k]*np.exp(-k*2*np.pi*i/N*j))
       Y.append(s)
print x
m=np.abs(X)
p=np.angle(X)
a=np.abs(Y)
b=np.angle(Y)
plot.subplot(231)
plot.stem(v,X,'r')
plot.subplot(232)
plot.stem(v,m,'b')
plot.subplot(233)
plot.stem(v,p,'g')
plot.subplot(234)
plot.stem(w,Y,'r')
plot.subplot(235)
plot.stem(w,a,'b')
plot.subplot(236)
plot.stem(w,b,'g')
plot.show()
