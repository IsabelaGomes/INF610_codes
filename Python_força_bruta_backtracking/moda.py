def M_FRQ(A):
    n_occ = 0; m_frq = A[0]; count = 1; x = 0
    #o contador se inicia em 1, pois um termo aparece ao menos uma vez
    for i in range(len(A)): #percorre todo o array
        for j in range(i+1, len(A)):
            #Cada elemento é comparado com os elementos a frente no array
            if A[i] == A[j]:
                count += 1
            x +=1
        if count > n_occ: #assume os valores mais frequentes
            n_occ = count
            m_frq = A[i]
        count = 1 #reinicia o Contador para verificar o próximo elemento
    return m_frq, n_occ, x


A = [3,4,1,3,4,6,4,5,3,4]
print(M_FRQ(A))
