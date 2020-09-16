def DISCORD(A):
    c = 0
    for i in range(1,len(A)):
        if A[i] == A[0]:
            while A[i-1]!= A[0]:
                aux = A[i-1]
                A[i-1] = A[i]
                A[i] = aux
                i-=1
                c+=4
    print(c)
    return A
            
A = [1,0,1,0]
print(DISCORD(A))
