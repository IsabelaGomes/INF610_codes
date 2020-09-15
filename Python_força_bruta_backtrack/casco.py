'''
O algoritmo a seguir detrmina os pontos pertencentes ao casco convexo de um polígono.
O input é um array de pontos, repetidos ou não, e se percorre esse array montando pares
a fim de se obter a equação de uma reta. A partir daí, se verifica se todos os pontos
restantes estão em um mesmo semi-plano através de variáveis booleanas. Se existir pelo
menos um ponto em um semi-plano diferente dos outros, as duas variáveis de verificação
terão o mesmo valor e isso significa que os pontos testados não pertencem ao casco. Se
forem diferentes, significa que todos os pontos obedecem a mesma condição e o par testado
está no casco.
'''

def CASCO(P):
    casco = []
    for i in range(len(P)):
        for j in range(i+1,len(P)): 
            a = P[j][1]-P[i][1]
            b = P[i][0]-P[j][0]
            c = (P[i][0]*P[j][1])-(P[i][1]*P[j][0])
            ver1 = ver2 = False
            for k in range(len(P)):
                if (P[k]!=P[i] and P[k]!=P[j]):
                    r = ((a*P[k][0])+(b*P[k][1])-c)
                    if r <= 0:
                        ver1 = True
                    elif r >= 0:
                        ver2 = True
            if ver1 != ver2:
                casco.append(P[i])
                casco.append(P[j])
    casco = list(dict.fromkeys(casco))#remove duplicatas
    return casco

#n = 12
P12 = [(8,7),(8,3),(7,4),(6,5),(6,1),(5,6),(5,3),(4,2),(3,5),(2,2),(8,7),(3,5)]

#n = 50
P50 = [(-4859,-2505),(-4631,7689),(9042,1071),(734,2545),(-5521,-1048),(7228,-1358),(-1331,-1942),(-2623,776),(-3105,1812),(-1347,12),(1730,2512),(-1228,-8034),(-5535,2868),(-674,9659),(747,-8281),(-3995,-3835),(8401,-8613),(-7329,9165),(5314,6370),(8292,-2532),(5757,8006),(2923,-129),(-694,-6099),(2194,8615),(-2897,-558),(3940,878),(7503,-7509),(-2084,-3210),(914,-7544),(-7930,-9064),(7615,889),(-627,6597),(6873,-8306),(-4047,-7924),(8472,2561),(2441,4987),(-396,-5508),(7105,-5358),(-9295,-3924),(-7458,9659),(3852,-4085),(2256,-3047),(686,9659),(8960,-3399),(5411,-3749),(884,4289),(5672,-8346),(5788,184),(5226,1242),(6014,4442)]

print("Os pontos pertencentes ao casco do conjunto de 12 pontos são: " + str(CASCO(P12)))
print('      ')
print("Os pontos pertencentes ao casco do conjunto de 50 pontos são: " + str(CASCO(P50)))



