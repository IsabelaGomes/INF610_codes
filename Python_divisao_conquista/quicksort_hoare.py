import datetime

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
  print('A: ' + str(A))
  return j

def QUICKSORT_HOARE(A,l,r):
  if l >= r:
    return
  s = HOARE(A,l,r)
  QUICKSORT_HOARE(A,l,s-1)
  QUICKSORT_HOARE(A,s+1,r)

A = [310, 285, 179, 652, 351, 423, 861, 254, 450, 520]
start = datetime.datetime.now()
print('A: ' + str(A))
QUICKSORT_HOARE(A,0,len(A) - 1)
print(A)
end = datetime.datetime.now()
print((end - start).total_seconds()*1000)
