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