#x = (A*x + c) % M, base forumula for random numbers!!
import numpy as np 
N = 100 
A = 1664525 
c = 1013904223
M = 4294967296
x = 1 #seed, first number all random numbers come from

results = []

for i in range(N):
    x = (A*x + c) % M
    results.append(x)
print(results)

#integrating using the Monte Carlo Method
def f(x):
    return x**4 - 2*x + 1
#need to go from x = [1,2]
a = 1 
b = 2
Ndarts = 10000
#defining the function
x = np.linspace(a, b, 1000) 
y = f(x)
#setting up the box around the function
y_min_box = 0
y_max_box = np.max(y)
x_min_box = a
x_max_box = b
#let's start throwing darts
xrand = np.random.uniform(a, b, size = Ndarts)
yrand = np.random.uniform(y_min_box, y_max_box, size = Ndarts)
integral_counter = 0
#for i in range(Ndarts):
    #if f(i) < f(xrand[i]):
        #integral_counter += 1 
box_area = (b - a)*(y_max_box - y_min_box)
integral_counter = np.sum(yrand < f(yrand)) 
integral = (integral_counter / Ndarts) * box_area
print(integral)

#Changing the function drawn: 
import matplotlib.pyplot as plt 

N = 10000
#xrand = np.random.random(N)
y = -1*np.log(1 + xrand)
plt.hist(y, bins = 100)
plt.savefig('mc_ex_graphs.png')


