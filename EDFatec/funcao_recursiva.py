'''#funções recursivas são aqulas que chamam a si próprias
def fat(n):
    if n<= 1: return 1
    return n * fat(n-1)
#caso mais simples n = 0 ou n = 1 sei que e 1
#caso contrário n! = n*(n-1)!
#faço a repetição sim while ou for, ela acontece no return

def pot(x, n): #pot(2, 3) = 8
    if n == 0: return 1
    return x * pot(x, n-1)
print (por(2, 3))

#Seja a sequenca de FIbonacci 1 1 2 3 5 8 13...
#Caso simples n == 1 or n == 2 sei que é 1 caso
#contrário fib(n) = fib(n-1) + fib(n-2)'''
'''def fib(n):
    print(n)
    if n == 1 or n == 2: return 1
    return fib(n-1) + fib(n-2)
print(fib(10))
#esta sequencia é ruim pois repete o mesmo rocesso várias vezes'''
'''#utilizano dicionário
f = {}
def fib(n):
    #print(n)
    if n == 1 or n == 2: return 1
    if n not in f: fib(n-1) + fib(n-2)
    return f[n]
print(fib(100))'''

#utilizando lib
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n==1 or n==2: return 1
    return  fib(n-1) + fib(n-2)
print (fib(100))
#lru_cache = Less Resuslts Utilized cache
#cache e uma meória do SI onde guardo coisas que uso muito

#@lru_cache é um decorador
#função que nelopa o fib recursio
#dando o "superpoder" de guardar na memória algo á calculado antes


