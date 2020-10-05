//Array a serem usados
vector<int> posi(n);//armazena as posicoes dos vertices no Heap (acesso ao vertice em tempo O(1))
vector<int> dist(n);//vetor de distâncias dos caminhos determinados pelo Dijkstra
vector<int> H;  //Heap: armazena os vértices ordenados pelas distancias (dist)
//================================================================================

template <typename T>
void troca(T &a, T &b){
    T x = a;
    a = b;
    b = x;
}

void Subida(int i){
    //H[(i-1)/2]  é o pai de H[i]
    if(i > 0 && dist[H[i]] < dist[H[(i-1)/2]] ){
        troca(H[i], H[(i-1)/2]);
        troca(posi[H[i]], posi[H[(i-1)/2]]);
        Subida(i/2);
    }
}


void Descida(int i){
    //2i+1  e 2i+2 sao as posicoes dos filhos esquerdo e direito de i
    int n = H.size();
    int min;
    if((2*i+1) < n && dist[H[2*i+1]] < dist[H[i]])
           min = 2*i+1;
    else  min = i;

    if(2*i+2 < n  && dist[H[2*i+2]] < dist[H[min]]) min = 2*i+2;

    if(min != i){
        troca(H[i] , H[min]);
        troca(posi[H[i]] , posi[H[min]]);
        Descida(min);
    }
}

void Insert(int w, int d){
    int n = H.size();
    H.push_back(w);  //insere no final: H[n]= w;
    dist[w] = d;
    posi[w] = n;
    Subida(n);//Subida a partir da ultima posição (arruma o heap)
}

int DeleteMin(){
    int r = H[0];
    int n = H.size();
    H[0] = H[n-1];
    posi[H[n-1]] = 0;
    H.erase (H.begin()+(n-1)); //apaga o ultimo elemento i.e. H[n-1]
    Descida(0); //descida a partir da raiz (posição 0)
    return r;
}

void Decrease(int w){
    Subida(posi[w]);//Subida a partir da posição de w
}

