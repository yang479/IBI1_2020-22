import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#os.chdir("/home/Aa\ Bb/desktop/Practical7") #change the working directory
covid_data = pd.read_csv("full_data.csv")
#The code for importing the .csv file works

'''
#print(covid_data.head(10)) #show tile line(without numbers) and the first five lines(0-4)
#print(covid_data.info()) #show:1 element number in each colunm 2 show type of title in each column 3 memory usage
#print(covid_data.describe()) #show entries, mean, standard deviation and a quantiles
#(new cases)mean:194.546773 median:0 (total death)0-37272
#print(covid_data.iloc[0,1]) #True:show the Afghanistan in [0,1]
#print(covid_data.iloc[2,0:5]) #line 2, column 0-5
#print(covid_data.iloc[0:2,:]) #line 0-2, column all
#print(covid_data.iloc[0:10:2,0:5]) #line 0,2,4,6,8,no 10  column 0-5
#print(covid_data.iloc[0:3,[0,1,3]]) #line 0-3, column 0,1,3
#my_columns = [True, True, False, True, False, False]
#print(covid_data.iloc[0:3,my_columns]) #line 0-3, column 0,1,3
#print(covid_data.loc[2:4,"date"]) #line 2-4, column tile "date"
#covid_data.loc[every row where location is "Afghanistan","total_cases"] #covid_data.loc[0:81,"total_cases"]
'''


print(covid_data.iloc[0:12:2,])
#Correct code for showing all columns, and every second row between (and including) 0 and 10

total = len(open("full_data.csv").readlines()) #number of lines
b=[]
for i in range(0,total-1): #read the file
	LC=covid_data.loc[i,"location"]
	if LC=="Afghanistan":# find the lines with Afhanistan
		b+=[i]
		B=covid_data.loc[b,:]
print(B) #print the result
#a Boolean to show “total cases” for all rows corresponding to Afghanistan


total = len(open("full_data.csv").readlines()) #number of lines
a=[]
b=[]
c=[]
for i in range(0,total-1): #read the file
	LC=covid_data.loc[i,"location"]

	if LC=="World": # find the lines with world
		b+=[i]
'''
        if LC=="China": #find the lines with China
		c+=[i]
	if LC=='United Kingdom': # find the lines with American
		a+=[i]
'''

B=covid_data.loc[b,["date","new_cases"]] #select the column
print(B.describe())
#mean:8454.326087   median:2023.500000 They are quite different.Mean is much biger than median.
#Intrepretation:To determine the characteristics of the whole data,we should inspect many them from many aspects.
#computed the mean and median of new cases for the entire world

world_dates=covid_data.loc[b,"date"]
world_new_cases=covid_data.loc[b,"new_cases"]
plt.title('New cases worldwide')
plt.xlabel('date')
plt.ylabel('number')
plt.plot(world_dates, world_new_cases, 'r+') #(hypothesis)r(red):the colour of data +:the shape of data
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90) #add the xticks
plt.show()
B.to_csv('World.csv') #output the file
#The peak is on the left. It means mean is biger than median.That is right.
#created a boxplot of new cases worldwide

'''
China_dates=covid_data.loc[c,"date"]
China_new_cases=covid_data.loc[c,"new_cases"]
America_dates=covid_data.loc[a,"date"]
America_new_cases=covid_data.loc[a,"new_cases"]
plt.title('New cases in England and China')
plt.xlabel('date')
plt.ylabel('number')
plt.plot(China_dates, China_new_cases, 'b+')
plt.plot(America_dates, America_new_cases, 'r+')
'''


world_new_deaths=covid_data.loc[b,"new_deaths"]
plt.title('New cases(red) and new deaths(blue) worldwide.')
plt.xlabel('date')
plt.ylabel('number')
plt.plot(world_dates, world_new_deaths, 'r+')
plt.plot(world_dates, world_new_cases, 'bo')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90) #add the xticks
plt.show()
#plotted both new cases and new deaths worldwide.


#There is code to answer the question stated in file question.txt
#question:How have new cases and total cases developed over time in Spain?
s=[]
for i in range(0,total-1): #read the file
        LC=covid_data.loc[i,"location"]
        if LC=="Spain": # find the lines with world
                s+=[i] #select the column
spain_total_cases=covid_data.loc[s,"total_cases"]
spain_new_cases=covid_data.loc[s,"new_cases"]
spain_dates=covid_data.loc[s,"date"]
plt.plot(spain_dates, spain_total_cases, 'b+')
plt.plot(spain_dates, spain_new_cases, 'r+')
plt.xticks(spain_dates.iloc[0:len(spain_dates):4],rotation=-90) #add the xticks

plt.title('Total cases(blue) and new cases(red) in Spain')
plt.xlabel('date')
plt.ylabel('cases')
plt.show()
