number={'USA': 29862124,'India': 11285561,'Brazil': 11205972,'Russia': 4360823,'UK': 4234924}
print(number)
#the use of library
#introduce the matplotlib
import matplotlib.pyplot as plt
#the name of each piece of pie
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK'
#the number/rate
sizes=(29862124,11285561,11205972,4360823,4234924)
#the gap length
explode=(0,0.2,0,0,0)
#have shadow, USA at 180 degree
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',
        shadow=True,startangle=180)
plt.axis('equal')
#print
plt.show()

