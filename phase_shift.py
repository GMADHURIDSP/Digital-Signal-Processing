import matplotlib.pyplot as plt
import numpy as np 
Fs =500
f=5
sample= 1000
x=np.arange(sample)
y= np.sin(2 * np.pi * f * x/ Fs)
plt.subplot(211)
plt.plot(x,y)

Fs1=400
f1=5
sample=1000
a=np.arange(sample)
b= np.sin(2 * np.pi * f * x/ Fs1+90)
plt.subplot(212)
plt.plot(a,b)

plt.xlabel('sample(n)')
plt.ylabel('voltage(v)')
plt.show()

