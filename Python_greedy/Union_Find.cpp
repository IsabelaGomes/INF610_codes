//Arrays a serem usados para na estrutura Union-Find
vector <int> raiz(n); //array de tamanho n, onde n é o número de vértices
vector <int> prox(n); //para fazer o encadeamento da lista
vector <int> size(n); //armazena o tamanho de cada lista

//=========================================================================
template <typename T>
void troca(T &a, T &b){
    T x = a;
    a = b;
    b = x;
}


void Make_Sets(int n){ //cria os n conjuntos
    for(int i = 0; i<n; i++){
        raiz[i] = i;
        prox[i] = i;
        size[i] = 1;
     }
}

int Find_Set(int i){
    return raiz[i];
}

void Union(int u, int v){
//A união é feita se u e v estão em conjuntos diferentes, ou seja se Find_Set(u) != Find_Set(v)

    int ru = raiz[u];
    int rv = raiz[v];
    if(size[ru] < size[rv] ){
        //lista de raiz rv recebe lista de raiz ru:
        size[rv] = size[rv] + size[ru];
        
        //altera a raiz dos elementos da lista de raiz ru:
        raiz[ru] = rv;
        for(int j = prox[ru]; j != ru; j=prox[j])
            raiz[j] = rv;
        
        troca(prox[ru], prox[rv]);
    }
    else{
        //lista de raiz ru recebe lista de raiz rv:
        size[ru] = size[ru] + size[rv];
        
        //altera a raiz dos elementos da lista de raiz rv:
        raiz[rv] = ru;
        for(int j = prox[rv]; j != rv; j = prox[j])
            raiz[j] = ru;
        troca(prox[ru], prox[rv]);
    }
}
