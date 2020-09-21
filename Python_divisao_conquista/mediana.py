def HOARE(A,l,r):
  p = A[l]
  i = l + 1
  j = r
  print('O pivô é ' + str(p))
  while True:
    while i <= j and A[i] <= p:
      i += 1
    while i <= j and A[j] >= p:
      j -= 1
    if i <= j:
      A[i], A[j] = A[j], A[i]
    else:
      break
  A[l], A[j] = A[j], A[l]
  print('\nA: ' + str(A))
  return j

def QUICKSORT_HOARE(A,l,r):
  if l >= r:
    return
  s = HOARE(A,l,r)
  QUICKSORT_HOARE(A,l,s-1)
  QUICKSORT_HOARE(A,s+1,r)

L = [6, 10, 14, 8, 2, 12, 4, 18, 16]
n = len(L)
print('\nA: ' + str(L))
QUICKSORT_HOARE(L,0,n - 1)
n = len(L)
if n%2 == 0:
  print('\nA mediana é ' + str((L[n//2] + L[n//2-1])/2))
else:
  print('\nA mediana é ' + str(L[n//2]))
