import numpy as np 
import matplotlib.pyplot as plt 
#dx/dt = xy - x
#dy/dt = y - xy + sin^2(omega*t)

def f(r, t):
    x = r[0]
    y = r[1]
    fx = x*y - x
    fy = y - x*y + np.sin(t)**2
    fr = np.array([fx, fy], float)
    return fr 

a = 0 
b = 10 
N = 100
h = (b - a) / N 
time = np.arange(a, b, h)
x_solution = []
y_solution = []
x_0 = 1 
y_0 = 1
r = np.array([x_0, y_0], float)

for t in time: 
    x_solution.append(r[0])
    y_solution.append(r[1])
    k1 = h*f(r, t)
    k2 = h*f(r + 0.5*k1, t + 0.5*h)
    k3 = h*f(r + 0.5*k2, t + 0.5*h)
    k4 = h*f(r + k3, t + h)
    r = r + (k1 + 2*k2 + 2*k3 + k4) / 6
    x = r[0]
    y = r[1] #not necessary, reiterates point that r just holds both variables!! 
plt.plot(time, x_solution, color = 'blue', label = 'x(t)')
plt.plot(time, y_solution, color = 'red', label = 'y(t)')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.savefig('2var_ode_ex.png')
