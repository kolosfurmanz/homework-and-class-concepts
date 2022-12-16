import numpy as np 

def f(x): 
    return x**4 - 2*x + 1
a = 0 
b = np.arange(0, 11)
N = 1000
def h(b): 
    return (b - a) / N 

def rect_func(b):
    s = 0
    for m in range(1, (N+1)):
        s += f(a + m*h(b))    
    r_integral = h(b) * s 
    return r_integral
rect_list = []
for j in b: 
    rect_int = rect_func(j)
    rect_list.append(rect_int)
print(rect_list)
def trap_func(b): 
    s = 0 
    for i in range(1, N):
        s += f(a + i*h(b))
    t_integral = h(b) * (0.5*(f(a) + f(b)) + s)
    return t_integral
trap_list = []
for i in b: 
    trap_int = trap_func(i)
    trap_list.append(trap_int)

def simpson_func(b): 
    o = 0 
    e = 0
    for j in range(1, N, 2):
        o += f(a + j*h(b))
    for k in range(2, N, 2):
        e += f(a + k*h(b))
    simpson_integral = h(b)/3 * (f(a) + f(b) + 4*o + 2*e) 
    return simpson_integral
Da_simpson = []
for i in b: 
    simpson_int = simpson_func(i)
    Da_simpson.append(simpson_int)

def true(x): 
    return x**5 / 5 - x**2 + x
true_list = []
for i in b: 
    integral = true(i)
    true_list.append(integral)
print(true_list)
