'''
O algoritmo dispõe n rainhas em um tabuleiro utilizando backtracking recursivo. 
'''

def Q_CAN(pos,queen,col): #verifica se é possível adicionar a rainha em dada posição
    i = 0
    while (i < queen):
        if pos[i]== col or abs(queen - i) == abs(col - pos[i]):
            return False
        i += 1
    return True

def Q_REC(pos,queen,n):
    if queen == n:
        print('Solução: ' + str(pos))#mostra o array de posição
        for i in range(1,n+1): #mostra o tabuleiro
            for j in range(1,n+1):
                if j == pos[i-1]:
                    print(i, end = ' ')
                else:
                    print('-', end = ' ')
            print()
        print()
    else:
        for c in range(1,n+1):
            if Q_CAN(pos,queen,c):
                pos[queen] = c
                Q_REC(pos,queen+1,n)

R = 0
n = 6
pos=[0]*n
print('Número de rainhas: ' + str(n))
Q_REC(pos,R,n)

