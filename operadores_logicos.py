'''
OPERADORES LOGICOS
Los operadores logicos son:
and , or , not
obedecen las tablas de verdad

'''
op1 = False
op2 = True
op3 = op1 or op2
print(op3)


# operador NOT
op4 = not op2
print(op4)

'''
JERARQUIA DEFINITIVA DE OPERADORES
            ()
            **
          *,/, %
           +,-
    >, <, !=, ==, <=, >=
            NOT
            AND
            OR
            -
'''