from CountingSort import *

def getMax(l):
	maximum = 0
	for elem in l:
		if int(elem[1])>maximum:
			maximum = int(elem[1])
	return maximum

def radixSort(l):
	maxDigit = len(str(getMax(l)))
	i=0
	for base in range(maxDigit-1,-1,-1):
		l=countigSort(l,base)
	return l

