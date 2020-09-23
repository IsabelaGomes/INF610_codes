def HOARE(A,l,r):
  p = A[l]
  i = l + 1
  j = r
  while True:
    print(A)
    while i <= j and A[i] < p:
      i += 1
    while i <= j and A[j] > p:
      j -= 1
    if i <= j:
      A[i], A[j] = A[j], A[i]
    else:
      break
  A[l], A[j] = A[j], A[l]
  return j - 1

def MEDIANA(A,l,r):
  s = 0
  while s != (len(A)//2):
    s = HOARE(A,l,r)
    l += 1
  print('A mediana é ', A[s])

L = [6,10,14,8,2,12,4,18,16]
MEDIANA(L,0,len(L)-1)

