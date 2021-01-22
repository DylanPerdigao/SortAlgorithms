from InsertionSort import *

def orderBy(l,n):
	aux=list()
	for i in range(0,len(l),n):
		aux.append(l[i])
	aux = insertionSort(aux)
	for k in range(0,len(l),n):
		l[k] = aux[int(k/n)]
	return l
		
def shellSort(l,key):
	numbers = key.split("-")
	for i in range(len(numbers)):
		l = orderBy(l,int(numbers[i]))
	return l