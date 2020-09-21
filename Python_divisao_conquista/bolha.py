import datetime

def BOLHA(A,n):
  for i in range(n-1):
    trocou = False
    for j in range(n-i-1):
      if A[j] > A[j+1]:
        aux = A[j]
        A[j] = A[j+1]
        A[j+1] = aux
        trocou = True
    if not trocou:
      break
  return A

A = [66709,39482,38777,69390,81582,28526,40604,28810,58641,31634,23831,64689,84356,48212,17448]
start = datetime.datetime.now()
print(BOLHA(A,len(A)))
end = datetime.datetime.now()
print((end - start).total_seconds()*1000)
