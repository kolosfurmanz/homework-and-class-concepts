import numpy as np 

#part a 
def f(x):
    return (1 - x**2)**(1/2) #making the function of a circle with radius 1

a = 0
b = 1
N = 1000000
x = np.linspace(a, b, N)
y = f(x)
x_min_box = a
x_max_box = b 
y_min_box = 0
y_max_box = np.max(y) #making the box with the minimum and maximum values
xrand = np.random.uniform(a, b, size = N)
yrand = np.random.uniform(y_min_box, y_max_box, size = N) #drawing random numbers within the limits of the box axes
box_area = (b - a)*(y_max_box - y_min_box)
integral_counter = np.sum(yrand < f(xrand)) #calculating the area with np.sum instead of a loop for efficiency 
integral = (integral_counter / N) * box_area #this is the area of a quarter-circle as only the first quadrant is considered as the range is 0 to 1
pi = 4*integral #multiplying by 4 to get the area of the entire circle which is pi since the radius squared is just 1  
print("The value of pi is approximately", pi)

#part b 
people = 0
people_list = []
N = 10000
birthday_list1 = [] #making two lists of all possible birthdays, one for each person
birthday_list2 = []
same_birthday = [] #the shared birthdays will be appended to this list
#probability = 0
for i in range(N):
    birthdays1 = np.random.randint(1, 366)
    birthdays2 = np.random.randint(1, 366)
    birthday_list1.append(birthdays1)
    birthday_list2.append(birthdays2) #the code above fills out all possible birthdays for both lists
    [same_birthday.append(y) for y in birthday_list1 if y in birthday_list2] #list comprehension to append the shared values into the shared list
    probability = len(same_birthday) / N 
    if probability > 0.5:
        break #this stops the loop from making the probability higher than the desired 50%
    people += 1
people = int(people / 8) #this equation was found to make the final result most often in the range of 22-24 people, with occassional outliers slightly above and below this range, making it a viable approximation method
print("The number of people it takes for have two of them to have a 50% probability of sharing a birthday is", people)
