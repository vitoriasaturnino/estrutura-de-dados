# Introdução Estrutura de Dados 
Conhecer e saber qual tipo de estrutura de dados deve ser implementada é dundamental, pois a partir dela podemos 
administrar uma grande quantidade de dados com alta performance no processamneto, usando banco de dados, aerviços de de busca,
indexação de dados e também para a construção de algoritmos eficientes. 
Utilizamos ED para inserir, excluir ou localizar um registro, percorrer todos os registros e clasificar os registros em uma 
ordem pré-determinada.


## Tipos

- __Array__, consiste em armazenar uma coleção de elementos do mesmo tipo, onde cada um desses elementos pode ser identificada
    por pelo menos um índice ou uma chave. O Array é a mais simpres estrutura de dados para armazenamento em memória e praticamente 
    todas as linguagens de programação incluen pelo menos um tipo de dado Array nativamente. O Array também é comnhecido como 
    __Vetor__ que trabalha com estruturas unidimencionais e __Matriz__ que  trabalha com estruturas multidimenionais.


```
    let diasDaSemana = [
        'Segunda-feira',
        'Terça-feira',
        'Quarta-feira',
        'Quinta-feira',
        'Sexta-feira',
        'Sábado',
        'Domingo'
    ];

    let usuarios = [
        ['Clark', 'Kent', 'Planeta Diário'],
        ['Gabriel', 'Fróes', 'Código Fonte'],
        ['Peter', 'Parker', 'Clarin Diário'],
        ['Vanessa', 'Weber', 'Código Fonte']
    ];

    console.log(diasDaSemana[2]); //Quarta-Feira

    console.log(usuários[1],[2]); //Código Fonte

```

- __Pilha__, é uma coleção ordenada de ítens baseada no princípio L.I.F.O (lest in First out), o último elemento adicionado na pilha é o primeniro a sair. EX.: A estrutura de pilha é utilizada com os comandos Crtl+Z e Ctrl+Shift+Z.


```
    class Pilha {

        constructor(){
            this.elementos = [];
        }
        
        //adiciona um elemento a pilha
        push() {
            this.elementos.push(elemento);
        }

        //remove um elemento da pilha
        pop() {
            this.elementos.pop();
        }

    }

    const pilha = new Pilha();

    pilha.push(1); //[1]
    pilha.push(2); //[1,2]
    pilha.push(3); //[1,2,3]
    pilha.push(4); //[1,2,3,4]
    pilha.push(5); //[1,2,3,4,5]

    pilha.pop(); //[1,2,3,4]
    pilha.pop(); //[1,2,3]
    pilha.pop(); //[1,2]
    pilha.pop(); //[1]
    pilha.pop(); //[]

```

- __Fila__, assim como a pilha a fila também é uma coleção ordenada de itens, o que as diferencia é o princípo em que são baseadas, a fila é representada pelo principio F.I.F.O(first in Fist out), o peimwiro a entrar é o primeiro a sair. Igual a uma fila de banco.
A adição de novos elementos é feita no final da fila e é chamada de tale e a remoção é feita no inicio da fila e é chamada de head.

```
class Fila { 

    constructor() {
        this.elementos = [];
    }

    enqueue(elemento) {
        this.elementos.push(elemento);
    }

    dequeue() {
        this.elementos.shift();
    }  

}

const filaDeAtendimento = new Fila();
fila.enqueue('Vitória');
fila.enqueue('Raphael');
fila.enqueue('Neila'); 

fila.dequeue(); //Vitória foi atendida e removida da fila
fila.dequeue(); //Raphael foi atendido e removido da fila
fila.dequeue(); //Neila foi atendido e removida da fila
//fila zerada

```

- __Árvore__ , é uma coleção não ordenada de itens, o modelo abstrato de uma estrutura hieráquica, esse típo de coleção é bastante usado quando queremos encontrar um elemento da forma mais fácil possível.
As Árvores são estruturas de dasdos constítuidas que tem um relacionamento pai e filho, cada nó tem um pai, exeto o que fica no topo da árvore, o que chamamos de raiz, e cada nó pode ter 0 ou mais filhos, ou ramos.
Além da raiz os outros nós se dividem em nós internos e externos, os internos são os que possuem um ou mais filhos, os nós externos que também são chados de folhas são os quais não tem nenhum filho.
Os exemplos de árvore mais conhecidos são os das Árvores Binárias e o da Árvore Binária de Busca, chamada também pela sigla BST(Binary Search Tree). A Árvore binária insere seus nós sem nenhuma regra definida, já a Árvore Binária de Busca inicia a operação inserindo a raiz e o primeiro ná filho, a partir do segundo nó é feita a verificação, se o nó inserido for maior que a raiz ele é armazenado do lado direito, caso contrário é armazenado no lado esquerdo e o mesmo processo se repete para os outros nós.

```
class Arvore { 

    constructor() {
        this.nos = {}
    }

    inserir(arvore, valor) {
        if (arvore.valor) {

            if (valor > arvore.valor) {     
                this.inserir(arvore.direita, valor)

            } else {
                this.inaerir(arvore.esquerda, valor)

            }
            
        } else {
            arvore.valor = valor
            arvore.direita = {}
            arvore.esquerda = {}
        }
        
    }

}

const novaArvore = new Arvore();
novaArvore.inserir(novaArvore.nos, 23);
novaArvore.inserir(novaArvore.nos, 12);
novaArvore.inserir(novaArvore.nos, 4);
novaArvore.inserir(novaArvore.nos, 18);
novaArvore.inserir(novaArvore.nos, 1);
novaArvore.inserir(novaArvore.nos, 27);
novaArvore.inserir(novaArvore.nos, 25);

```

- Dicionários 
- Grafos
- Conjuntos.....





    