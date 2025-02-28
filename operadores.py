# Operadores en python
'''
Los operados en python
siguen  el siguente orden jerarquico:
1. /,*, % 
2. +,-
3. =
'''
a = 3
b = 2
c = 1 
x = 5 

y =  a * b + c 
print (y)  #7
'''
Si hay operaciones en el mismo nivel de jerarquia, se resuelven de izquierda a derecha 
'''

y = a * b - 1 / 3 + c

print (y) 

y = a ** 2 - a * b - 1 / 3 + c 
print (y) 

y = a * 2 ** 3 - a + c -c ** 3 + c
print (y) 

'''
NOTA:Si operaciones en el mismo  nivel si hay parentesisentro de parentesis primero en parentesis interno
'''

y = a ** 2 * 3 / (c - x )
print (y) 

y = ((2 * a + c )/ 7) * (a +(4 * a )/ c)
print (y) 