import datetime

def HOARE(A,l,r):
  p = A[l]
  i = l + 1
  j = r
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
  return j

def QUICKSORT_HOARE(A,l,r):
  if l < r:
    s = HOARE(A,l,r)
    QUICKSORT_HOARE(A,l,s-1)
    QUICKSORT_HOARE(A,s+1,r)
  
A = [2,3,3,3,3,3,2,3,2]
start = datetime.datetime.now()
QUICKSORT_HOARE(A,0,len(A) - 1)
print(A)
end = datetime.datetime.now()
print((end - start).total_seconds()*1000)
