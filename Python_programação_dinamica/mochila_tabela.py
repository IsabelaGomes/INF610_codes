import numpy as np

def TABLE_MOCHILA(n,W):
    for i in range(1,n+1):
        for j in range(1,W+1):
            if j - Pesos[i-1] < 0:
                F[i][j] = F[i-1][j]
            else:
                F[i][j] = max(F[i-1][j],Valores[i-1]+F[i-1][j - Pesos[i-1]])
    return F[n][W]

def P_MOCHILA_TABLE(F,W,n):
    capa = W
    res = F[n][W]
    cam =[]
    for i in range(n,0,-1):
        if res <= 0:
            break
        if res == F[i-1][capa]:
            continue
        else:
            cam.append(i)
            res -= Valores[i-1]
            capa -= Pesos[i-1]
    print('Itens na mochila: ',cam)
                       
W = 6
Pesos = [1,2,3,4] 
Valores = [1,3,4,6]
n = len(Valores)

F = np.zeros((n+1,W+1))
for i in range(1,n+1):
    for j in range(1,W+1):
        F[i][j] = 1

otimo = TABLE_MOCHILA(n,W)
P_MOCHILA_TABLE(F,W,n)
print("O valor máximo que pode ser armazenado na mochila é ",otimo)
print(F)

