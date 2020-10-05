import numpy as np

def MOCHILA(item,capa,isin):
    if item == 0 or capa == 0:
        return 0
    if capa < Pesos[item-1]:
        valor = MOCHILA(item-1,capa,isin)
        isin[item-1] = True
    else:
        a = MOCHILA(item-1,capa,isin)
        b = (Valores[item-1]+MOCHILA(item-1,capa-Pesos[item-1],isin))
        if a >= b:
            valor = a
            isin[item-1] = False
        else:
            valor = b
            isin[item-1] = True
    F[item][capa] = valor
    return F[item][capa]

W = 6
Pesos = [1,2,3,4] 
Valores = [1,3,4,6]
n = len(Valores)
isin = [False]*n

F = np.zeros((n+1,W+1))
for i in range(1,n+1):
    for j in range(1,W+1):
        F[i][j] = 1

otimo = MOCHILA(n,W,isin)
print("O valor máximo que pode ser armazenado na mochila é ",otimo)
print("Itens na mochila:", end=" ")
for i in range(n):
    if isin[i]:
        print(i+1,end=" ")
print()
print(F)

