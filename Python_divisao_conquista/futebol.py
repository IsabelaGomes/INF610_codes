import numpy as np

def FUTEBOL(times,T,n):
  if n == 2:
    T[0].append(times[1])
    T[0].append(times[0])
    return -1
  else:
    A = times[:n//2]
    B = times[n//2:]

    C1 = FUTEBOL(A,T,len(A))
    C2 = FUTEBOL(B,T,len(B))

    sup = PREENCHE_SUPERIOR(B)
    inf = PREENCHE_INFERIOR(A)
      
    aux = np.concatenate((sup, inf), axis=1) #empilha
    if type(C1) is not int: 
      tmp = np.concatenate((C1, C2), axis=1) #empilha
      aux = np.concatenate((tmp, aux), axis=0)#junta na horizontal
    
    return aux

def PREENCHE_SUPERIOR(vetor):
  M = [vetor]
  
  i = -1
  for j in range(0, len(vetor)-1):
    i += 1
    a = i+1
    
    temp = []
    while a != i:
      temp.append(vetor[a])
      a += 1
      a = a%len(vetor)
      
    temp.append(vetor[a])
    M.append(temp)
    del temp
  return M
          
        
def PREENCHE_INFERIOR(vetor):
  n = len(vetor)
  M = np.zeros((n,n), dtype=int)
  for i in range(n):
    for j in range(n):
        if i == j:
          M[i][j] = vetor[0]
        elif i > j:
          M[i][j] = vetor[i - j]
        else:
          M[i][j] = vetor[n-(j-i)]
  return np.transpose(M.tolist()) 
  

n = 16
times = []
for i in range(1,n+1):
  times.append(i)
T = [[]]
fut = FUTEBOL(times,T,n)
print(np.transpose(np.concatenate((T, fut), axis=0)))
