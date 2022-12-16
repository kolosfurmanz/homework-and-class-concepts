#linear equations
#copied from gausselim.py, zero replaces the first two:

from numpy import array,empty
import numpy as np 


A = array([[ 0, 1,  4,  1 ],
           [ 3,  4, -1, -1 ],
           [ 1, -4,  1, 5 ],
           [ 2, -2,  1,  3 ]],float)
v = array([ -4, 3, 9, 7 ],float)
N = len(v)

# Gaussian elimination
for m in range(N): 
    # Divide by the diagonal element
    for n in range(N):
        div = A[m,n] #making the second element a unique value so it can be switched to avoid dividing by zero
        A[m, n], A[n, m] = A[n, m], A[m, n] #this officially switches the values around so that there is no division by zero, no matter where the zeros are. This was tested using the other given array and still ran
    A[m, :] = A[m, :] / div
    v[m] /= div

    # Now subtract from the lower rows
    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

# Backsubstitution
x = empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]
print("The solution for the linear system of equations is", x)

#root finding 
import random
def B_v(T): 
    return (2*np.pi*h*c**2 / lam**5)*np.exp(-h*c / (lam*k*T)) #I ended up using this form of Planck's equation from modern physics because it is the approximation for short wavelengths, making it still valid, and the derivatives for this equation ended up not being zero, making Newton's method viable
h = 6.62607004e-27
lam = 870e-4
c = 29979245800
k = 1.3806542e-16 
#this bisection code was found online from Berkeley as an excerpt from "Python Programming and Numerical Methods" by Kong, Siauw, and Bayen
def bisection(B_v, a, b, tol):
    if np.sign(B_v(a)) == np.sign(B_v(b)):
        a = random.randint(1, 100) #since a root is found where the values change sign, this condition redraws temperature values if it doesn't change sign
        b = random.randint(1, 100)
    m = (a + b)/2 #gets the midpoint if the value changes sign 
    if np.abs(B_v(m)) < tol: #this means that the value at the midpoint of the equation is less than the tolerance, making it as close to zero as possible. In this specific case, the best that the code could approximate to was 1 
        return m
    elif np.sign(B_v(a)) == np.sign(B_v(b)):
        return bisection(B_v, m, b, tol)
    elif np.sign(B_v(b)) == np.sign(B_v(m)):
        return bisection(B_v, a, m, tol)
T = 10*bisection(B_v, random.randint(1, 100), random.randint(1, 100), 1)
print("the temperature found using bisection is", int(T), "K")

def deriv_B(T, n): #in-class equation for derivatives, now just using "n" instead of "h" for step size 
    return (B_v(T + n) - B_v(T - n)) / (2*n)
n = 0.01 
T = random.randint(1, 100)

def newton(a, T): 
    return a - (B_v(a)) / deriv_B(T, n) #newton's method where "a" is the new value and "T" is the old value   
a = random.randint(1, 100)
tol = 0.01
while newton(a, T) < 0: #avoids negative temperatures
    T = random.randint(1, 100)
    a = random.randint(1, 100)
else: 
    while B_v(a) < tol: #tolerance condition to make the value of the intensity as close to zero as possible, definition of a root
        T = random.randint(1, 100)
        a = random.randint(1, 100)
    else:
        print("The temperature found using Newton's method is", a, "K")