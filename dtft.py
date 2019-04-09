import numpy as np
from matplotlib import pyplot as plt

n=int(input('enter the lenth of sequence'))
x=[]
for i in range(n):
	b=int(input('enter the samples'))
	x.append(b)
print(x)
plt.subplot(311)
plt.stem(x)

j=np.complex(0,1)
a=1000
s=0
w=np.linspace(-np.pi,np.pi,a)
print(w)
mag=[]
phase=[]
for i in range(a):
	for k in range(n):
		s=s+(x[k]*np.exp(-j*w[i]*k))
	mag.append(np.abs(s))
	phase.append(np.angle(s))
	
	print(s)
	s=0
plt.subplot(312)
plt.plot(w,mag)
plt.subplot(313)
plt.plot(w,phase)
plt.show()
	
		
	


