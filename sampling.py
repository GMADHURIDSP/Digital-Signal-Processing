import matplotlib.pyplot as plt
import numpy as m
F=5
Fs=10
n=m.arange(0,10,0.5)
A=m.sin((2*m.pi*F*n)/Fs)
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.stem(n,A)
plt.show()
