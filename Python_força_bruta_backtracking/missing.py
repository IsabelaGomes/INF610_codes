def MISS(A):
    soma = int(((len(A)+2)*(len(A)+1))/2) #soma dos n termos
    for i in range(len(A)): #percorre todo o array
        soma = soma - A[i] #subtrai todos os termos presentes no array
        print(soma)
    return soma #o resultado que sobra é o número que falta

def MISSR(A):
    miss = False
    for i in range(1, len(A)+2): #varre os valores
        print(i)
        isin = False #assumir que o elemento não está no array
        for j in range(len(A)): #percorre todo o array
            if A[j]==i: #operação base
                isin = True #encontrou o valor
                break  #saiu do loop interno
        if not isin: #se não encontrou o valor
            return i #retorna o que está faltando
   

B = [1,4,2,7,6,3]
C = [2,3,1,5]
print(MISS(C), MISSR(C))

