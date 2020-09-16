def SUM2 (x, A):
    for i in range(len(A)):
        for j in range(i,len(A)):
            sum2 = A[i] + A[j]
            if x == sum2:
                print('A soma de '+str(A[i])+' e '+str(A[j])+' é '+str(x))
                  
A = [1,2,3,4]
SUM2(4,A)
