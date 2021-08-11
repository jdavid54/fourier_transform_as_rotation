import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
e = np.e
sample_rate = 200

# rotation clockwise
exponent = -2*pi*1j


def rot(cycle):
    return e**(exponent*cycle)
# signal with n periods
n = 2
t = np.linspace(0,n,sample_rate)
one_round = np.linspace(0,1,sample_rate)

# compound signal
f1 = 2
f2 = 3
s1 = (np.cos(2*pi*f1*t)+1)/2
s2 = (np.cos(2*pi*f2*t)+1)/2
all_sig = (s1+s2)/2

# signal to study
one_period = ((np.cos(2*pi*f1*one_round)+1)/2 + (np.cos(2*pi*f2*one_round)+1)/2)/2

# spread one period of signal with as many rotations as cycles by period
cycle = 2  
cy = np.linspace(0,cycle,sample_rate)
rotation = rot(cy)
# do the rotation on one_period signal
y = one_period*rotation

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(10,5))
for k in range(1,n+1):
    ax1.plot((k/cycle,k/cycle),(0,1),'r-.')
#ax1.plot(t, s2)
ax1.plot(t, all_sig)
#ax2.plot(y.real[0], y.imag[0],'ro')
#ax2.plot(y.real[10], y.imag[10],'ro')
ax2.plot(y.real, y.imag)

s = sum(y)/sample_rate
print(s)
plt.plot(s.real, s.imag,'ko')
ax1.grid()
plt.tight_layout()
ax2.grid()
plt.show()

# cycling 0 to n
n = 5
fourier = []
samples = 100
cycles = np.arange(0, n+.1, n/samples)
for c in cycles:
    cy = np.linspace(0, c, sample_rate)
    rotation = rot(cy)
    y = one_period*rotation
    s = sum(y)/sample_rate
    fourier.append(s.real)
    print(c,s)
plt.plot(cycles,fourier)
plt.grid()
plt.show()
