import datetime

def MERGE(B,C,A):
  i = j = k = 0
  p = len(B)
  q = len(C)
  while i < p and j < q:
    if B[i] <= C[j]:
      A[k] = B[i]
      i += 1
    else:
      A[k] = C[j]
      j += 1
    k += 1
  while i < p:
    A[k] = B[i]
    i += 1
    k += 1
  while j < q:
    A[k] = C[j]
    j += 1
    k += 1

def MERGESORT(A):
  n = len(A)
  B = A[:n//2]
  C = A[n//2:]
  if n > 1:
    B = A[:n//2]
    C = A[n//2:]
    MERGESORT(B)
    MERGESORT(C)
    MERGE(B,C,A)

A = [2,3,3,3,3,3,2,3,2]
start = datetime.datetime.now()
MERGESORT(A)
print(A)
end = datetime.datetime.now()
print((end - start).total_seconds()*1000)
