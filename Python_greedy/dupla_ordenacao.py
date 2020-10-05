def ORDENAR(A, n):
	for i in range(n):
		change = False
		for j in range(n-i-1):
			if A[j][0] > A[j+1][0]:
				A[j], A[j+1] = A[j+1],A[j]
				change = True
			elif A[j][0] == A[j+1][0] and A[j][1] < A[j+1][1]:
				A[j], A[j+1] = A[j+1],A[j]
				change = True
		if not change:
			break
	return A

def ACT(A,n):
	ORDENAR(A,n)
	prazo = A[0][0]
	lucro = A[0][1]
	for i in range(1,n):
		if A[i][0] != prazo:
			prazo = A[i][0]
			lucro += A[i][1]
	return lucro
	


A = [(2,100),(3,40),(1,80),(2,20),(2,60),(4,10)]
print(ACT(A,len(A)))
