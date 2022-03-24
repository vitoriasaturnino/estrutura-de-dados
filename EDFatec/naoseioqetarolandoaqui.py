
import ast
import codegen
expr='''
def resposta():
   print ('Alô Mundo')
'''
p = ast.parse(expr)
p.body[0].body = \
    [ast.parse('return 42').body[0]]
print(codegen.to_source(p))


#16/03/22 ainda não sei