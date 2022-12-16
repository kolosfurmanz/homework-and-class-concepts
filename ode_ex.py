import numpy as np 
from matplotlib import pylab as plt 

def f(x, t): 
    return -x**3 + np.sin(t)

a = 0 
b = 10 
N = 20
h = (b-a) / N 
x_t_solution = []
time = np.arange(a, b, h)

x = 0 #initial condition 

#2nd order RK example
#for t in time:
    #x_t_solution.append(x)
    #k1 = h*f(x, t)
    #k2 = h*f(x + 0.5*k1, t + 0.5*h)
    #x = x + k2
for t in time:
    x_t_solution.append(x)
    k1 = h*f(x, t)
    k2 = h*f(x + 0.5*k1, t + 0.5*h)
    k3 = h*f(x + 0.5*k2, t + 0.5*h)
    k4 = h*f(x + k3, t + h)
    x = x + (k1 + 2*k2 + 2*k3 + k4) / 6

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(time, x_t_solution)
ax.set_xlabel('time')
ax.set_ylabel('x(t)')
fig.savefig('ode_ex.png')