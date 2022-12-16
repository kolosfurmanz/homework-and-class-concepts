import numpy as np 
import matplotlib.pyplot as plt 

def f(x): 
    return np.sin(x)

def approx(x, h): 
    return (f(x + h) - f(x - h)) / (2*h)

def deriv(x): 
    return np.cos(x)

x = np.arange(0, 2*np.pi, np.pi/32)
y = f(x)
z = deriv(x) + 0.1
h = 1
a = approx(x, h)
h = 0.1
b = approx(x, h)
h = 0.01 
c = approx(x, h)

fig, ax = plt.subplots(1)
ax.set_xticks(np.arange(0, 2*np.pi+1, np.pi/4))
labels = [r'$0$', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$', r'$5\pi/4$', r'$3\pi/2$', r'$7\pi/4$', r'$2\pi$', r'$2\pi$']
ax.set_xticklabels(labels)
plt.xlabel("x values")
plt.ylabel("y values") 
plt.plot(x, y, color = 'blue')
plt.plot(x, z, color = 'red') 
plt.plot(x, a, color = 'orange')
plt.plot(x, b, color = 'green')
plt.plot(x, c, color = 'black')
plt.savefig('derivative-function-graphs.png')