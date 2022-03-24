'''Fazer as funções recursivas a abaixo:'''
#Inverso de um strng s
def inv(s):
    if len(s) == 0: return s
    #return inv(s[1:]) + s[0]
    return s[-1] + inv(s[:-1])
print(s('vitoria'))


#soma dos digitos de um inteiro n
def sd(n):
    if n <= 9: return n
    return n % 10 + sd()
print (sd(123))
    
#mdc de a e b segundo Euclides
''' a  b   a%b
   21 15    6
   15  6    3
   6   3    0 -> mdc(a,b) =  b quando a%b==0 | Caso mais simples'''
def mdc(a, b):
    if a%b == 0: return b
    return(mdc(b, a%b))
print(mdc(21,15))
print(mdc(15, 2))

#DESAFIO cinverter de decimal p binário
def dec2bin(n): 
