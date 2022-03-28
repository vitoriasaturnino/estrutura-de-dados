## __Ponteiros e Listas Encadeadas__

### Coteúdos: Passaem de valor por referencia, Alocação diamica de um vetor com o tamanho definido em tempo de execução.

#

> Info.: Um valor do tipo int ocupa 4 bites enquano um valor do tipo char ocupa somente um.
>& = endereço na memória

Uma função básicas na linguagem C de ponteiros é:
  1- Passagem de variáveis por referência.
  Ex.: Se eu tenho uma variável local e eu quero que a função altere tenho que passar o ponteiro da variável Scanf();

regras: 

1- Ponteiro e coisa pontada são duas coisas diferentes. (int k; int*p; p = &k;)

2- Não deve se usar um ponteiro que não aponta para nada.

3- Vetores em C tem dados contíguos (um do dado do ladinho do outro), isso é bom para mover massas de dados, por exemplo a vantagem em termos de velocidade em games ou computação gráfica quando quero mover muitos dados mais rapidamente.
porém para remover ou inserir alguém no início é muito ineficiente jé que, tería que empurar todos os outros elementos para a esquerda, mas para resolver esse problemas temos as listas encadeadas, para inserir ou remover no inicio.

```
//13 7 -2 22 10 11 4 77 
//inserir 42 no início

int v[100] = {13, 7, -2, 22, 10, 11, 4, 77};
for (k=0; k < 8; k++){
  v[k+1] = v[k];
}
v[0] = 42;
```
Então como eu posso inserir 42 rapidamente em C no alto nível? Usando ponteiros! Pense no exemplo de caça ao tesouro, uma pista/ponta leva a outra. Com poteiros eu vou implementar uma estrutura de dados chamada Lista Encadeada ou Lista Ligada.

```
atruct cel {
int conteudo;
struct cel *seg; // seguinte
}
typedef struct cel celula;

celula a ;
celula *p;
p = &a;
a.conteudo = 42;
(*p).conteudo = 42;
```
Quando eu pego um ponteiro e coloco um * na frente estou acessando a coisa apontada.
Em C, pra não escrever (*p). Se preferiu a seguinte sintaxe p->

```
(*p).seg //é o mesmo que 
p->seg
```

[Ex.:código da lista = lista ligada com cabeça e sem aloação dinamica](/EDFatec/Códigos%20em%20C/Lista%20Ligada%20com%20cabeça%20sem%20alocação%20dinâmica.c)

Em C posso alocar memória sem declarar variável, usando a função (__malloc__ = memory allocator).
Essa função vai devolver um ponteiro até acabar a memória, quando ela acaba ele devole __NULL__. 

Programar em C tem muitos detahes para mehorar a eficiencia, porque C é baixo nível.

O ato de inserir elementos na lista deve ser no ínicio, pois ter que andar até 
até o final da lista torna o processo ineficiente.
É conveniente ter uma CABEÇA  de lisa, que nada mais é que tratar a primeira célula da lista encadeada como um marcador de início e ignorar o conteúdo da célula. Assim podemos eviar que;
1- Evita testes de listas vazias;
2- Não preciso usar ponteio para ponteiros, porque se a lista estiver com NULL no começo, ao inserir o primero precisarei alterar  o ponteiro cmo o ponteiro é variável local, preciso passar o endereço dele para função insere, e dentro da função insere terei um ponteiro para ponteiro.

Ex.: [Lista ligada cira lista sem cabeça](/EDFatec/Códigos%20em%20C/Lista%20Ligada%20cria%20lista%20sem%20cabeça.c) e [Lista ligada cria lista com cabeça](/EDFatec/Códigos%20em%20C/Lista%20Ligada%20cria%20lista%20com%20cabeça.c).

Na lista [Códigos em C](EDFatec/C%C3%B3digos%20em%20C/) vimos também muitos detalhes; um éxemplo é que como não temos indices como estamos acostmadas, precisamos devolver um ponteiro.

Concatena: preciso percorrer até o final paa achar a "liga".
Libera : que eu preciso salvar o seguinte, antes de liberar a list para a memória.
Vetor para lista: preciso percorrer o vetor de trás para frente, porque se quero criar uma lista encadeada
como ele insere no inicio, para ficar igual preciso percorrer ao contrario
Ex.: minha lista é = lista[3, 5, 10], para implementar em uma lista encadeada, nesta ordem, devo começar inserindo o último elemento, já que as inserções são feitas no fim da lista. 

>!DESAFIOS
>Inverte e Josephus (vídeo no YT)

>Estudar pela [Lista de exercícios](/EDFatec/Lista%20de%20Exercícios%20Listas%20Encadeadas%20ED%202011-01%20(1).pdf)

Sobre o código lista ligada sem cabeça:
1) Se eu sacrificar uma cabeça que equivale a 8 bites, meu código fica muito mais eiciente sem a pergunta de lista vazia.
2) Se o começo da lista lst(variavel local) está com NULL na primeira inserção preciso alterar se eu passar &lst dentro de um insere vai ficar **p. (???)

### 14/03

[Slides apartir do slide 58](/EDFatec/SLIDES-A-handout.pdf)

## __Filas__ = FIFO = Fist In First Out.

O primeiro que entra é o primeiro que sai. Estrutura bastante usada pra jogos. Implementação:
```
fila = []
fila.append(novo)  #enfilera
x = fila.pop(0)    #tira da fila
```

Qual é melhor, dcionário ou matriz?
DEPENDE, caso eu precise saber os vizinhos dicionário é mas rápido, caso queira saber os que estão ligados posso usar matriz.

> Em C int **A pode significar que é um ponteiro para um ponteiro ou uma matriz.

### 15/03

Grafo =  nós e arestas.
- Matriz = bom para saber se está ligado, porém, gasta muito espaço e não é a melhor opção para pegar todos os vizinhos.
- Dicionário = bom para pegar todos os vizinhos, gasta pouco esaço, porém é ruim para ver apenas se está ligado.

## __Pilha__ = LIFO = Last In First Out. Implementação: 

```
p=[] #criando pilha
p.append(x) #para acrescentar
p.pop() para #remover elemento
```
[Algoritmo do binário](/EDFatec/dec2binED.py)

#

__Busca em um vetor ordenado__

vetor[2, 5, 9, 12, 13, 13, 18, 21, 34, 41, 42, 54, 55, 58]

1- busca sequencial (ver de um em um). Pior caso = está no final ou não existe, pois terei que percorrer todos os elementos.

2- Poso fazer algo melhor utilizando o dado, isto é, já que o vetor esta em ordem.
Uma lista telefonica tem os nomes em ordem alfabétida, se você precisa achar um nome que começa com F não tem necessidade de procurar nas outras letras.

## BUSCA BINÁRIA 
Funciona como se o vetor fosse dividido ao meio, a partir daí vejo para qual lado ir, e em cada passo descarto metade da possibilidades. Essa é a ideia do ìndice de BD

O algoritmo de busca biária é como a invenção da roda no mundo da programação.

__Problema:__ Quero transformar uma folha de papel em 128 retangulos. Qual a forma mais fácil de se fazer isso?

__1-__ Ana vai desenhar um por um.

__2-__ Masa dobra o papel no meio, dobra novamente e assim sussesivamente, na 7 dobra ele já terá 128 retangulos!

Busca binária vale muito a pena para valores grandes.
A ideia é simples, dividir o mundo em 2, porém a implementaçã demorou 17 anos.

[Código de busca binária](/EDFatec/buscaBinaria.py)

Exemplo do prof.:
```
cont = 0
def busca_binaria(x, v):
global cont
eduardo = -1  #-1 limite esquerdo
damares = len(v)  #len(v) limite esquerdo

while eduardo < damares-1:  #quando eduardo == d-1 siqnifica que estão lado a lado
  m = (eduardo + damares) // 2 
  cont = cont + 1
  if v[m] < x:
    eduardo = m
  else:
    damares = m
return d

v = list(range(1000000))
from random import randint
print (busca_binaria(randint(1, 1000000), v))
print (cont)

```

Ex.: Vamos deduzir o numero de passos do aloritmo de busca binária
 ```
 from math import log
n = 1000000
log(n, 2)
19.931568569324174
n = 2 * n
log(n, 2)
20.931568569324174
n = 1000000000
log(n, 2)
29.897352853986263
 ```

  Pergunta: Na vida você encontra facilmente vetor ordenado? Não, mas vale a pena ordenar!

21/03/2022

# Algoritmo de Busca Binária

## __📌 Dividindo o mundo em dois!__

O computador escolhe um número aleatório entre 1 e 100.
Toda vez que você chutar um número ele vai dizer alto ou baixo. Qual número você chuta primeiro? 
A resposta é o número 50, pois diminui o número de possilidades pela metade!  
Se  computador disser alto, chuto 25 para descartar metade dos números.   
Se ele disser alto chuto 12.  
Se o computador disser baixo 18.  
Se o computador disser baixo 21.  
Se o computador disser baixo chuto 23.  
Se o computador disser alto o número é 22.  
CONSIGO RESOLVER PROBLEMAS COM 7 PASSOS.

#

O número pode ser absurdamente grande e você sempre irá acertar em um tempo rasoável. um trilhão leva no máximo 30 chutes
A ídeia é tão boa que pode ser utilizada em diversos algoritmos.

Nos bancos de dados, sempre que crio um índice estou utilizando a ideia de dividir no meio (busca binária).
NOSQL - Bancos não relaconais
MongoDB, Cassandra, Redis, Neo4J.

Machine larning também é da área de estrutura de dados. - (estudar sobre) aprendizagem supervisionada.

__Conclusão:__ sempre consigo chegar a meta em `log(n,2)` passos, quanto maior o número mais rápido posso chegar ao resultado.


🟡 Vai cair na prova [Algoritmo de Busca Binária](/EDFatec/busca_binaria.py) e [Adivinha um número entre 1 e 100](/EDFatec/Advinhando%20um%20número%20entre%201%20e%20100.py)

#

## Existem duas duas formas de buscar um elemento em um vetor ordenado:

__1- Busca sequencial__  
 No pior caso vou demorar o tamanho do vetor, pois o número pode estar na última posião ou não estar armazenado no vetor.

__2- Busca binária__  
No pior caso vou demorar `log(n,2)`. Dessa forma é muito mais rápida, porque eu usei um dado que tenho! O Vetor ordenado. 

Então podemos concluir que, vale a pena ordenar!  
O mais interessante é que para ordenar um vetor existem algoritmos muito rápidos, e a maioría deles usa a mesma idéia de busca binaria.

Vamos ver  algoritmos de ordenação: 2 ruins e 3 bancos.
- Algoritmos ruins: [inserção](/EDFatec/AlgoritmoasBonsERuins/inserção.py) e [seleção](/EDFatec/AlgoritmoasBonsERuins/seleção.py)
- Aloritmos bons: [mergesort](/EDFatec/AlgoritmoasBonsERuins/mergesort.py), [quicksort](/EDFatec/AlgoritmoasBonsERuins/quicksort.py) e [heapsort](/EDFatec/AlgoritmoasBonsERuins/heapsort.py).

## Inserção
Percorrer os dados da esquerda para direita e enfiar no lado esquerdo ordenando

### Exemplo: Algoritmo do baralho.

Vetor_Inicial = [0, 2, 4, 7, 3, 5, 6, 1]  

<-- A partir daí vou verificando, da esquerda para a direita se o número é o mais baixo, se sim, deio ele na posição que está, caso encontre um número mais alto e um menor na seguencia "troco" esses dois de lugar -->

0 2 4 7 3 5 6 1  -  0 ok   
0 2 4 7 3 5 6 1  -  2 ok   
0 2 4 7 3 5 6 1  -  4 ok   
0 2 4 7 3 5 6 1  -  7 ok   
0 2 3 4 7 5 6 1  -  3 epurra o 4 e o 7   
0 2 3 4 5 7 6 1  -  5 emurra o 7    
0 2 3 4 5 6 7 1  -  6 empurra o 7   
0 1 2 3 4 5 6 7  -  1 empurra 2, 3, 4, 5, 6 e o 7  

Nesse caso números grandes são bons e os pequenos muito ruins, pois tenho que ficar empurrando os maiores até que o vetor esteja ordenado e sse proceso de organização demora muito.   

### Fazer o mesmo processo __sozinha__ para o seguinte vetor = [3, 5, 6, 7, 4, 2, 0, 1]

3 5 6 7 4 2 0 1  -  3 ok   
3 5 6 7 4 2 0 1  -  5 ok    
3 5 6 7 4 2 0 1  -  6 ok   
3 5 6 7 4 2 0 1  -  7 ok   
3 4 5 6 7 2 0 1  -  4 epurra 5 6 e o 7   
2 3 4 5 6 7 0 1  -  2 empurra 3 4 5 6 7   
0 2 3 4 5 6 7 1  -  0 empurra 2 3 4 5 6 7   
0 1 2 3 4 5 6 7  -  1 empurra 2 3 4 5 6 7   

__Conclusão:__ Vou gastar n passos para percorrer da esquerda para dirita.
No pior caso, o número é muito pequeno e eu tenho que empurrar todos os outros.    
Então no pior caso n * n = n ** 2, como tenho também casos bons, na prática, vou demorar menos que n**2.

Algoritmo do exemplo acima [inserção](/EDFatec/AlgoritmoasBonsERuins/inserção.py)

#

## Seleção   
Vou percorrer todo mundo da esquerda para a direita e procurar a menor posição de onde estou pra frente.

Vetor_Inicial = [0, 2, 4, 7, 3, 5, 6, 1]  

<-- Caso o vetor omeçe com o menor número na primeira posição ainda assim devo fazer a troca, dele por ele mesmo. Assim que ordear o número vou para o próximo e o comparo com seus seguintes, se houver algum número menor devo troca-los de posição -->

0 2 4 7 3 5 6 1  -  troco 0 com 0   
0 2 4 7 3 5 6 1  -  troco 2 com 1    
0 1 2 7 3 5 6 4  -  troco 2 com 4    
0 1 2 3 7 5 6 4  -  troco 3 com 7   
0 1 2 3 4 5 6 7  -  troco 4 com 7    
0 1 2 3 4 5 6 7  -  troco 5 com 5   
0 1 2 3 4 5 6 7  -  troco 6 com 6    
0 1 2 3 4 5 6 7  -  troco 7 com 7

### Repetindo o processo __sozinha__ para o seguinte vetor = [3, 5, 6, 7, 4, 2, 0, 1]

3 5 6 7 4 2 0 1  -  troco 3 pelo 0
0 5 6 7 4 2 3 1  -  troco 5 pelo 1
0 1 6 7 4 2 3 5  -  troco 6 pelo 2
0 1 2 7 4 6 3 5  -  troco 7 pelo 3
0 1 2 3 4 6 7 5  -  troco 4 pelo 4 
0 1 2 3 4 5 7 6  -  troco 5 pelo 6
0 1 2 3 4 5 6 7  -  troco 6 com 7
0 1 2 3 4 5 6 7  -  troco 7 com 7

__Conclusão:__ Gasto n passos para percorrer todos e sempre gasto mais n passos para achar o menor, no total gasto n*n - n ** 2, n para descorir todos e n para descobri o min.

[ALgoritmo do exemplo acima](/EDFatec/AlgoritmoasBonsERuins/seleção.py) 
- O `min()` que aparce no código é uma função do Python. (min com maconha kkkkkk)

📌Perguta:   
Não deveria demorar mais que o inserção? 
A solução usa `min()` que é muito mais rápida que n passos pois é uma função embutida do Python que quarda os menores para construir a lista (também existe a função max() que qurda os maiores).

SEMPRE QUE ANALISAR UM CÓDIGO PARA OTIMIIZAR O RPOCESSO LEMBRAR DE PROCURAR ALGUMA LIB OU FUNÇÂO QUE FAÇÃO O QUE VOCÊ EESTÁ FAZENDO! 

# 

## Mergesort

### dividir para conquistar! Programação dinamica

Vetor_Iniial = [3, 5, 7, 6, 0, 2, 4, 1]  
[3, 5, 7, 6]  [0, 2, 4, 1]  -  divide o vetor em 2  
[3, 5]  [7, 6]  [0, 2]  [4, 1]  -  divide o vetor em 4   
[3]  [5]  [7]  [6]  [0]  [2]  [4]  [1] -  divide o vetor em 8  

então, separo em quatro vetores de 2 posições cada um inicio a comparação   

[3, 5]  [6, 7]  [0, 2]  [1, 4]  -  tenho 4 vetores de duas posiçõs ordenado  
[3, 5, 6, 7]  [0, 1, 2, 4]  -  2 vetores de 4 posições ordenados
comparo do primeiro para o último (0<3 1<3 2<3 3<4 5>4 6>7   )

Por fim, tenho o vetor ordenado  [0, 1, 2, 3, 4, 5, 6, 7]   

### __Duas fases:__ 
__1-__ dividir o vetor até que ele tenha apenas 1 posição, `log(n, 2)`   
__2-__ juntar os partes dobrando e ordenando, `log(n, 2)` 

__Custo total:__ log(n, 2) * n  
__1-__ processo em duas fases log(n, 2)
__2-__ percorrer todos para juntar n passos

### Repetindo o processo para o seguinte vetor = [0, 1, 6, 7, 5, 3, 4, 2]

[0, 1, 6, 7, 5, 3, 4, 2]  -  1 vetor de 8 posições  
[0, 1, 6, 7]  [5, 3, 4, 2]  -  2 vetores de 4 posições  
[0, 1]  [6, 7]  [5, 3]  [4, 2]  -  4 vetores de 2 posições  
[0]  [1]  [6]  [7]  [5]  [3]  [4]  [2]  -  8 vetores de 1 posição  
[0, 1]  [6, 7]  [3, 5]  [2, 4]  -  faço as comparações trazedo os parzinhos do vetor anerior de volta  
[0, 1, 6, 7]  [2, 3, 4, 5]  -  junto mais uma vez ordeno
Faço as últimas comparações (0<1 1<2 2<6 3<6 4<6 5<6 6<7)   
Vetor ordenado = [0, 1, 2, 3, 4, 5, 6, 7]          

__Mergesort__ tem muitas coisas interessantes.  
__1-__ Cada metade é independente, por isso posso fazer os processos em paralelo.
__2-__ porém tenho um ponto falho, no merge eu tenho que usar uma lista auxiliar r e como não removo ninguém do lado esquerdo ou direito, vou recisar do dobro de espaço! 

Muito importante Quando analisar um código, não olhar apenas o número de passos, mas também o espaço ocupado.

[ALgoritmo do exemplo acima](/EDFatec/AlgoritmoasBonsERuins/mergesort.py) 

#

## Quicksort

📌Exemplo:
Pego um voluntário na sala e divido em menores e maiores que ele, 
vou repetindo o processo em cada metade, então o número de voluntários(pivô) na posição definitiva vai dobrando a cada passo em log(n, 2) todos estarão ordenados.

__Custo total:__ n * log(n, 2), n passos para todos se compararem com o pivô log(n, 2) e ficarem todos na posição correta.  

__Conclusão__
Quicksort é tão rápido quanto o mergesort mas tem a vantagem de não gastar o dobro de espaço, enquanto mergesort só dobra o número de posições ordenadas, quicksort soma com os anteriores 1 + 2 + 4 + 8 + 16 + ... + 

[ALgoritmo do exemplo acima - Quicksort](/EDFatec/AlgoritmoasBonsERuins/quicksort.py) 

__Heapsort__ Usa estruturas internas que andam na lista com passos que vão dobrando a cada vez, ou seja, ando nos índies muito mais rápido.
O mais rápido é o sort interno do Python, que é híbrido, se chama TIM sort.

<!-- Comentários para estudar para a prova:
1- Mergesort pode ser executada em paralelo, as duas metades sendo indepedendentes, podem ser executadas em paralelo. Preciso de um vetor auxiliar para unir as duas metades, logo preciso do dobro de espaço. (mergesort recursigo é menor que o interaativo, em questão de espaço)

2- Quicksort - O pior caso do quicksort é um vetor ja ordenado, porque a cada passo não vai ningué para o lado dos menores, entáo vou demorar n passos para terminar, e como todos precisam se comarar com o pivô o custo total é de n*n = n **2, isso torna meu algoritmo tão ruim quanto o inserção e seleção.
Porque isso é interessante? na prática é extremamente raro encontrar um vetor já ordenado para ser ordenado novamente . Mais ainda o número de pessoas na posição correta é acumulativo: 1 + 2 + 4 + 8 + 16 + 32 + ... + Não apenas dobra, mas acumula os anteriores
__Conclusão:__ Não basta ver o pior caso, é muito mais interessante ver o caso médio.
Por últimmo, para ver a eficiencia não basta testar somente para números pequenos, é sempre bom testar para números altos
-->
