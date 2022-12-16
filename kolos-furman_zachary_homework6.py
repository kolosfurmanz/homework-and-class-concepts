import numpy as np 
N = 100000
R = 0.7
r = np.random.uniform(0, R)
l = 4e-3 
c = 299792458
theta1 = np.random.uniform(0, 2*np.pi)
theta2 = np.random.uniform(0, 2*np.pi) #randomizing each component of the distance equation

def x(theta1):
    return r*np.cos(theta1)

def y(theta1):
    return r*np.sin(theta1)

def distance(r, theta1, theta2):
    return np.sqrt(r**2 + R**2 - 2*r*R*np.cos(theta1 - theta2)) #this is the polar distance equation, found online

for i in range(N): 
    time = (distance(r, theta1, theta2))**2 / (l*c) #this is the equation for the time it takes the photons to travel through the sun, also found online
    time = time / (3600 * 24* 365)
print("The time it takes for photons to escape the sun with radius 0.7 m is", time, "years")

#the loop is repeated for each power of the solar radius, all the way through the actual value of 7e8 m
R = 7 
for i in range(N): 
    time = (distance(r, theta1, theta2))**2 / (l*c)
    time = time / (3600 * 24* 365)
print("The time it takes for photons to escape the sun with radius 7 m is", time, "years") 

R = 70
for i in range(N): 
    time = (distance(r, theta1, theta2))**2 / (l*c)
    time = time / (3600 * 24* 365)
print("The time it takes for photons to escape the sun with radius 70 m is", time, "years") 

R = 700
for i in range(N): 
    time = (distance(r, theta1, theta2))**2 / (l*c)
    time = time / (3600 * 24* 365)
print("The time it takes for photons to escape the sun with radius 700 m is", time, "years") 

R = 7000 
for i in range(N): 
    time = (distance(r, theta1, theta2))**2 / (l*c)
    time = time / (3600 * 24* 365)
print("The time it takes for photons to escape the sun with radius 7000 m is", time, "years") 

R = 70000
for i in range(N): 
    time = (distance(r, theta1, theta2))**2 / (l*c)
    time = time / (3600 * 24* 365)
print("The time it takes for photons to escape the sun with radius 7e4 m is", time, "years") 

R = 700000
for i in range(N): 
    time = (distance(r, theta1, theta2))**2 / (l*c)
    time = time / (3600 * 24* 365)
print("The time it takes for photons to escape the sun with radius 7e5 m is", time, "years") 

R = 7000000
for i in range(N): 
    time = (distance(r, theta1, theta2))**2 / (l*c)
    time = time / (3600 * 24* 365)
print("The time it takes for photons to escape the sun with radius 7e6 m is", time, "years") 

R = 70000000
for i in range(N): 
    time = (distance(r, theta1, theta2))**2 / (l*c)
    time = time / (3600 * 24* 365)
print("The time it takes for photons to escape the sun with radius 7e7 m is", time, "years") 

R = 700000000
for i in range(N): 
    time = (distance(r, theta1, theta2))**2 / (l*c)
    time = time / (3600 * 24* 365)
print("The time it takes for photons to escape the sun with radius 7e8 m is", time, "years") 
