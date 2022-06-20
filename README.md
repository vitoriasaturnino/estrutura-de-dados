## **Ponteiros e Listas Encadeadas**

### Coteúdos: Passagem de valor por referencia, Alocação diamica de um vetor com o tamanho definido em tempo de execução.

#

> Info.: Um valor do tipo int ocupa 4 bites enquano um valor do tipo char ocupa somente um.
> & = endereço na memória

Uma função básicas na linguagem C de ponteiros é:
1- Passagem de variáveis por referência.
Ex.: Se eu tenho uma variável local e eu quero que a função altere tenho que passar o ponteiro da variável Scanf();

regras:

1- Ponteiro e coisa pontada são duas coisas diferentes.
ex.:

```
//váriável
int k;
//ponteiro
int*p;
//ponteiro recebe o endereço de valor da váiável
p = &k;
```

2- Não deve se usar um ponteiro que não aponta para nada.

3- Vetores em C tem dados contíguos (um do dado do ladinho do outro), isso é bom para mover massas de dados, por exemplo a vantagem em termos de velocidade em games ou computação gráfica quando quero mover muitos dados mais rapidamente; porém, para remover ou inserir alguém no início é muito ineficiente já que, tería que empurar todos os outros elementos para a esquerda, mas para resolver esse problemas temos as listas encadeadas, para inserir ou remover no inicio.

```
//13 7 -2 22 10 11 4 77
//inserir 42 no início

int v[100] = {13, 7, -2, 22, 10, 11, 4, 77};
for (i = 0; i < 8; i++){
  v[i+1] = v[i];
}
i[0] = 42;
```

Então como eu posso inserir 42 rapidamente em C no alto nível? Usando ponteiros! Pense no exemplo de caça ao tesouro, uma pista/ponta leva a outra. Com poteiros eu vou implementar uma estrutura de dados chamada Lista Encadeada ou Lista Ligada.

```
atruct cel {
int conteudo;
struct cel *seg; // seguinte
}
typedef struct cel celula;

celula a;
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

Em C posso alocar memória sem declarar variável, usando a função (**malloc** = memory allocator).
Essa função vai devolver um ponteiro até acabar a memória, quando ela acaba ele devole **NULL**.

Programar em C tem muitos detahes para mehorar a eficiencia, porque C é baixo nível.

O ato de inserir elementos na lista deve ser no ínicio, pois ter que andar até
até o final da lista torna o processo ineficiente.
É conveniente ter uma CABEÇA de lisa, que nada mais é que tratar a primeira célula da lista encadeada como um marcador de início e ignorar o conteúdo da célula. Assim podemos eviar:
1- Testar de listas vazias;
2- Não preciso usar ponteio para ponteiros, porque se a lista estiver com NULL no começo, ao inserir o primero precisarei alterar o ponteiro, como o ponteiro é variável local, preciso passar o endereço dele para função insere, e dentro da função insere terei um ponteiro para ponteiro.

Ex.: [Lista ligada cira lista sem cabeça](/EDFatec/Códigos%20em%20C/Lista%20Ligada%20cria%20lista%20sem%20cabeça.c) e [Lista ligada cria lista com cabeça](/EDFatec/Códigos%20em%20C/Lista%20Ligada%20cria%20lista%20com%20cabeça.c).

Na lista [Códigos em C](EDFatec/C%C3%B3digos%20em%20C/) vimos também muitos detalhes; um éxemplo é que como não temos indices como estamos acostmadas, precisamos devolver um ponteiro.

Concatena: preciso percorrer até o final paa achar a "liga".
Libera : que eu preciso salvar o seguinte, antes de liberar a list para a memória.
Vetor para lista: preciso percorrer o vetor de trás para frente, porque se quero criar uma lista encadeada
como ele insere no inicio, para ficar igual preciso percorrer ao contrario
Ex.: minha lista é = lista[3, 5, 10], para implementar em uma lista encadeada, nesta ordem, devo começar inserindo o último elemento, já que as inserções são feitas no fim da lista.

> !DESAFIOS
> Inverte e Josephus (vídeo no YT)

> Estudar pela [Lista de exercícios](</EDFatec/Lista%20de%20Exercícios%20Listas%20Encadeadas%20ED%202011-01%20(1).pdf>)

Sobre o código lista ligada sem cabeça:

1. Se eu sacrificar uma cabeça que equivale a 8 bites, meu código fica muito mais eiciente sem a pergunta de lista vazia.
2. Se o começo da lista lst(variavel local) está com NULL na primeira inserção preciso alterar se eu passar &lst dentro de um insere vai ficar \*\*p. (???)

### 14/03

[Slides apartir do slide 58](/EDFatec/SLIDES-A-handout.pdf)

## **Filas** = FIFO = Fist In First Out.

O primeiro que entra é o primeiro que sai. Estrutura bastante usada pra jogos. Implementação:

```
fila = []
fila.append(novo)  #enfilera
x = fila.pop(0)    #tira da fila
```

Qual é melhor, dcionário ou matriz?
DEPENDE, caso eu precise saber os vizinhos dicionário é mas rápido, caso queira saber os que estão ligados posso usar matriz.

> Em C int \*\*A pode significar que é um ponteiro para um ponteiro ou uma matriz.

### 15/03

Grafo = nós e arestas.

- Matriz = bom para saber se está ligado, porém, gasta muito espaço e não é a melhor opção para pegar todos os vizinhos.
- Dicionário = bom para pegar todos os vizinhos, gasta pouco esaço, porém é ruim para ver apenas se está ligado.

## **Pilha** = LIFO = Last In First Out. Implementação:

```
p=[] #criando pilha
p.append(x) #para acrescentar
p.pop() para #remover elemento
```

[Algoritmo do binário](/EDFatec/dec2binED.py)

#

**Busca em um vetor ordenado**

vetor[2, 5, 9, 12, 13, 13, 18, 21, 34, 41, 42, 54, 55, 58]

1- busca sequêncial (ver de um em um). Pior caso = está no final ou não existe, pois terei que percorrer todos os elementos.

2- Poso fazer algo melhor utilizando o dado, isto é, já que o vetor esta em ordem.
Uma lista telefonica tem os nomes em ordem alfabétida, se você precisa achar um nome que começa com F não tem necessidade de procurar nas outras letras.

## BUSCA BINÁRIA

Funciona como se o vetor fosse dividido ao meio, a partir daí vejo para qual lado ir, e em cada passo descarto metade da possibilidades. Essa é a ideia do ìndice de BD

O algoritmo de busca biária é como a invenção da roda no mundo da programação.

**Problema:** Quero transformar uma folha de papel em 128 retangulos. Qual a forma mais fácil de se fazer isso?

**1-** Ana vai desenhar um por um.

**2-** Masa dobra o papel no meio, dobra novamente e assim sussesivamente, na 7 dobra ele já terá 128 retangulos!

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

## **📌 Dividindo o mundo em dois!**

O computador escolhe um número aleatório entre 1 e 100.
Toda vez que você chutar um número ele vai dizer alto ou baixo. Qual número você chuta primeiro?
A resposta é o número 50, pois diminui o número de possilidades pela metade!  
Se computador disser alto, chuto 25 para descartar metade dos números.  
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

**Conclusão:** sempre consigo chegar a meta em `log(n,2)` passos, quanto maior o número mais rápido posso chegar ao resultado.

🟡 Vai cair na prova [Algoritmo de Busca Binária](/EDFatec/busca_binaria.py) e [Adivinha um número entre 1 e 100](/EDFatec/Advinhando%20um%20número%20entre%201%20e%20100.py)

#

## Existem duas duas formas de buscar um elemento em um vetor ordenado:

**1- Busca sequêncial**  
 No pior caso vou demorar o tamanho do vetor, pois o número pode estar na última posião ou não estar armazenado no vetor.

**2- Busca binária**  
No pior caso vou demorar `log(n,2)`. Dessa forma é muito mais rápida, porque eu usei um dado que tenho! O Vetor ordenado.

Então podemos concluir que, vale a pena ordenar!  
O mais interessante é que para ordenar um vetor existem algoritmos muito rápidos, e a maioría deles usa a mesma idéia de busca binaria.

Vamos ver algoritmos de ordenação: 2 ruins e 3 bancos.

- Algoritmos ruins: [inserção](/EDFatec/AlgoritmoasBonsERuins/inserção.py) e [seleção](/EDFatec/AlgoritmoasBonsERuins/seleção.py)
- Aloritmos bons: [mergesort](/EDFatec/AlgoritmoasBonsERuins/mergesort.py), [quicksort](/EDFatec/AlgoritmoasBonsERuins/quicksort.py) e [heapsort](/EDFatec/AlgoritmoasBonsERuins/heapsort.py).

## Inserção

Percorrer os dados da esquerda para direita e enfiar no lado esquerdo ordenando

### Exemplo: Algoritmo do baralho.

Vetor_Inicial = [0, 2, 4, 7, 3, 5, 6, 1]

<-- A partir daí vou verificando, da esquerda para a direita se o número é o mais baixo, se sim, deio ele na posição que está, caso encontre um número mais alto e um menor na seguencia "troco" esses dois de lugar -->

0 2 4 7 3 5 6 1 - 0 ok  
0 2 4 7 3 5 6 1 - 2 ok  
0 2 4 7 3 5 6 1 - 4 ok  
0 2 4 7 3 5 6 1 - 7 ok  
0 2 3 4 7 5 6 1 - 3 epurra o 4 e o 7  
0 2 3 4 5 7 6 1 - 5 emurra o 7  
0 2 3 4 5 6 7 1 - 6 empurra o 7  
0 1 2 3 4 5 6 7 - 1 empurra 2, 3, 4, 5, 6 e o 7

Nesse caso números grandes são bons e os pequenos muito ruins, pois tenho que ficar empurrando os maiores até que o vetor esteja ordenado e sse proceso de organização demora muito.

### Fazer o mesmo processo **sozinha** para o seguinte vetor = [3, 5, 6, 7, 4, 2, 0, 1]

3 5 6 7 4 2 0 1 - 3 ok  
3 5 6 7 4 2 0 1 - 5 ok  
3 5 6 7 4 2 0 1 - 6 ok  
3 5 6 7 4 2 0 1 - 7 ok  
3 4 5 6 7 2 0 1 - 4 epurra 5 6 e o 7  
2 3 4 5 6 7 0 1 - 2 empurra 3 4 5 6 7  
0 2 3 4 5 6 7 1 - 0 empurra 2 3 4 5 6 7  
0 1 2 3 4 5 6 7 - 1 empurra 2 3 4 5 6 7

**Conclusão:** Vou gastar n passos para percorrer da esquerda para dirita.
No pior caso, o número é muito pequeno e eu tenho que empurrar todos os outros.  
Então no pior caso n \* n = n ** 2, como tenho também casos bons, na prática, vou demorar menos que n**2.

Algoritmo do exemplo acima [inserção](/EDFatec/AlgoritmoasBonsERuins/inserção.py)

#

## Seleção

Vou percorrer todo mundo da esquerda para a direita e procurar a menor posição de onde estou pra frente.

Vetor_Inicial = [0, 2, 4, 7, 3, 5, 6, 1]

<-- Caso o vetor omeçe com o menor número na primeira posição ainda assim devo fazer a troca, dele por ele mesmo. Assim que ordear o número vou para o próximo e o comparo com seus seguintes, se houver algum número menor devo troca-los de posição -->

0 2 4 7 3 5 6 1 - troco 0 com 0  
0 2 4 7 3 5 6 1 - troco 2 com 1  
0 1 2 7 3 5 6 4 - troco 2 com 4  
0 1 2 3 7 5 6 4 - troco 3 com 7  
0 1 2 3 4 5 6 7 - troco 4 com 7  
0 1 2 3 4 5 6 7 - troco 5 com 5  
0 1 2 3 4 5 6 7 - troco 6 com 6  
0 1 2 3 4 5 6 7 - troco 7 com 7

### Repetindo o processo **sozinha** para o seguinte vetor = [3, 5, 6, 7, 4, 2, 0, 1]

3 5 6 7 4 2 0 1 - troco 3 pelo 0
0 5 6 7 4 2 3 1 - troco 5 pelo 1
0 1 6 7 4 2 3 5 - troco 6 pelo 2
0 1 2 7 4 6 3 5 - troco 7 pelo 3
0 1 2 3 4 6 7 5 - troco 4 pelo 4
0 1 2 3 4 5 7 6 - troco 5 pelo 6
0 1 2 3 4 5 6 7 - troco 6 com 7
0 1 2 3 4 5 6 7 - troco 7 com 7

**Conclusão:** Gasto n passos para percorrer todos e sempre gasto mais n passos para achar o menor, no total gasto n\*n - n \*\* 2, n para descorir todos e n para descobri o min.

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
[3, 5, 7, 6] [0, 2, 4, 1] - divide o vetor em 2  
[3, 5] [7, 6] [0, 2] [4, 1] - divide o vetor em 4  
[3] [5] [7] [6] [0] [2] [4] [1] - divide o vetor em 8

então, separo em quatro vetores de 2 posições cada um inicio a comparação

[3, 5] [6, 7] [0, 2] [1, 4] - tenho 4 vetores de duas posiçõs ordenado  
[3, 5, 6, 7] [0, 1, 2, 4] - 2 vetores de 4 posições ordenados
comparo do primeiro para o último (0<3 1<3 2<3 3<4 5>4 6>7 )

Por fim, tenho o vetor ordenado [0, 1, 2, 3, 4, 5, 6, 7]

### **Duas fases:**

**1-** dividir o vetor até que ele tenha apenas 1 posição, `log(n, 2)`  
**2-** juntar os partes dobrando e ordenando, `log(n, 2)`

**Custo total:** log(n, 2) \* n  
**1-** processo em duas fases log(n, 2)
**2-** percorrer todos para juntar n passos

### Repetindo o processo para o seguinte vetor = [0, 1, 6, 7, 5, 3, 4, 2]

[0, 1, 6, 7, 5, 3, 4, 2] - 1 vetor de 8 posições  
[0, 1, 6, 7] [5, 3, 4, 2] - 2 vetores de 4 posições  
[0, 1] [6, 7] [5, 3] [4, 2] - 4 vetores de 2 posições  
[0] [1] [6] [7] [5] [3] [4] [2] - 8 vetores de 1 posição  
[0, 1] [6, 7] [3, 5] [2, 4] - faço as comparações trazedo os parzinhos do vetor anerior de volta  
[0, 1, 6, 7] [2, 3, 4, 5] - junto mais uma vez ordeno
Faço as últimas comparações (0<1 1<2 2<6 3<6 4<6 5<6 6<7)  
Vetor ordenado = [0, 1, 2, 3, 4, 5, 6, 7]

**Mergesort** tem muitas coisas interessantes.  
**1-** Cada metade é independente, por isso posso fazer os processos em paralelo.
**2-** porém tenho um ponto falho, no merge eu tenho que usar uma lista auxiliar r e como não removo ninguém do lado esquerdo ou direito, vou recisar do dobro de espaço!

Muito importante Quando analisar um código, não olhar apenas o número de passos, mas também o espaço ocupado.

[ALgoritmo do exemplo acima](/EDFatec/AlgoritmoasBonsERuins/mergesort.py)

#

## Quicksort

📌Exemplo:
Pego um voluntário na sala e divido em menores e maiores que ele,
vou repetindo o processo em cada metade, então o número de voluntários(pivô) na posição definitiva vai dobrando a cada passo em log(n, 2) todos estarão ordenados.

**Custo total:** n \* log(n, 2), n passos para todos se compararem com o pivô log(n, 2) e ficarem todos na posição correta.

**Conclusão**
Quicksort é tão rápido quanto o mergesort mas tem a vantagem de não gastar o dobro de espaço, enquanto mergesort só dobra o número de posições ordenadas, quicksort soma com os anteriores 1 + 2 + 4 + 8 + 16 + ... +

[ALgoritmo do exemplo acima - Quicksort](/EDFatec/AlgoritmoasBonsERuins/quicksort.py)

**Heapsort** Usa estruturas internas que andam na lista com passos que vão dobrando a cada vez, ou seja, ando nos índies muito mais rápido.
O mais rápido é o sort interno do Python, que é híbrido, se chama TIM sort.

<!-- Comentários para estudar para a prova:
1- Mergesort pode ser executada em paralelo, as duas metades sendo indepedendentes, podem ser executadas em paralelo. Preciso de um vetor auxiliar para unir as duas metades, logo preciso do dobro de espaço. (mergesort recursigo é menor que o interaativo, em questão de espaço)

2- Quicksort - O pior caso do quicksort é um vetor ja ordenado, porque a cada passo não vai ningué para o lado dos menores, entáo vou demorar n passos para terminar, e como todos precisam se comarar com o pivô o custo total é de n*n = n **2, isso torna meu algoritmo tão ruim quanto o inserção e seleção.
Porque isso é interessante? na prática é extremamente raro encontrar um vetor já ordenado para ser ordenado novamente . Mais ainda o número de pessoas na posição correta é acumulativo: 1 + 2 + 4 + 8 + 16 + 32 + ... + Não apenas dobra, mas acumula os anteriores
__Conclusão:__ Não basta ver o pior caso, é muito mais interessante ver o caso médio.
Por últimmo, para ver a eficiencia não basta testar somente para números pequenos, é sempre bom testar para números altos

Algoritmos de ordenação

quero procurar uma palavra num texto
Existem várias formas de fazer isso:

1. Busca sequêncial, comparo letra por letra até encontrar a posição correta se a frase tem n letras e a palavra tem m letras no pior caso vou gastar m \* n comparações

podemos usar o dado para fazer um algoritmo melhor. A frase não sei qual será mas já sei qual palavra estou procurando. Sabendo que da palavra que estou procurando, nesse caso "algoritmo" posso percorrer om passos mais largos, posso buscar ao contrário, por exemplo:
sabendo de todas as letras pertencem a palavra posso continuar o pular a verificação de alguma palavra.
é muito inteligente, consigo dar pulos maiores se sei usar a oalavra posso gerar um vetor de pulos para aumentar os meus passos
1- para toda letra que não faz parte da palavra posso pular len(palavra)
2- quando a letra faz parte, pelo meos irei dar pulos maiores que um
[ALGORITMO DE BOYERMOORE]()

[EP2](/EP2)

1. sequêncial, que tem n _ m passos xxxxxxxxxxxxxxxxxx@xxxxx
   Supondo que faça a comparação de trás paa frente, então evou descobrir que não é a mesma palavra deoius de m comparações, e como tenho n caracteres, o total é n _ m

2. a melhor forma é usar o DADO que temos, ou seja, a palavra que estou buscando, no caso "algoritmo" os alggoritmos de ordenação
   algoritmo
   876043210 ta bela de "pulos", quando tenho letra repetida pego o menor valor, todo caractere que não faz parte da palavra, permite um "pulão" do tamanho da palavra. Esse algoritmo é chamado de BoyerMoore

Repare que o pior caso continua com n \* m comparações, exemplo do xxxx... , mas na prática ele é muito prático, por dois motios:

1. a maior parte dos caracteres não az parte da palavra, que implica pulo grandes
2. mesmo que faça parte sempre ganho pulos

Esse problema nã serve só para buscar no texto, serve para ver sequências de DNA no seu sequênciamento total, ou procurar assinatura de virus na memória ou no seu HD interno

-->

=================================================================================================

#

# Algoritmos de Enumeração

Enumerar é listar todas as possibilidades.
Existem algoritmos muito ruins, mas que são usados, principamente, porque não há outra alternativa. Existem problemas, chamados NP difíceis, que não possuem solução rápida, então fazemos aproximações ou usamos algoritmos de **força bruta** também chamados de **backtracking**. Esses algoritmos são aqueles que testam todas as posilidades.

Existem dois grandes grupos de algoritmos de força bruta, que testam todos os subconjuntos que é 2^ n-1 passos, ou todas as permutações que é n! passos.

## Exemplo de como calcular todos os subconjuntos de n

> **Dica:** Ler a sequência da esquerda pra direita
> <---------------------------------------

```
Para Montar os Sub conjuntos é mais fácil se lermos a sequência ao contrário, devemos montar cada sub conjunto até chegar a n, assim que estivermos no número máximo podemos remove-lo, somar +1 no seu antecessor e continuar montando subconjuntos até atingir novamente o valor de n e então repetir o processo (recursividade) até que só reste o valor de n como subconjunto

Exemplo 1: n = 4

começo enumerando todas as possibilidades até chegar em n

1
12
123
1234

quando chegar em n (4),tiro o último e incremento + 1 em seu anterior (3) (3+1=4)

124
13
134
14
2
23
234
24
3
34
cheguei no meu n (4)

temos um total de 14 sunconjuntos para n=4
```

```
Exemplo 2: n = 3

1
12
123
13
2
23
cheguei no meu n (3)

sete subconjuntos de n = 3
```

## Exemplo de como calcular todas permutações de n

para fazer permutações osso fixar os primeiros números e ir realizando as permutações de dois em dois até atingir o resultado de n!

```
Exemplo 1: n = 3

Fixando o número 1
123
132

Fixando o número 2
213
231

Fixando o número 3
312
321

tenho 6 premutações para n = 3, que é o mesmo que n!
```

```
Exemplo 1: n = 4

Fixando o número 1 e 2
1234
1243

Fixando o número 1 e 3
1324
1342

Fixando o número 1 e 4
1432
1423

Fixando o número 2 e 1
2134
2143

Fixando o número 2 e 3
2314
2341

Fixando o número 2 e 4
2413
2431

Fixando o número 3 e 1
3124
3142

Fixando o número 3 e 2
3241
3214

Fixando o número 3 e 4
3412
3421

Fixando o número 4 e 1
4123
4132

Fixando o número 4 e 2
4231
4213

Fixando o número 4 e 3
4312
4321

tenho 24 premutações para n = 4, que é o mesmo que n!
```

## Para Treinar subconjuntos e permutações:

[Exercício EP2 - Arthur Merlin Games](./EDFatec/EP2/ep2.py)

#

# Ávore Binária

Árvore binaria funciona da mesma forma que a busca binária em termos de busca, o resultado pode ser encotrado em log n2 passos, porém para inserir ou remover no final é muito melhor pois uso ponteiros, e ainda tenho uma estrutura de dados ordenada, já que os números maiores ficam sempre armazenados a esquerda e os menores a direita.

Uma ávore binária é composta por nós e arcos, cada nó pode ser ligado a no máximo dois outros nós, os que estão a esquerda tem valor menor e os da direita valor maior em comparação ao seu nó pai um nó pode ter 0, 1 ou no máximo 2 filhos e os nós sem filhos são chamados de folhas o pimeiro nó da árvore é denominado nó raiz.

Uma ávore binária é definida de forma recursiva, já que um nó root com dois filhos por sua vez, representam uma árvore binária que segue a mesma definiação. Cada nó pode ter seu filho da esquerda e da direita com um nó que pode originar duas novas árvores, esta definião é valida recursivamente por toda a árvore.

Para calcular o número máximo de nós que uma árvore pode possuir devemos olhar seus níveis, pois em cada nível se tem o dobro de nós do nível anterior

### Como fazer iserção de elementos em uma árvore binária?

É preciso verificar se há um nó raiz:

**1.** Caso não haja o primeiro elemento a ser inserido se tornará a raiz da árvore;  
**2.** Caso a raiz já exista é preciso verificar se o elemento a ser inserido é maior ou menor que ela:

- **a)** Se o elemento for menor que a raiz deve ser inserido a esquerda
- **b)** Se for maior, deve ser inserido a sua direita

Aqui, mais uma vez podemos notar a recursividade, essa regra se repete em sucessão até que seja encontrda alguma árvore que não possua raiz

### Como deletar um elemento de um árvore binária?

Regras para remoção de um nó:

**1.** Caso o nó não tem filhos, nesse caso basta apenas deleta-lo sem consequências;  
**2.** Caso o nó possui apenas um único filho, devemos remover o pai e colocar o filho em seu lugar, possivelmente movendo também uma subárvore da qual esse nó é a raiz;  
**3.** Caso o nó que deve ser deletado possui dois filhos, nesse caso temos duas opções:

- **a)** Substitui-lo pelo maior número da subárvore da esquerda;
- **b)** Subistituilo pelo menor número da subárvore da direita. Depois dessa substituição é preciso remover o nó escolhido do lugar original e movelo para sua nova posição, dessa forma caímos de volta no caso 1 ou 2.

### Pior caso de busca em uma árvore binária

É quando tenho uma árvore desbalanciada com um dos galhos muito maior que o outro, já que desta forma não estaria jogando fora metada das minhas possibilidades na hora de realizar uma busca, isso tornaria meu algoritmo muito ruim.  
Para resolver isso podemos remover elementos no meio da árvore,para torna-la mais balanceada.

### Aplicação

Índices de busca em bancos de dados.

#

# Teoria dos Grafos

Um Grafo tem dois tipos de objetos, um conjunto de vértices e um conjunto de arestas. O que define um grafo são seus vértices e arestas, de forma que não há problema se existirem vértices isolados (que não fazem parte de uma aresta).  
O conjunto de **arestas** de um grafo é denotado por **"E"** e o conjunto de **vertices** é denotado por **"V"**.  
Arestas são um par não ordenados de vértices, ou seja, não importa a direção.

Aqui vamos estudar somente **grafos simples** que são aqueles que não possuem arestas "paralelas", ou seja, não podem ter das arestas diferentes com o mesmo par de pontas. Além disso as duas pontas de qualquer aresta são diferentes, desta forma não há laços.

O complementar de um grafo é definido pela letra G com uma barra em cima. Um grafico G barra tem os mesmos vértices, no entanto, onde tem arestas no original não tem no complementar e onde não tinha passa a ter. Um grafo completo também se ele tem todas as arestas ligadas.

<h2>Grafo do cavalo 3x3</h2>

<div align="center">
  <img width=400px src="./EDFatec/teoria_dos_grados/cavalo_3x3.jpg">
</di>

<h2>Grafo do cavalo 3x3 Planar</h2>

<div align="center">
  <img width=400px src="./EDFatec/teoria_dos_grados/cavalo_3x3_planar.jpg">
</di>

<h2>Grafo do Cubo Q3</h2>

<div align="center">
  <img width=400px src="./EDFatec/teoria_dos_grados/cubo_Q3.jpg">
</di>

<h2>Grafo do Cubo Q3 Planar</h2>

<div align="center">
  <img width=400px src="./EDFatec/teoria_dos_grados/cubo_Q3_planar.jpg">
</di>

## Importante 📌

Os dois grafos ilustrados acima tem propriedades raras, por isso são usados como entrada de algoritmos para validação.  
Note que com a forma planar dos dois grafos resolvemos problemas apresentados anteriormente:

- **Ciricuito Hamiltoniano**  
  Com a sequência 3 A 2 D 1 C 4 B do grafo **Cavalo 3x3** e a sequência 000 010 011 111 110 100 101 001 do grafo **Cubo Q3** temos uma possível solução para a disposição dos cavaleiros ao redor da mesa da Távola Redonda.

- **Emparelhamento Máximo**  
  Casando | A3 | B4 | C2 | D1 | do grafo do **Cavalo 3x3** e | 000 casa com 001 | 010 casa com 011 | 100 casa com 101 | 111 casa com 110 | do grafo **Cubo Q3** eu obtenho o emparelhamento máximo casando todos os vértices, resolvendo assim o problema do casamento das damas da corte.
