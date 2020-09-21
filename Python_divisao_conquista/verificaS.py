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

L = [1,2,3,4,5,6,7]
VERSOMA(L,4)
