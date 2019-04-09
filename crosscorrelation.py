import numpy as np
from matplotlib import pyplot as plt
a=int(input('enter the no.of elements'))
b=int(input('enter the no.of elements as '))
x=[]
for i in range(int(a)):	
	c=input('enter the elements')
	x.append(c)
print(x)
d=a+b-1
h=[]
r=[]
for k in range(int(b)):
	e=input('enter the elements')
	h.append(e)
for o in range(b):
	q=h[b-o-1]
	r.append(q)
for l in range(int(a-1)):
	f=0
	r.append(int(f))
print(r)
y=[]
s=0
for l in range(int(d)):
	for m in range(int(a)):
		s=s+int(x[m])*int(r[l-m])
	y.append(s)
	s=0
print(y)
l=np.arange(0,d,1)
plt.stem(l,y)
plt.show()

