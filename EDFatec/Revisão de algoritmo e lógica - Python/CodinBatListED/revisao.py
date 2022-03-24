#faça uma fução fatorial, que dado um inteiro n 
#positivo calcle n! = 1*2*3*...*n
#Ex.: fat(4) = 24

def fat(n):
  cont = 1 
  f = 1 
  while cont <= n:
    f = f * cont
    cont = cont + 1 
  return f
print (fat(4))