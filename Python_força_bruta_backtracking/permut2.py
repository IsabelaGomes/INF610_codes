def PER(n,v,a): #left e right são posições
    if len(v) == n: #left chegou no fim do array
        aux = []
        for i in v:
            aux.append(i)
        a.append(aux)
        print(v) #exibe uma permutação
    else:
        for i in range(1,n+1): #varre todos os valores
            if not i in v:
                v.append(i)
                PER(n,v,a)
                v.pop()

v = []
n = 3
a = []
PER(n,v,a)
print('*')
print(a)
