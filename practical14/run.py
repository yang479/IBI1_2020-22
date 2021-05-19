
#I chose carbohydrate
from xml.dom.minidom import parse
import xml.dom.minidom
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

import sys
sys.setrecursionlimit(500000) #increase the number of recursion


DOMTree = xml.dom.minidom.parse("go_obo.xml") #open the file
xnl = DOMTree.documentElement
terms = xnl.getElementsByTagName("term") #select all terms


Dic={}
#set the default data

for term in terms: #collect all childnodes and ids in terms
	id=term.getElementsByTagName('id')
	Dic[id[0].firstChild.data]=[]
for term in terms:
	id=term.getElementsByTagName('id')
	is_as=term.getElementsByTagName('is_a')
	for is_a in is_as: #link the childnodes and ids to establish the dictionaty
        	Dic[is_a.firstChild.data].append(id[0].firstChild.data)
#print(Dic)

'''
def count(a):
    for term in terms:
        if a in term.getElementsByTagName('defstr')[0].firstChild.data:#if 'a' exist in defstr, we thought we find what we need
            ids=term.getElementsByTagName('id')[0].firstChild.data#get the id information
            if dictionary[ids] !=[]:
                counter=dictionary[ids]
                n=count2(counter)
    print('the childnode number of '+a+' is '+str(n))
    return n
def count2(counter):
    for i in range(len(counter)):
        if counter[i] not in listf:
            listf.append(counter[i])#put the childnodes into listf
            count2(dictionary[counter[i]])#put the 'grandchildnodes' into listf
    return len(listf)
listf=[]#listf is used to store the childnodes
'''




def measure(what):
	number=0
	for term in terms:
		if what in term.getElementsByTagName('defstr')[0].firstChild.data: #determine the type of substances showed in the 'defstr'
			id_what=term.getElementsByTagName('id')[0].firstChild.data #collect the ids of the type'what'
			if Dic[id_what]!=[]:
				Tag=Dic[id_what]
				number=f(Tag)
	return number
def f(Tag):
	for i in range(len(Tag)):
		if Tag[i] not in List:
			List.append(Tag[i]) #collect the childnodes by list
			f(Dic[Tag[i]]) #collect the childnodes of childnodes
	return len(List)
List=[]
DNA=measure('DNA')
print('the number of childnodes of DNA is',str(DNA))

List=[]
RNA=measure('RNA')
print('the number of childnodes of RNA is',str(RNA))

List=[]
protein=measure('protein')
print('the number of childnodes of protein is',str(protein))

List=[]
carbohydrate=measure('carbohydrate') #I chose carbohydrate#I chose carbohydrate
print('the number of childnodes of carbohydrate is',str(carbohydrate))

#draw the pie chart
DNAp=DNA/(DNA+RNA+protein+carbohydrate)
RNAp=RNA/(DNA+RNA+protein+carbohydrate)
proteinp=protein/(DNA+RNA+protein+carbohydrate)
carbohydratep=carbohydrate/(DNA+RNA+protein+carbohydrate)
#caculate the ratio
#I doubt whether it is necessary, because the pie chart will calculate the ratio automatically in my version of python.
substances=[DNAp,RNAp,proteinp,carbohydratep] #input the data
labels='DNA','RNA','protein','carbohydrate' #label the name
plt.pie(substances,explode=(0.1,0.1,0,0.1),labels=labels,autopct='%1.2f%%',shadow=True,startangle=90) #draw the pie chart
plt.title("The childnode number of DNA, RNA, protein and carbohydrate") #add the title
plt.show() #print it

