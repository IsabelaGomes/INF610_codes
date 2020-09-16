import time

def CAIXEIRO(n,D,ciclo,l,r,pack):
    if l == r: #gerou uma permutação
        comp = i = 0
        while i < n: #calcula o comprimento do caminho
            comp += D[ciclo[i]-1][ciclo[i+1]-1]
            i += 1
        aux = [] #salva o ciclo 
        for i in ciclo:
            aux.append(i)
        pack.append((comp,aux))
        return pack #retorna a permutação com sua distância
        
    else:
        for i in range(l,r): #varre todos os valores excluindo o primeiro
            aux = ciclo[l]  
            ciclo[l] = ciclo[i]
            ciclo[i] = aux
            pack = CAIXEIRO(n,D,ciclo,l+1,r,pack)
            aux = ciclo[l] 
            ciclo[l] = ciclo[i]
            ciclo[i] = aux
        return pack #retorna a lista de permutações com suas distâncias

def OTM_CAIXEIRO(pack,minimo,otimo):
    for i in range(len(conjunto)): #varre todos os valores
        if conjunto[i][0] <= minimo: #identifica o mínimo
            teste = minimo
            minimo = conjunto[i][0]
            if teste != minimo: #se o minino recebe novo valor, reinia a lista de ciclos
                otimo.clear()
            otimo.append(conjunto[i][1]) #adiciona o ciclo hamiltoniano na lista de caminhos ótimos
    return otimo, minimo

#n = 10
#D = [[0,31,4,39,25,1,27,15,18,24],[31,0,26,16,11,31,27,18,12,11],[4,26,0,35,21,5,24,11,14,20],[39,16,35,0,26,39,22,24,22,26],[25,11,21,26,0,26,32,17,11,1],[1,31,5,39,26,0,26,15,19,25],[27,27,24,22,32,26,0,16,21,31],[15,18,11,24,17,15,16,0,7,16],[18,12,14,22,11,19,21,7,0,10],[24,11,20,26,1,25,31,16,10,0]]
#n = 12
#D = [[0,31,22,17,4,22,8,18,19,6,15,7],[31,0,11,19,28,23,25,13,12,37,24,30],[22,11,0,16,19,13,15,9,5,27,20,20],[17,19,16,0,13,25,15,7,11,22,4,20],[4,28,19,13,0,21,6,15,16,9,12,8],[22,23,13,25,21,0,15,20,17,25,28,16],[8,25,15,15,6,15,0,14,13,13,16,5],[18,13,9,7,15,20,14,0,4,24,11,19],[19,12,5,11,16,17,13,4,0,25,14,18],[6,37,27,22,9,25,13,24,25,0,20,9],[15,24,20,4,12,28,16,11,14,20,0,20],[7,30,20,20,8,16,5,19,18,9,20,0]]
#n = 14
#D = [[0,61,92,37,55,87,40,88,15,45,55,52,21,19],[61,0,31,83,51,71,62,52,74,56,14,62,55,70],[92,31,0,112,71,79,87,52,105,80,41,84,85,100],[37,83,112,0,50,75,28,89,25,37,83,39,58,18],[55,51,71,50,0,31,22,38,58,14,59,14,67,48],[87,71,79,75,31,0,50,29,88,43,82,37,98,78],[40,62,87,28,22,50,0,61,38,9,65,13,57,28],[88,52,52,89,38,29,61,0,94,52,65,51,93,85],[15,74,105,25,58,88,38,94,0,45,69,52,35,11],[45,56,80,37,14,43,9,52,45,0,61,9,59,35],[55,14,41,83,59,82,65,65,69,61,0,68,45,67],[52,62,84,39,14,37,13,51,52,9,68,0,68,41],[21,55,85,58,67,98,57,93,35,59,45,68,0,40],[19,70,100,18,48,78,28,85,11,35,67,41,40,0]]
n = 4
D = [[0,31,4,39],[31,0,26,16],[4,26,0,35],[39,16,35,0]]

pack = []
otimo = []

ciclo = []
for i in range(1,n+1):
    ciclo.append(i)
ciclo.append(1)
inicio = time.time()
conjunto = CAIXEIRO(n,D,ciclo,1,n,pack)
otimo, minimo = OTM_CAIXEIRO(conjunto,9999999,otimo)
fim = time.time()
print('Os melhores caminhos para serem percorridos são: ' + str(otimo) + ' cujas distâncias são ' + str(minimo))
print('Tempo de execução: ' + str(fim - inicio))     
