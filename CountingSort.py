def countigSort(A,base):
	k=10
	B = [0 for _ in range(len(A))]
	C = [0 for _ in range(k)]
	#conta os elementos com o mesmo valor e posiciona a soma no indice do valor em C
	for j in range(0,len(A)):
		val = int(A[j][1][base])
		C[val] += 1
	#aumenta consoante as contagens anteriores
	for i in range(1,k):
		C[i] += C[i-1]
	for j in range(len(A)-1,-1,-1):
		val = int(A[j][1][base])
		B[C[val]-1] = A[j]
		C[val] -= 1
	return B