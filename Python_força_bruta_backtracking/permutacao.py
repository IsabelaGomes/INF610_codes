def PER(n,left,right): #left e right são posições
    if left == right: #left chegou no fim do array
        print(n) #exibe uma permutação
    else:
        for i in range(left,right): #varre todos os valores
            aux = n[left] #permuta valores 
            n[left] = n[i]
            n[i] = aux
            PER(n, left+1, right)
            aux = n[left] #permuta valores
            n[left] = n[i]
            n[i] = aux

n = [1,2,3,4]
PER(n,0,len(n))
