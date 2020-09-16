'''
O algoritmo determina os subconjuntos de um
conjunto S que possuem a mesma soma
'''
def SUBCON_T(S): #verifica se é possivel particionar
        total = sum(S)
        subcon =[]
        if total%2 != 0:
                return -1, -1
        T = [] 
        return SUBCON(S,T)

def SUBCON(S,T): #função de partição
        if sum(S) == sum(T): #operação básica
                return S,T
        #como min() faz n comparações no array, é O(n)
        elif sum(S) > sum(T):
                T.append(min(S))
                S.remove(min(S))
        else:
                S.append(min(T))
                T.remove(min(T))
        return SUBCON(S,T)
  

S = [4,8,1,3,10,2,3,4,8]
S1, S2 = SUBCON_T(S)
if S1 == S2 == -1:
        print('Não existem S1 e S2')
else:
        print(S1,S2)
