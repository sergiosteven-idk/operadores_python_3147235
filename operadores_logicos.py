'''
OPERADORES LOGICOS
Los operadores logicos son:
and , or , not
obedecen las tablas de verdad

'''

op1=False
op2=True
op3=False
op4=True

resultado = not op1 and (op2 or op3 and not op1) and not op4
print(resultado)