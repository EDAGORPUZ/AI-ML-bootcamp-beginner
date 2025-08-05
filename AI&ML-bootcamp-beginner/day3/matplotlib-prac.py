import matplotlib.pyplot as plt
import numpy as np

#LİNE GRAPH
x_ages = np.array([20, 40])          #x values between 20 and 40
y_salaries = np.array([25000, 35000])    #x values between 25k and 35k

plt.xlabel('age')               #title of the x label
plt.ylabel('salary')
plt.title('salaries and ages')

y_py_salaries = np.array([10000, 50000])

plt.plot(x_ages,y_py_salaries,'k--',label = 'python dev')     #p1+ p2 = x and y definitions , p3 = colour and linestyle , p4 = title  

plt.plot(x_ages, y_salaries, marker = 'o' ,color= 'b' ,label = 'all devs')          

plt.grid(True)     #add layout

plt.legend()   #necessary for the graph titles wrk
plt.show()       #like print


#BAR CHART

categories = ['c++', 'python', 'java']
users = [40, 50, 30]

plt.bar(categories, users, color = 'g' )
plt.title('bar chart')
plt.ylabel('number of users')
plt.xlabel('categories')

plt.show()

# HORİZONTAL BAR CHART

X = ['math', 'physical', 'chemistry']
y = [70, 80, 50]

plt.barh(X, y, color = 'k')
plt.title('HORİZONTAL BAR CHART')
plt.ylabel('points')
plt.xlabel('classes')

plt.show()


#PİE CHART

names = ['ayşe', 'ali', 'mehmet', 'fatma']
rate = [50, 40, 70, 95]

plt.pie(rate, labels = names, autopct = '%1.1f%%')  #autopct = rates(float)
plt.title('PİE CHART')
plt.axis('equal')

plt.show()

#SCATTER CHART

# plt.scatter() = dot graph