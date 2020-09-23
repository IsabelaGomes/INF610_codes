import math 

def POLIGONO(pa,pb,S):
  if len(S) == 0:
    return []
  else:
    S11 = []
    S22 = []
    dmax = i = j = 0
    a = pb[1]-pa[1]
    b = pa[0]-pb[0]
    c = (pa[1]*pb[0])-(pa[0]*pb[1])
    for i in S:
      raiz = math.sqrt(pow(a,2)+pow(b,2))
      dist = abs((a*i[0])+(b*i[1])+c)/raiz
      if dist >= dmax:
        dmax = dist
        pc = i
    for i in S:
      if i == pa or i == pc:
        continue
      det = (pa[0]*pc[1])+(i[0]*pa[1])+(pc[0]*i[1])-(i[0]*pc[1])-(pc[0]*pa[1])-(pa[0]*i[1])
      if det >= 0: #se o ponto está do lado esquerdo de papc
        S11.append(i)
    for j in S:
      if j == pb or j == pc:
        continue
      det = (pb[0]*pc[1])+(j[0]*pb[1])+(pc[0]*j[1])-(j[0]*pc[1])-(pc[0]*pb[1])-(pb[0]*j[1])
      if det <= 0: #se o ponto está do lado direito de pbpc
        S22.append(j)
    POL1 = POLIGONO(pa,pc,S11)
    POL2 = POLIGONO(pc,pb,S22)
    POL = POL1 + POL2
    POL.append(pc)
    return POL
      
def QUICK(S,n):
  EC = []
  S1 = []
  S2 = []
  if n >= 2:
    pa = (999999999,0)
    pb = (-999999999,0)
    for i in range(n):
      if S[i][0] < pa[0]:
        pa = S[i]
      elif S[i][0] > pb[0]:
        pb = S[i]
    EC.append(pa)
    EC.append(pb)
    for i in range(n):
      det = (pa[0]*pb[1])+(S[i][0]*pa[1])+(pb[0]*S[i][1])-(S[i][0]*pb[1])-(pb[0]*pa[1])-(pa[0]*S[i][1])
      if det > 0: #se o ponto está do lado esquerdo
        S1.append(S[i])
      elif det < 0: #se o ponto está do lado direito
        S2.append(S[i])
    S1 = list(dict.fromkeys(S1)) #remove duplicatas
    S2 = list(dict.fromkeys(S2)) #remove duplicatas
    EC1 = POLIGONO(pa,pb,S1)
    EC2 = POLIGONO(pb,pa,S2)
    return (EC + EC1 + EC2)

S = [(-4859,-2505),(-4631,7689),(9042,1071),(734,2545),(-5521,-1048),(7228,-1358),(-1331,-1942),(-2623,776),(-3105,1812),(-1347,12),(1730,2512),(-1228,-8034),(-5535,2868),(-674,9659),(747,-8281),(-3995,-3835),(8401,-8613),(-7329,9165),(5314,6370),(8292,-2532),(5757,8006),(2923,-129),(-694,-6099),(2194,8615),(-2897,-558),(3940,878),(7503,-7509),(-2084,-3210),(914,-7544),(-7930,-9064),(7615,889),(-627,6597),(6873,-8306),(-4047,-7924),(8472,2561),(2441,4987),(-396,-5508),(7105,-5358),(-9295,-3924),(-7458,9659),(3852,-4085),(2256,-3047),(686,9659),(8960,-3399),(5411,-3749),(884,4289),(5672,-8346),(5788,184),(5226,1242),(6014,4442)]
QUICK(S,len(S))
print(S)
