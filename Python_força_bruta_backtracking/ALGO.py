'''
def ALGO( n ): #considere n potência de 2.
    if (n == 1 ): return 1
    else:
        for i in range (1,8):
            z = ALGO(n//2)
        for i in range (1,n*n*n):
            z = z + 1 # operação básica: soma
    return z

print(ALGO(2))
print(ALGO(4))
'''
def ASTERISCO( n ): 
    if ( n > 0 ):
        ASTERISCO(n-1)
        print('/',end='')
        for i in range (1,n):
            print('*',end='') # operação básica
        ASTERISCO(n-1)
        print('/',end='')
ASTERISCO(4)

