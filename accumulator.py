import numpy as np
from matplotlib import pyplot as plt
n=input("enter the no.of samples")
c=[]
d=[]
y=0
for i in  range(0,int(n)):
	x=input("enter the elements")
	c.append(x)
	y=y+int(x)
	d.append(y)
print (c)
print (d)
l=np.arange(0,int(n),1)
plt.stem(l,d)
plt.show()


