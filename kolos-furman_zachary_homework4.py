import numpy as np 

#defining functions in terms of z, as they are in the homework document
def H(z): 
    return (0.3*(1 + z)**3 + 0.7)**0.5 #the 1+z^2 term was omitted since omega_r was equal to zero 

def r(z): 
    return 3000 / H(z)

z_2 = np.linspace(0, 10, 11) #making the z_2 values an array with 11 components, as that is the number of np.trapz that will be calculated
z_1 = 0 
N = 7
def h(z_2): 
    return (z_2 - z_1) / N #h is no longer constant since it depends on a varaible b, that's why it's a function here
#I define the integrals as functions since they are already for loops so that the loops can be done in the range of z_2's length
s = 0 
def linear_func(z_2): #linear integral
    s = 0
    for m in range(N + 1):
        s += r(z_1 + m*h(z_2))    
    r_integral = h(z_2) * s 
    return r_integral
Da_linear = []
for j in z_2: 
    linear_int = linear_func(j) / (j + 1)
    Da_linear.append(linear_int)

def trap_func(z_2): #trapezoid integral
    s = 0 
    for i in range(1, N):
        s += r(z_1 + i*h(z_2))
    trap_integral = h(z_2) * (0.5*(r(z_1) + r(z_2)) + s)
    return trap_integral
Da_trap = []
for i in z_2:
    trap_int = trap_func(i) / (i + 1)
    Da_trap.append(trap_int)

def simpson_func(z_2): #Simpson integral
    o = 0 
    e = 0
    for j in range(1, N, 2):
        o += r(z_1 + j*h(z_2))
    for k in range(2, N, 2):
        e += r(z_1 + k*h(z_2))
    simpson_integral = h(z_2)/3 * (r(z_1) + r(z_2) + 4*o + 2*e) 
    return simpson_integral
Da_simpson = []
for i in z_2: 
    simpson_int = simpson_func(i) / (i + 1)
    Da_simpson.append(simpson_int)

from gaussxw import gaussxw, gaussxwab 
Da_gauss = []
def gauss_int_func(z_2): #Gaussian quadrature, using the gaussxw.py file above 
    s = 0
    x, w = gaussxw(N)
    for i in range(N):
        xprime = 0.5*(z_2 - z_1)*x + 0.5*(z_2 + z_1)
        wprime = 0.5*(z_2 - z_1)*w 
        s = s + wprime[i]*r(xprime[i])
    return s 
for j in z_2: 
    gauss_int = gauss_int_func(j) / (j + 1)
    Da_gauss.append(gauss_int)

#I'd like to give a massive shout out to Derod for helping me with this section, as this process took me a long time to grasp and it actually inspired me to rewrite the other integrals as they became much more accurate doing them in a separate loop 
#np.trapz would not work in a loop whatsoever due to issues with dimensions and/or the values not being integers. Derod's explanation of the np.trapz function also greatly helped me realize this fact. I apologize in advance for the redudancy below.
Da_nptrapz = [] 

z0 = np.linspace(0, 0, 25)
z1 = np.linspace(0, 1, 25)
z2 = np.linspace(0, 2, 25)
z3 = np.linspace(0, 3, 25)
z4 = np.linspace(0, 4, 25)
z5 = np.linspace(0, 5, 25)
z6 = np.linspace(0, 6, 25)
z7 = np.linspace(0, 7, 25)
z8 = np.linspace(0, 8, 25)
z9 = np.linspace(0, 9, 25)
z10 = np.linspace(0, 10, 25)

Z0 = np.trapz(r(z0), z0) #These 11 lines define each np.trapz value that is appended to the empty list in line 69
Z1 = np.trapz(r(z1), z1) / 2
Z2 = np.trapz(r(z2), z2) / 3
Z3 = np.trapz(r(z3), z3) / 4
Z4 = np.trapz(r(z4), z4) / 5
Z5 = np.trapz(r(z5), z5) / 6
Z6 = np.trapz(r(z6), z6) / 7
Z7 = np.trapz(r(z7), z7) / 8 
Z8 = np.trapz(r(z8), z8) / 9
Z9 = np.trapz(r(z9), z9) / 10
Z10 = np.trapz(r(z10), z10) / 11

Da_nptrapz.append(Z0)
Da_nptrapz.append(Z1)
Da_nptrapz.append(Z2)
Da_nptrapz.append(Z3)
Da_nptrapz.append(Z4)
Da_nptrapz.append(Z5)
Da_nptrapz.append(Z6)
Da_nptrapz.append(Z7)
Da_nptrapz.append(Z8)
Da_nptrapz.append(Z9)
Da_nptrapz.append(Z10)

#Finally, this section is the section for the graphs themselves in order of the integrations methods used to the labels, to the title, to the legend, and finally saving the figure as a .png file 
import matplotlib.pyplot as plt 
plt.scatter(z_2, Da_linear, color = 'blue', label = 'linear')
plt.scatter(z_2, Da_trap, color = 'red', label = 'my trap')
plt.scatter(z_2, Da_simpson, color = 'orange', label = 'Simpson')
plt.scatter(z_2, Da_gauss, color = 'green', label = 'Gaussian quad') 
plt.plot(z_2, Da_nptrapz, color = 'black', label = 'np.trapz') 
plt.xlabel('z') 
plt.ylabel('$D_{a}$')
plt.title("Angular Diameter Distance ($D_{a}$) vs redshift (z) using an N value of 7")
leg = plt.legend(loc='upper right')
plt.savefig('homework_4_graphs.png')