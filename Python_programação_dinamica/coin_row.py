def COINROW(C,n):
    M = [False]*(n+1)
    F = [0]*(n+1)
    F[0] = 0
    F[1] = C[1]  
    for i in range(2,n+1):
        if (C[i]+F[i-2]) > F[i-1]:
            #if i == 2:
             #   M[1] = True
            F[i] = C[i]+F[i-2]
            M[i] = True
        else:
            F[i] = F[i-1]
            if i == 2:
                M[1] = True
    PRINTRES(M,C)
    return F[n-1]

def PRINTRES(M,C):
    print("Moedas coletadas: ")
    for i in range(n):
        if M[i] == True:
            print(C[i])

C = [0,10,2,4,20,12,1]
n = 6
print("Valor máximo coletado: ",COINROW(C,n))

