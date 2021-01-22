def insertionSort(l):
	aux = list()
	for i in range(1,len(l)):
		k = i-1
		#ir da direita para a esquerda ate ter o elem i<k
		while l[i][1]<l[k][1]:
			k-=1
		k+=1 #para compensar a volta no ciclo a mais
		aux = l[i]
		# SHIFT para a direita comecando a direita
		for m in range(i-1,k-1,-1):
			l[m+1] = l[m]
		l[k]=aux
	return l