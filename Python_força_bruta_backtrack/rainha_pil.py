'''
O algoritmo dispõe n rainhas em um tabuleiro utilizando backtracking com pilha. 
'''
class pilha:
    size = 0
    p = []

    def push(self, item): #insere elemento no topo da pilha
        self.p.append(item)
        self.size = len(self.p)
        
    def pop(self): #retira elemento do topo da pilha
        self.p.pop(-1)
        self.size = len(self.p)

    def clear(self): #esvazia a pilha
        while len(self.p)>0:
            self.p.pop(-1)

def Q_CAN(pos,queen,col): #verifica se é possível adicionar a rainha em dada posição
    i = 1
    while (i < queen):
        if pos.p[i-1][1]== col or abs(queen - i) == abs(col - pos.p[i-1][1]):
            return False
        i += 1
    return True

def P_SOL(pos, n): #imprime as soluções na tela
    print('Solução: [', end='') 
    for k in range(pos.size-1):
        print(str(pos.p[k][1]) + ',', end='')
    print(str(pos.p[-1][1]) + ']')

    for i in range(1,n+1):
        for j in range(1,n+1):
            if j == pos.p[i-1][1]:
                print(i, end = ' ')
            else:
                print('-', end = ' ')
        print()
    print()

def Q_PIL(pos,n):
    aloc = False #variável que verifica se a rainha está alocada
    q = c2 = 1
    while not aloc and q <= n: #faz o loop para todas as rainhas
        for c1 in range(c2,n+1):
            if q == 2 and pos.size == 0: #verifica se já chegou na última solução
                return
            print(pos.p)
            if Q_CAN(pos,q,c1):
                pos.push((q,c1))
                aloc = True
                break
        if aloc == False and pos.size > 0: #uma rainha não pode ser alocada
            c2 = pos.p[-1][1]+1
            pos.pop()
            q -= 1 #volta uma rainha
        else: #a rainha foi bem alocada e se faz um incremento no loop
            q += 1
            aloc = False
            c2 = 1
        if pos.size == n: #encontrou uma solução
            P_SOL(pos,n)
            c2 = pos.p[0][1]+1
            pos.clear()
            q = 1
            aloc = False
            
n = 4
pos = pilha()
print('Número de rainhas: ' + str(n))
Q_PIL(pos,n)
        
