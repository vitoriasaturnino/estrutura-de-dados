def BemFormada(s):
  p = []
  for c in s:
    if c == ')': #menina fofa
      if p[-1] == '(': p.pop() #menino fofo
      else: return False
    elif c == '}': #menina pontuda
      if p[-1] == '{': p.pop() #menino pontudo
      else: return False
    else:
      p.append(c)
  return len(p) == 0 # ver se sobra algum encalhado na pilha :(
print (BemFormada('((){()})'))
print (BemFormada('({)}'))
print (BemFormada ('((()))')) #meu exemplo



 
