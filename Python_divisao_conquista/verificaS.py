'''
def VERSOMA(A,x):
  i = 0 #setar o ponteiro na primeira posição
  j = len(A)-1 #setar o ponteiro na última posição
  while i < len(A) and j > 0:
    if (j - i) == 1 and (A[i] + A[j]) != x: #não encontrou os valores
      print('Não existe termos na lista cuja soma é '+ str(x))
      return
    if (A[i] + A[j]) == x: #encontrou os valores
      print('Os termos '+ str(A[i]) +' '+ str(A[j]) +' somados são '+ str(x))
      return
    elif (A[i] + A[j]) > x:
      j -= 1 #caminha uma posição para trás
    else:
      i += 1 #caminha uma posição para frente
'''

def VERSOMA(A,x):
  for i in range(len(A)):
    l = i + 1
    r = len(A)-1
    while l <= r:
      m = (l+r)//2
      if A[i]+A[m] == x:
        print('Os termos ',A[i],' ',A[m],' somados são ',x)
        return
      elif A[i]+A[m] > x:
        r = m - 1
      else:
        l = m + 1
  print('Não existe termos na lista cuja soma é ',x)
  return
  
L = [1,2,3,4,5,6,7]
VERSOMA(L,10)
