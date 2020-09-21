import datetime

def SELECAO(A,n):
  for i in range(n-1):
    min = i
    for j in range(i+1,n):
      if A[j] < A[min]:
        min = j
    aux = A[i]
    A[i] = A[min]
    A[min] = aux
  return A

A = [66709,39482,38777,69390,81582,28526,40604,28810,58641,31634,23831,64689,84356,48212,17448]
start = datetime.datetime.now()
print(SELECAO(A,len(A)))
end = datetime.datetime.now()
print((end - start).total_seconds()*1000)
