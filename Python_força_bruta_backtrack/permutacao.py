
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
'''
def PER(n,left,right): #left e right são posições
    if left == right: #left chegou no fim do array
        print(n)
    else:
        for i in range(left,right): #varre todos os valores
            aux = n[left] #permuta valores 
            n[left] = n[i]
            n[i] = aux
            PER(n, left+1, right)
            aux = n[left] #permuta valores
            n[left] = n[i]
            n[i] = aux

n = [1,2,3]
print(PER(n,0,len(n))

'''
