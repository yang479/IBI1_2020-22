L=[182098504]
def bubble_sort(L):
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
L=[182098504]
bubble_sort(L)
print(bubble_sort(L))

