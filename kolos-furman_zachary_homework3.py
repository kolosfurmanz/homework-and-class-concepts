import numpy as np 

annual_data = np.loadtxt('annual_csv.csv', dtype = 'float', delimiter = ' ', usecols = (1,2), skiprows = 1)
average_data = np.loadtxt('annual_csv_average.csv', dtype = 'float', delimiter = '\t', skiprows = 1)
#Importing the data from the csv files as floats and separating the values into axes with delimiters. The average data had a strange delimiter which wasn't a space, which is why the "\t" was necessary. Columns 1 and 2 were used in the annual data and both skipped the first row since that was just for headings. 
annual_data = np.flip(annual_data, 0)
average_data = np.flip(average_data, 0)
#Flipping the data around the first axis so it is in chronological order. 
#I'd like to shout out Austin for helping me out with this part as I was not familiar with the nuances of np.loadtxt and np.flip.
an_list_temp = []
an_list_year = []
av_list_temp = []
av_list_year = []
#Making empty lists for both the temperatures and years so they can be plotted as axes.

for i in annual_data: 
    an_list_year.append(i[0])
    an_list_temp.append(i[1]) 
    #This separates the year and temperature into separate lists with the data for each in them as they are appended throughout the duration of the for loop. 
    an_deriv = np.diff(an_list_temp) / np.diff(an_list_year)
    #This is the equation of the derivative itself, the difference of y over the difference of x 
    an_deriv = an_deriv.tolist()
    an_deriv.append(0)
#The derivative was made into a list here so 0 could be appended in order for each list to have the same number of terms since the difference between the last term and the last term is zero. 

for j in average_data: 
    av_list_year.append(j[0])
    av_list_temp.append(j[1])
    av_deriv = np.diff(av_list_temp) / np.diff(av_list_year)
    av_deriv = av_deriv.tolist()
    av_deriv.append(0)

import matplotlib.pyplot as plt 
fig, (ax1, ax2) = plt.subplots(2, 1)
x = an_list_year
y = an_deriv
ax1.set_xlabel("Year")
ax1.set_ylabel("Derivative of the mean temperature in degrees Celsius", fontsize = 6, wrap = True)
ax1.set_yticks([-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3])
ax1.set_title("Derivative of the mean temperature of Earth from the years 1880 to 2016", fontsize = 8, wrap = True) 
ax1.plot(x, y, color = 'red')
#This is the code for the first graph as a subplot defined as ax1. 

a = av_list_year 
b = av_deriv 
ax2.set_xlabel("Average year of the bin")
ax2.set_ylabel("Derivative of the bins in degrees Celsius", fontsize = 6, wrap = True)
ax2.set_ylim(-0.02, 0.03)
ax2.set_title("Derivative of 10 year bins of the mean temperature of Earth from the years 1880 to 2009", fontsize = 8, wrap = True)
ax2.plot(a, b, color = 'blue')
plt.subplots_adjust(left = 0.2, bottom = 0.1, right = 0.9, top = 0.9, wspace = 0.4, hspace = 0.7)
#This adjusts the graphs so that they fit on the screen nicely. 
plt.savefig('graphs.png')
#This final line saves the graphs as a png file, which is also committed in the repository. 