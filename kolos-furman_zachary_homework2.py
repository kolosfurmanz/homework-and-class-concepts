import numpy as np
#part b 
#the altitude is h in m

G = 6.67e-11 #in m^3kg^-1s^-2
M = 5.97e24 #in kg 
R = 6371000 #in m, multiplied the number given in the book by 1000
T = int(input("What is the orbital period T in seconds? ")) #I used the orbital period of the moon, about 2360621 seconds to test this part of the code. It gave me an answer of about 377 million m, which is very comparable to the answer I found online 
h = ((G * M * T**2) / (4 * (np.pi)**2))**(1 / 3) - R 
print("the height the satellite orbits above Earth is", h, "m") 

#part c 

T = 86400 #this is the period in seconds, 24 hours multiplied by 60 minutes times 60 seconds
h = ((G * M * T**2) / (4 * (np.pi)**2))**(1 / 3) - R 
print("the height a geosynchronous satellite orbits above Earth is", h, "m")

T = 5400 #this is the period in seconds, 90 minutes multiplied by 60 seconds 
h = ((G * M * T**2) / (4 * (np.pi)**2))**(1 / 3) - R
print("the height of a satellite orbiting every 90 minutes is", h, "m")

T = 2700 #this is the period in seconds, 45 minutes multiplied by 60 seconds 
h = ((G * M * T**2) / (4 * (np.pi)**2))**(1 / 3) - R
print("the height of a satellite orbiting every 45 minutes is", h, "m")
print("I conclude from the last of these calculations that an orbital period of 45 minutes is impossible since the height at which the satellite would orbit would be negative")
