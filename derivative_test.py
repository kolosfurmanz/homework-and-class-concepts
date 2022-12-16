import numpy as np 

def f(x): 
    return np.sin(x) 

def deriv(x_0, h): 
    return (f(x_0 + h) - f(x_0 - h)) / (2*h) 

x_0 = 5 
h = 10 
answer = np.cos(x_0)

print("the derivative approximation with h = 10 is", deriv(x_0, h))
h = 1 
print("the derivative approximation with h = 1 is", deriv(x_0, h))
h = 0.1 
print("the derivative approximation with h = 0.1 is", deriv(x_0, h))
h = 0.01 
print("the derivative approximation with h = 0.01 is", deriv(x_0, h))
print("the actual value of the derivative is", answer)