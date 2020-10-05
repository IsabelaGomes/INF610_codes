def HOARE(A,l,r):
  p = A[l][2]
  i = l + 1
  j = r
  while True:
    while i <= j and A[i][2] <= p:
      i += 1
    while i <= j and A[j][2] >= p:
      j -= 1
    if i <= j:
      A[i], A[j] = A[j], A[i]
    else:
      break
  A[l], A[j] = A[j], A[l]
  return j

def QUICK(A,l,r):
  if l < r:
    s = HOARE(A,l,r)
    QUICK(A,l,s-1)
    QUICK(A,s+1,r)

def MAKE_SETS(n):
    for i in range(n):
        raiz[i] = i
        prox[i] = i
        size[i] = 1

def FIND_SET(i):
    return raiz[i]

def UNION(u,v):
    ru = raiz[u]
    rv = raiz[v]
    if size[ru] < size[rv]:
        size[rv] += size[ru]
        raiz[ru] = rv
        j = prox[ru]
        while j != ru:
            raiz[j] = rv
            j=prox[j]
        prox[ru],prox[rv] = prox[rv],prox[ru]
    else:
        size[ru] += size[rv]
        raiz[rv] = ru
        j = prox[rv]
        while j != rv:
            raiz[j] = ru
            j=prox[j]
        prox[ru],prox[rv] = prox[rv],prox[ru]
  
def KRUSKAL (A,n):
    Et = []
    cost = 0
    QUICK(A,0,len(A)-1)
    MAKE_SETS(n)
    k = 0
    while k < len(A) and len(Et) < (n - 1):
        u,v = A[k][0],A[k][1]
        if FIND_SET(u) != FIND_SET(v):
            Et.append((u,v))
            cost += A[k][2]
            UNION(u,v)
        k += 1
    return Et, cost

#A = [(0,7,18),(3,6,17),(3,7,16),(0,4,15),(1,4,14),(1,7,13),(2,3,12),(1,5,11),(1,6,10),(1,2,9),(2,6,8),(2,5,7),(0,3,6),(0,1,5),(6,7,4),(4,5,3),(5,6,2),(4,7,1)]
#n = 8
#A = [(7,9,74),(8,0,273),(4,8,424),(9,0,166),(3,7,230),(0,2,304),(0,3,100),(8,6,336),(7,6,13),(7,0,134),(1,7,173),(3,6,486),(5,8,92),(4,7,2),(3,8,445),(6,0,404),(2,6,50),(4,1,354),(7,8,229),(5,3,366)]
#n = 10 #20 arestas
#A = [(7,49,74),(8,30,273),(44,28,424),(9,40,166),(3,27,230),(40,12,304),(19,9,158),(10,33,100),(28,16,336),(47,26,13),(17,10,134),(29,49,80),(21,17,173),(43,36,486),(45,28,92),(44,7,2),(3,8,445),(18,40,125),(46,30,404),(22,16,50),(24,1,354),(27,8,229),(33,48,482),(35,13,366),(14,13,37),(25,19,116),(44,29,2),(17,45,106),(4,1,299),(38,23,6),(32,2,67),(16,37,439),(44,1,398),(21,28,138),(44,4,110),(31,45,176),(35,48,143),(49,18,413),(10,7,95),(8,45,469),(13,30,7),(12,42,366),(21,45,213),(21,1,91),(31,38,58),(16,40,141),(29,35,7),(22,48,96),(19,4,224),(39,10,406),(26,23,7),(13,20,239),(44,20,345),(16,34,227),(44,13,239),(44,40,51),(9,23,448),(35,17,273),(39,47,386),(46,35,124),(35,15,126),(34,42,12),(29,2,245),(45,18,397),(42,15,492),(33,19,398),(3,47,326),(10,12,212),(25,35,369),(45,26,268),(39,24,332),(6,1,373),(10,44,485),(5,39,408),(15,43,270),(30,5,356),(6,13,3),(26,8,250),(31,44,139),(8,47,152),(49,3,232),(31,14,420),(25,9,181),(29,23,55),(10,37,46),(17,25,201),(6,14,98),(48,4,51),(0,26,413),(4,47,5),(31,48,66),(28,49,210),(29,3,484),(47,7,274),(22,5,177),(3,24,131),(16,0,445),(20,35,17),(48,5,134),(7,26,179),(16,7,212),(28,14,320),(37,33,92),(20,12,134),(47,31,89),(39,23,378),(4,8,201),(4,10,416),(47,30,231),(5,46,108),(38,0,427),(35,7,114),(14,43,361),(4,18,358),(13,2,418),(43,19,468),(47,19,396),(3,23,104),(9,6,431),(24,32,474),(0,31,481),(3,0,21),(33,8,4),(30,29,333),(24,49,43),(49,21,311),(29,33,471),(40,23,151),(21,29,319),(46,49,231),(21,26,125),(44,8,197),(21,14,61),(48,1,441),(3,1,302),(20,25,13),(33,38,118),(8,0,325),(45,7,12),(43,3,66),(10,42,404),(2,7,142),(10,0,300),(27,21,288),(14,25,142),(17,48,343),(15,24,446),(23,20,412),(39,4,306),(16,6,305),(10,48,93),(20,16,81),(17,2,440),(16,41,172),(45,20,241),(0,11,64),(44,33,228),(27,45,32),(42,16,7),(47,11,104),(24,8,437),(31,15,211),(16,5,474),(31,20,292),(19,15,328),(36,28,126),(34,17,450),(26,46,77),(16,17,21),(34,41,211),(8,11,245),(18,14,326),(18,28,30),(34,27,241),(4,40,397),(35,33,49),(15,11,253),(14,26,238),(25,45,211),(47,37,300),(47,15,194),(29,1,26),(39,8,34),(0,39,171),(17,46,39),(43,38,437),(21,19,497),(47,38,360),(37,35,236),(12,34,490),(26,11,326),(19,31,404),(4,3,180),(15,41,108),(4,6,451),(3,32,33),(41,4,478),(17,0,290),(29,17,17),(48,12,30)]
#n = 50 #200 arestas
#A = [(7,49,74),(58,30,273),(44,78,424),(9,40,166),(92,42,488),(3,27,230),(40,12,304),(69,9,158),(60,33,100),(78,16,336),(97,26,13),(67,10,134),(79,49,80),(21,67,173),(93,36,486),(45,28,92),(94,57,2),(53,8,445),(68,90,125),(96,30,404),(22,66,50),(24,1,354),(77,8,229),(33,98,482),(35,13,366),(14,63,37),(25,69,116),(94,29,2),(17,95,106),(4,51,299),(88,23,6),(82,52,67),(16,37,439),(44,1,398),(71,28,138),(58,77,398),(94,4,110),(31,45,176),(35,98,143),(99,68,413),(60,57,95),(8,95,469),(13,30,7),(62,42,366),(21,95,213),(71,1,91),(31,38,58),(16,90,141),(79,35,7),(72,98,96),(19,54,224),(89,60,406),(26,23,7),(13,70,239),(94,20,345),(66,34,227),(94,63,239),(44,90,51),(59,23,448),(85,17,273),(39,47,386),(96,85,124),(20,44,469),(35,15,126),(34,42,12),(79,52,245),(95,18,397),(92,15,492),(33,69,398),(53,47,326),(10,62,212),(25,35,369),(95,76,268),(39,74,332),(56,1,373),(60,94,485),(55,89,408),(15,93,270),(80,55,356),(6,63,3),(76,8,250),(31,44,139),(8,97,152),(49,3,232),(31,14,420),(75,9,181),(29,23,55),(60,37,46),(17,25,201),(56,64,98),(48,4,51),(50,76,413),(54,97,5),(81,48,66),(78,99,210),(29,53,484),(47,7,274),(22,5,177),(53,24,131),(66,0,445),(70,85,17),(98,55,134),(57,76,179),(66,57,212),(78,14,320),(37,33,92),(20,62,134),(97,31,89),(89,73,378),(4,58,201),(54,60,416),(47,80,231),(55,46,108),(38,0,427),(35,57,114),(14,93,361),(54,18,358),(85,29,16),(63,2,418),(43,19,468),(47,69,396),(3,73,104),(48,85,159),(59,6,431),(24,32,474),(3,97,421),(50,31,481),(3,0,21),(33,58,4),(80,79,333),(74,49,43),(49,71,311),(79,83,471),(40,23,151),(71,29,319),(46,99,231),(21,76,125),(44,58,197),(71,64,61),(98,51,441),(3,51,302),(5,80,419),(20,25,13),(83,88,118),(8,50,325),(95,57,12),(90,66,411),(93,53,66),(60,42,404),(52,7,142),(10,0,300),(27,71,288),(14,25,142),(17,48,343),(15,74,446),(73,20,412),(39,54,306),(66,56,305),(60,98,93),(20,16,81),(67,52,440),(98,1,312),(16,91,172),(45,20,241),(58,53,128),(50,11,64),(94,33,228),(27,95,32),(42,16,7),(15,24,102),(97,61,104),(24,8,437),(81,15,211),(16,5,474),(81,20,292),(69,65,328),(36,28,126),(84,67,450),(76,46,77),(66,67,21),(84,91,211),(58,11,245),(25,67,190),(18,14,326),(18,28,30),(34,27,241),(54,40,397),(35,83,49),(65,11,253),(64,76,238),(75,45,211),(47,37,300),(47,15,194),(79,29,165),(79,1,26),(89,58,34),(0,89,171),(17,46,39),(43,38,437),(21,19,497),(47,88,360),(87,35,236),(12,84,490),(84,34,168),(19,15,46),(76,61,326),(19,31,404),(4,3,180),(65,91,108),(24,65,122),(54,6,451),(3,32,33),(41,54,478),(17,0,290),(65,47,123),(79,17,17),(48,62,30),(39,8,404),(57,61,253),(66,21,58),(96,55,431),(94,55,222),(12,93,428),(32,44,292),(98,52,357),(70,3,440),(14,99,267),(35,21,44),(52,86,220),(50,10,124),(69,5,444),(11,31,493),(16,99,472),(39,70,337),(91,57,334),(28,77,411),(83,76,490),(91,34,212),(4,26,392),(90,22,365),(90,84,314),(41,27,180),(84,37,371),(61,81,166),(2,32,333),(54,59,348),(77,62,11),(19,50,378),(41,36,221),(99,12,260),(56,90,153),(48,14,45),(18,50,102),(1,45,462),(57,10,429),(5,73,138),(69,96,4),(21,75,19),(54,63,144),(89,50,236),(15,64,495),(63,58,153),(92,16,215),(20,60,451),(68,41,348),(96,87,2),(34,28,72),(48,75,254),(19,71,321),(64,79,131),(10,80,114),(42,38,383),(44,28,394),(75,80,1),(96,47,371),(87,43,234),(52,61,325),(0,80,279),(57,23,499),(14,45,163),(9,10,350),(18,90,56),(43,55,386),(34,75,322),(51,26,252),(59,83,215),(37,79,199),(0,37,286),(78,84,343),(15,60,68),(40,7,67),(28,62,364),(69,90,124),(78,13,262),(10,40,479),(0,94,8),(56,51,287),(76,84,253),(8,14,455),(19,28,172),(70,63,448),(24,43,355),(8,81,53),(88,63,360),(19,79,357),(61,87,354),(99,88,245),(80,66,284),(74,36,410),(67,34,440),(84,51,50),(89,27,274),(81,95,437),(74,35,232),(72,28,299),(70,87,298),(89,46,91),(11,12,464),(12,81,452),(30,21,214),(28,50,101),(94,30,133),(59,77,280),(32,72,384),(81,53,123),(21,56,319),(91,0,197),(20,4,100),(29,44,176),(70,16,100),(80,18,289),(52,28,301),(62,40,150),(85,83,16),(59,78,460),(61,82,49),(70,28,252),(44,69,96),(69,10,173),(23,25,220),(46,69,171),(94,10,393),(64,24,362),(19,20,63),(61,25,435),(49,90,323),(60,93,429),(22,81,367),(68,23,223),(39,17,294),(64,78,457),(71,41,356),(36,89,229),(20,2,313),(16,47,447),(51,72,312),(23,36,106),(7,33,367),(53,12,426),(40,53,258),(33,95,140),(51,58,195),(60,38,430),(75,98,293),(33,62,277),(36,46,374),(64,84,193),(19,42,329),(59,62,146),(16,27,173),(48,0,371),(98,92,46),(28,0,144),(92,63,284),(72,1,10),(21,86,14),(69,31,358),(19,86,357),(16,54,255),(14,15,38),(66,97,378),(60,12,192),(31,74,464),(77,24,285),(33,50,28),(99,29,110),(44,64,452),(12,79,135),(7,83,101),(59,10,254),(91,21,226),(53,61,359),(91,63,421),(68,87,27),(72,19,142),(45,70,475),(62,76,318),(26,13,345),(71,79,36),(29,88,349)]
#n = 100 #400 arestas
A = [(7,49,74),(58,30,273),(44,78,424),(9,40,166),(92,42,488),(3,27,230),(40,12,304),(69,9,158),(60,33,100),(78,16,336),(97,26,13),(67,10,134),(79,49,80),(21,67,173),(93,36,486),(45,28,92),(94,57,2),(53,8,445),(68,90,125),(96,30,404),(22,66,50),(24,1,354),(77,8,229),(33,98,482),(35,13,366),(14,63,37),(25,69,116),(94,29,2),(17,95,106),(4,51,299),(88,23,6),(82,52,67),(16,37,439),(44,1,398),(71,28,138),(58,77,398),(94,4,110),(31,45,176),(35,98,143),(99,68,413),(60,57,95),(8,95,469),(13,30,7),(62,42,366),(21,95,213),(71,1,91),(31,38,58),(16,90,141),(79,35,7),(72,98,96),(19,54,224),(89,60,406),(26,23,7),(13,70,239),(94,20,345),(66,34,227),(94,63,239),(44,90,51),(59,23,448),(85,17,273),(39,47,386),(96,85,124),(20,44,469),(35,15,126),(34,42,12),(79,52,245),(95,18,397),(92,15,492),(33,69,398),(53,47,326),(10,62,212),(25,35,369),(95,76,268),(39,74,332),(56,1,373),(60,94,485),(55,89,408),(15,93,270),(80,55,356),(6,63,3),(76,8,250),(31,44,139),(8,97,152),(49,3,232),(31,14,420),(75,9,181),(29,23,55),(60,37,46),(17,25,201),(56,64,98),(48,4,51),(50,76,413),(54,97,5),(81,48,66),(78,99,210),(29,53,484),(47,7,274),(22,5,177),(53,24,131),(66,0,445),(70,85,17),(98,55,134),(57,76,179),(66,57,212),(78,14,320),(37,33,92),(20,62,134),(97,31,89),(89,73,378),(4,58,201),(54,60,416),(47,80,231),(55,46,108),(38,0,427),(35,57,114),(14,93,361),(54,18,358),(85,29,16),(63,2,418),(43,19,468),(47,69,396),(3,73,104),(48,85,159),(59,6,431),(24,32,474),(3,97,421),(50,31,481),(3,0,21),(33,58,4),(80,79,333),(74,49,43),(49,71,311),(79,83,471),(40,23,151),(71,29,319),(46,99,231),(21,76,125),(44,58,197),(71,64,61),(98,51,441),(3,51,302),(5,80,419),(20,25,13),(83,88,118),(8,50,325),(95,57,12),(90,66,411),(93,53,66),(60,42,404),(52,7,142),(10,0,300),(27,71,288),(14,25,142),(17,48,343),(15,74,446),(73,20,412),(39,54,306),(66,56,305),(60,98,93),(20,16,81),(67,52,440),(98,1,312),(16,91,172),(45,20,241),(58,53,128),(50,11,64),(94,33,228),(27,95,32),(42,16,7),(15,24,102),(97,61,104),(24,8,437),(81,15,211),(16,5,474),(81,20,292),(69,65,328),(36,28,126),(84,67,450),(76,46,77),(66,67,21),(84,91,211),(58,11,245),(25,67,190),(18,14,326),(18,28,30),(34,27,241),(54,40,397),(35,83,49),(65,11,253),(64,76,238),(75,45,211),(47,37,300),(47,15,194),(79,29,165),(79,1,26),(89,58,34),(0,89,171),(17,46,39),(43,38,437),(21,19,497),(47,88,360),(87,35,236),(12,84,490),(84,34,168),(19,15,46),(76,61,326),(19,31,404),(4,3,180),(65,91,108),(24,65,122),(54,6,451),(3,32,33),(41,54,478),(17,0,290),(65,47,123),(79,17,17),(48,62,30),(39,8,404),(57,61,253),(66,21,58),(96,55,431),(94,55,222),(12,93,428),(32,44,292),(98,52,357),(70,3,440),(14,99,267),(35,21,44),(52,86,220),(50,10,124),(69,5,444),(11,31,493),(16,99,472),(39,70,337),(91,57,334),(28,77,411),(83,76,490),(91,34,212),(4,26,392),(90,22,365),(90,84,314),(41,27,180),(84,37,371),(61,81,166),(2,32,333),(54,59,348),(77,62,11),(19,50,378),(41,36,221),(99,12,260),(56,90,153),(48,14,45),(18,50,102),(1,45,462),(57,10,429),(5,73,138),(69,96,4),(21,75,19),(54,63,144),(89,50,236),(15,64,495),(63,58,153),(92,16,215),(20,60,451),(68,41,348),(96,87,2),(34,28,72),(48,75,254),(19,71,321),(64,79,131),(10,80,114),(42,38,383),(44,28,394),(75,80,1),(96,47,371),(87,43,234),(52,61,325),(0,80,279),(57,23,499),(14,45,163),(9,10,350),(18,90,56),(43,55,386),(34,75,322),(51,26,252),(59,83,215),(37,79,199),(0,37,286),(78,84,343),(15,60,68),(40,7,67),(28,62,364),(69,90,124),(78,13,262),(10,40,479),(0,94,8),(56,51,287),(76,84,253),(8,14,455),(19,28,172),(70,63,448),(24,43,355),(8,81,53),(88,63,360),(19,79,357),(61,87,354),(99,88,245),(80,66,284),(74,36,410),(67,34,440),(84,51,50),(89,27,274),(81,95,437),(74,35,232),(72,28,299),(70,87,298),(89,46,91),(11,12,464),(12,81,452),(30,21,214),(28,50,101),(94,30,133),(59,77,280),(32,72,384),(81,53,123),(21,56,319),(91,0,197),(20,4,100),(29,44,176),(70,16,100),(80,18,289),(52,28,301),(62,40,150),(85,83,16),(59,78,460),(61,82,49),(70,28,252),(44,69,96),(69,10,173),(23,25,220),(46,69,171),(94,10,393),(64,24,362),(19,20,63),(61,25,435),(49,90,323),(60,93,429),(22,81,367),(68,23,223),(39,17,294),(64,78,457),(71,41,356),(36,89,229),(20,2,313),(16,47,447),(51,72,312),(23,36,106),(7,33,367),(53,12,426),(40,53,258),(33,95,140),(51,58,195),(60,38,430),(75,98,293),(33,62,277),(36,46,374),(64,84,193),(19,42,329),(59,62,146),(16,27,173),(48,0,371),(98,92,46),(28,0,144),(92,63,284),(72,1,10),(21,86,14),(69,31,358),(19,86,357),(16,54,255),(14,15,38),(66,97,378),(60,12,192),(31,74,464),(77,24,285),(33,50,28),(99,29,110),(44,64,452),(12,79,135),(7,83,101),(59,10,254),(91,21,226),(53,61,359),(91,63,421),(68,87,27),(72,19,142),(45,70,475),(62,76,318),(26,13,345),(71,79,36),(29,88,349),(78,17,224),(38,8,430),(26,68,307),(99,55,330),(76,88,397),(19,64,138),(16,18,492),(83,98,121),(48,61,152),(18,77,447),(61,78,229),(63,35,7),(8,68,180),(19,23,178),(92,53,479),(53,95,272),(75,4,463),(32,19,32),(35,68,469),(10,34,271),(78,65,46),(79,75,328),(87,63,38),(75,84,56),(56,99,165),(93,86,134),(24,47,195),(30,67,166),(10,82,306),(14,52,242),(85,91,307),(3,30,86),(0,85,468),(84,88,201),(86,0,496),(99,2,429),(83,17,137),(2,89,79),(25,89,223),(95,5,320),(14,62,207),(83,26,420),(1,30,145),(75,58,463),(31,36,221),(8,11,398),(0,14,397),(99,45,34),(62,39,255),(93,35,489),(71,38,322),(91,13,61),(57,92,244),(75,68,414),(15,36,392),(79,6,55),(7,37,204),(21,47,35),(49,16,260),(38,50,184),(86,96,186),(24,22,364),(2,95,37),(54,8,481),(31,30,96),(14,12,137),(37,9,186),(19,81,111),(8,9,440),(67,19,267),(99,20,16),(77,22,143),(80,81,386),(30,25,437),(94,45,103),(33,80,457),(34,17,382),(81,58,306),(92,60,152),(1,42,445),(35,55,373),(43,22,14),(41,81,280),(18,60,230),(55,82,365),(32,13,196),(28,4,356),(11,81,111),(61,64,406),(22,13,444),(36,18,495),(88,43,140),(2,43,71),(19,12,318),(32,82,98),(59,73,91),(19,10,412),(15,78,43),(8,83,100),(9,13,51)]
n = 100 #500 arestas
raiz = [0]*n
prox = [0]*n
size = [0]*n
tree, cost = KRUSKAL(A,n)
print("A árvore gerador é formada pelas arestas: ",tree)
print("O custo dessa árvore é ", cost)

