def SUBCON(L): 
    F = []   
    subcon = [F] 
    for i in range(len(L)): 
        orig = subcon[:] 
        new = L[i] 
        for j in range(len(subcon)): 
            subcon[j] = subcon[j] + [new] 
        subcon = orig + subcon 
    print('Subconjuntos: ',subcon)
    return subcon

def MOCHILA_BF(itens,W):
    res = []
    subcon = SUBCON(itens)
    for i in subcon:
        v = 0
        w = 0
        for j in range(len(i)):
            v = v + Valores[i[j]]
            w = w + Pesos[i[j]]
        res.append((i,v,w))
    for i in range(1,len(res)):
        if res[i][2] <= W:
            if res[i-1][1] > res[i][1]:
                fim = res[i-1]
            else:
                fim = res[i]
    print('O maior valor que pode ser transportado é ',fim[1])
    print('Os objetos escolhidos são: ',end='')
    for obj in fim[0]:
        print(obj+1,end=' ')
    return fim

W = 5
Pesos = [2,1,3,2] 
Valores = [12,10,20,15]
n = len(Valores)
itens = []
for i in range(n):
    itens.append(i)

MOCHILA_BF(itens,W)
