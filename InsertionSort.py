def insertionSort(l):
	aux = list()
	for i in range(1,len(l)):
		k = i-1
		while l[i][1]<l[k][1]:
			k-=1
		k+=1 
		aux = l[i]
		for m in range(i-1,k-1,-1):
			l[m+1] = l[m]
		l[k]=aux
	return l