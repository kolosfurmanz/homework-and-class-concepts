import numpy as np
def f(x): 
    return x**4 - 2*x + 1 

a = int(input("What is the lower bound? "))
b = int(input("What is the upper bound? "))
N = int(input("How many rectangles/trapezoids/parabolas or N value will be used in the approximation? "))
h = (b - a) / N
#for the rectangle rule:
s = 0
for m in range(1, (N+1)):
    s += f(a + m*h)  
r_integral = h*s
print("The value using the rectangle rule is", r_integral)

#for the trapezoid rule: 
s = 0 
for i in range(1, N):
    s += f(a + i*h)
t_integral = h * (0.5*(f(a) + f(b)) + s)
print("The value of using the trapezoid rule with", N, "trapezoids is", t_integral)

#for Simpson's rule: 
o = 0 
e = 0
for j in range(1, N, 2): 
    o += f(a + j*h) 

for k in range(2, N, 2): 
    e += f(a + k*h)
s_integral = h/3 * (f(a) + f(b) + 4*o + 2*e)
print("The value of using Simpson's rule with", N, "parabolas is", s_integral)

from gaussxw import gaussxw, gaussxwab 
x, w = gaussxw(N)
solution = 0 
for k in range(N): 
    xprime = 0.5*(b - a)*x + 0.5*(b + a)
    wprime = 0.5*(b - a)*w
    solution = solution + wprime[k]*f(xprime[k])
print("The value using Gaussian quadtrature with N value", N, "is", solution)

def integral(x):
    return x**5/5 - x**2 + x
x = b - a
print("The true value of the integral is", integral(x))