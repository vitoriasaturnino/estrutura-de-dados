Algoritmos de ordenação

quero procurar uma palavra num texto
Existem várias formas de fazer isso:
1) Busca sequencial, comparo letra por letra até encontrar a posição correta
se a frase tem n letras e a palavra tem m letras 
no pior caso vou gastar m * n comparações

podemos usar o dado para fazer um algoritmo melhor. A frase não sei qual será mas já sei qual palavra estou procurando. Sabendo que  da palavra que estou procurando, nesse caso "algoritmo" posso percorrer om passos mais largos, posso buscar ao contrário, por exemplo:
sabendo de todas as letras pertencem a palavra posso continuar o pular a verificação de alguma palavra.
é muito inteligente, consigo dar pulos maiores se sei usar a oalavra posso gerar um vetor de pulos para aumentar os meus passos
1- para toda letra que não faz parte da palavra posso pular len(palavra)
2- quando a letra faz parte, pelo meos irei dar pulos maiores que um 
[ALGORITMO DE BOYERMOORE]()

[EP2](/EP2)

1) sequencial, que tem n * m passos xxxxxxxxxxxxxxxxxx@xxxxx
Supondo que faça a comparação de trás paa frente, então evou descobrir que não é a mesma palavra deoius de m comparações, e como tenho n caracteres, o total é n * m

2) a melhor forma é usar o DADO que temos, ou seja, a palavra que estou buscando, no caso "algoritmo" os alggoritmos de ordenação
algoritmo 
876043210 ta bela de "pulos", quando tenho letra repetida pego o menor valor, todo caractere que não faz parte da palavra, permite um "pulão" do tamanho da palavra. Esse algoritmo é chamado de BoyerMoore 

Repare que o pior caso continua com n * m comparações, exemplo do xxxx... , mas na prática ele é muito prático, por dois motios:
1) a maior parte dos caracteres não az parte da palavra, que implica pulo grandes 
2) mesmo que faça parte sempre ganho pulos

Esse problema nã serve só para buscar no texto, serve para ver sequencias de DNA no seu sequenciamento total, ou procurar assinatura de virus na memória ou no seu HD interno

mudando de assunto

Existem algoritms muito ruins, mas que são usados, principamente, porque não há outra alternativa. Existem problemas, chamados NP difíceis, que não possuem solução rápida, então faremos aprozimações, ou usamos FORÇA BRUTA.

Por que se chamam força bruta? Porque testam TODAS as posiilidades, e para isso preciso saber todas as pocibilidalidades, e para isso preciso saber gerar todas as entrdas

Existem dois grandes grpos de algoritmos de força bruta, que testam todos os subconjuntos, ou todas as permutações.

A pessoa recebeu vários cheques, e no final do mês deu negativo. Quais ps cheques que provavlmente não tinham fundo? Subconjuntos.

exercíio programadores ep2 

arvore binaria é igual a busca binária em termos de busca, log de n 2 passos, porém paa inserir ou remover no final é muito melhor pois uso ponteiros, e ainda tenho uma estrutura de dados ordenada, já que os números maiores ficam sempre armazenados a esquerda e os menores a direita.


uma ávore binária é composta por nós e arcos, cada nó pode ser ligado a no máximo dois outros nós, os que estão a esquerda tem valor menor e os da direita valor maior em comparação ao seu nó pai
um nó pode ter 0, 1 ou no máximo 2 filhos e os nós sem filhos são chamados de folhas
o pimeiro nó é chamado de nó raiz

A ávore binária é definida de forma recursiva, já que um nó root com dois filhos por sua vez, representam uma árvore binária que segue a mesma definiação. Cada nó pode ter seu filho da esquerda e da direita com um nó que pode originar duas novas árvores essa definião é valida recursivamente por toda a árvore

Para calcular o número máximo de nós que uma árvore pode possuir devemos olhar seus níveis, pois em cada nível se tem o dobro de nós do nível anterior

Como fazer iserção de elementos em uma árvore binária?
É preciso verificar se há um nó raiz:
    a - Caso não haja o primeiro elemento a ser inserido se tornará a raiz da árvore
    b - Caso a raiz já exista é preciso verificar se o elemento a ser inserido é maior ou menor que ela.
        1 - Se o elemento for menor que a raiz deve ser inserido a esquerda
        2 -Se for menor, deve ser inserido a sua direita

Aqui, mais uma vez podemos notar a recursividade, essa regra se repete em sucessão até que seja enontrda alguma árvore que não possua raiz

Como deletar um elemento de um árvore binária?
Regras para remoção de um nó:
Caso 1 - O nó não tem filhos, nesse caso basta apenas deleta-lo sem consequencias
Caso 2 - O nó possui apenas um único filho, devemos remover o pai e colocar o filho em seu lugar, possivelmente movendo também uma subárvore da qual esse nó é a raiz
Caso 3 - O nó que deve ser deletado possui dois filhos, nesse caso temos duas opções:
    a - Substitui-lo pelo maior número da subárvore da esquerda 
    b - Subistituilo pelo menor número da subárvore da direita
Depois dessa substituição é preciso remover o nó escolhido do lugar original e movelo para sua nova posição, dessa forma caímos de volta no caso 1 ou 2.









