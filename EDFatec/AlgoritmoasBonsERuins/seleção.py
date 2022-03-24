def seleção(v):
  r = []
  while v:
    m = min(v) 
    r.append(m)
    v.remove(m)
  return r

from time import time
from random import shuffle
v = list(range(20000))
shuffle(v)
t1 = time()
seleção(v)
t2 = time()
print (t2-t1)

