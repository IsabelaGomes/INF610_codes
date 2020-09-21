import datetime

def INSERTION_SORT(A):
  for i in range(len(A)):
    v = A[i]
    j = i - 1
    while j >= 0 and A[j] > v:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = v

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

def QUICKSORT_INS(A,l,r):
  if r - l < 16:
    INSERTION_SORT(A)
  else:
    s = HOARE(A)
    QUICKSORT_INS(A,l,s-1)
    QUICKSORT_INS(A,s+1,r)

A = [66709,39482,38777,69390,81582,28526,40604,28810,58641,31634,23831,64689,84356,48212,17448]
start = datetime.datetime.now()
QUICKSORT_INS(A,0,len(A) - 1)
print(A)
end = datetime.datetime.now()
print((end - start).total_seconds()*1000)
