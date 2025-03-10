# Operadores en python
'''
Los operados en python
siguen  el siguente orden jerarquico:
1. /,*, % 
2. +,-
3. =
'''
a = 7
b = 3
c = 7
x = 5 
h =1 

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
'''
operciones relacionales:
lasoperaciones atirmeticas
resultan tener un valor numerico:
Las operaciones relacionales
resultan tener un valor booleano:
True False : (V, F, SI NO )
> , < , => , <= , != , ==
JERARQUIA DE OPERACIONES 
(incluyendo los relacionales)
1. ()
2. **
3. *,/,%
4. +, -
5.  > , < , => , <= , != , ==
6. =
'''

y = x + 2 * a - c != b + x * a
print (y)

y = (a * 2 + c /(3 - b )) + 5 <= (3 * a )/ 5 * b
print (y)

y = a ** 2 * 3 /(c - x )
print (y)