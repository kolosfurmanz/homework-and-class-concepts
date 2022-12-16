import numpy as np

#Question 1 
def f(x, t):
    return -0.001*(0 - 40) #plugging in given values into given DE 
a = 0 
b = 600
N = 600
h = (b - a) / N 
T_0 = 0
x = 0 #initial conditions
time = np.arange(a, b, h)
for t in time: #Euler's method, using previous results to create new ones in T_n = T_0
    T_n = T_0 + h*f(x, t)
    T_0 = T_n
    t += h
print("The temperature using time steps of 1 second and Euler's method is", T_n, "C")

T_0 = 0 #repeated so that it doesn't combine with the first initial temperature value 
for t in time: #2nd order RK method with k_1 and k_2 
    k_1 = h*f(x, t)
    k_2 = h*f(x + 0.5*k_1, t + 0.5*h)
    T_0 += h*f(x + 0.5*h, t + 0.5*h*f(x, t)) 
print("The temperature using time steps of 1 second and the 2nd order RK method is", T_0, "C")

#these two for loops are repeated for the remaining time steps, h, just with different N-values 
T_0 = 0
N = 1200
h = (b - a) / N
time = np.arange(a, b, h)
for t in time: 
    T_n = T_0 + h*f(x, t)
    T_0 = T_n
    t += h
print("The temperature using time steps of 0.5 seconds and Euler's method is", T_n, "C")
T_0 = 0 
for t in time: 
    k_1 = h*f(x, t)
    k_2 = h*f(x + 0.5*k_1, t + 0.5*h)
    T_0 += h*f(x + 0.5*h, t + 0.5*h*f(x, t)) 
print("The temperature using time steps of 0.5 seconds and the 2nd order RK method is", T_0, "C")

T_0 = 0
N = 2400
h = (b - a) / N
time = np.arange(a, b, h)
for t in time: 
    T_n = T_0 + h*f(x, t)
    T_0 = T_n
    t += h
print("The temperature using time steps of 0.25 seconds and Euler's method is", T_n, "C")
T_0 = 0 
for t in time: 
    k_1 = h*f(x, t)
    k_2 = h*f(x + 0.5*k_1, t + 0.5*h)
    T_0 += h*f(x + 0.5*h, t + 0.5*h*f(x, t)) 
print("The temperature using time steps of 0.25 seconds and the 2nd order RK method is", T_0, "C")

T_0 = 0
N = 4800
h = (b - a) / N
time = np.arange(a, b, h)
for t in time: 
    T_n = T_0 + h*f(x, t)
    T_0 = T_n
    t += h
print("The temperature using time steps of 0.125 seconds and Euler's method is", T_n, "C")
T_0 = 0 
for t in time: 
    k_1 = h*f(x, t)
    k_2 = h*f(x + 0.5*k_1, t + 0.5*h)
    T_0 += h*f(x + 0.5*h, t + 0.5*h*f(x, t)) 
print("The temperature using time steps of 0.125 seconds and the 2nd order RK method is", T_0, "C")
print("The actual value after solving the DE is 24 C.") 
print("From the results above, it appears that the most accurate results are those with time steps of 0.125 seconds as the values are just 4.9x10^-13 short of the actual value.") 
print("Surprisingly, the values become less and less accurate as the time step decreases until the value of the time step reaches 0.125 seconds.")

#Question 2  
import matplotlib.pyplot as plt
def f_x(x, y):
    return x - 0.5*x*y
def f_y(x, y):
    return 0.5*x*y - 2*y #defining given functions with given coefficients
x = 2 
y = 2
a = 0 
b = 30
N = 300
h = (b - a) / N #setting up increments of time, 0.1 was found to be appropriate 
time = np.arange(a, b, h)
xpops = []
ypops = []
for t in time: #big for loop going through the 4th order RK method
    k_1x = h*f_x(x, y)
    k_2x = h*f_x(x + 0.5*k_1x, y)
    k_3x = h*f_x(x + 0.5*k_2x, y)
    k_4x = h*f_x(x + k_3x, y)
    x += (k_1x + 2*k_2x + 2*k_3x + k_4x) / 6
    xpops.append(x)
    k_1y = h*f_y(x, y)
    k_2y = h*f_y(x, y + 0.5*h)
    k_3y = h*f_y(x, y + 0.5*h)
    k_4y = h*f_y(x, y + h)
    y += (k_1y + 2*k_2y + 2*k_3y + k_4y) / 6
    ypops.append(y)
#Special shout out to Derod for helping me effectively combine the two equations under one by modifying the RK equations in terms of x and y and puttind both in a single for loop 
plt.plot(time, xpops, color = 'blue')
plt.plot(time, ypops, color = 'red')
plt.title("Rabbit and Fox Populations Over Time")
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend(["Rabbit Population", "Fox Population"], loc = 'upper right')
plt.savefig('homework8_graph_kolos-furman_zachary.png')