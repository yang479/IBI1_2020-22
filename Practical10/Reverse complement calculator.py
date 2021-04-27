#12 Reverse complement calculator
#def search_for_elmt(L, e):
#	for i in L:
#		if i == e:
#			return True
#	return False
#i=1
#def is_even (i):
#	print ("inside is even")
#	return i%2 == 0
#is_even(98)
#print (is_even)
#def is_even(x):
 #   if x % 2 == 0:
  #     return True
   # else:
    #   return False
#def f(x):
#	x+=1
#	print(' in f(x): x =', x)
#	return x

#x = 3
#z = f(x)
#print(x)
#print(f(x))
#print(z)
#AAAGTCTGAC
'''
L=[182098504]
def (L):
        swap = False
        while not swap:
                swap = True
                for j in range(1,len(L)):
                        if L[j-1:j] > L[j:j+1]:
                                swap = False
                                temp = L[j:j+1]
                                L[j:j+1] = L[j-1:j]
                                L[j-1:j] = temp
                                print(temp)
        return L
bubble_sort(L)
print(bubble_sort(L))
'''


#REAL Work
'''
import re
DNA=input("The DNA sequence is:")
#print(DNA)
duplication={'A':'T','T':'A','C':'G','G':'C'}
n=len(DNA)
Reverse_complement=''
for i in range (n,0,-1):
    Reverse_complement+=duplication[DNA[i-1:i]]
print('Reverse complement=',Reverse_complement)
'''
DNA=input("The DNA sequence is:")
def RC(DNA):
	#import re
	
	duplication={'A':'T','T':'A','C':'G','G':'C'}
	n=len(DNA)
	Reverse_complement=''

	for i in range (n,0,-1):
		Reverse_complement+=duplication[DNA[i-1:i]]
	print('Reverse complement=',Reverse_complement)
	return DNA
RC(DNA)

