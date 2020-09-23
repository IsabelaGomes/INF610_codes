def ORD2(A):
    i = j = 1
    while i < len(A):
        print(A)
        if A[i-1] > A[i]:
            A[i-1],A[i] = A[i],A[i-1]
        else:
            j = i
            i += 1
    return A

print(ORD2([3,2,3,2,3,2,3,3,3,3,2]))
