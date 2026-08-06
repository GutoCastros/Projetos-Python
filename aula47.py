"""
listas em Python
tipo list - Mutavel
Suponha vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos úteis: appendi, insert, pop, del, clean, extend,*

"""
#       01234
#      -54321
string = 'ABCDE' # 5 caracteres (len)

#print(lista, type(lista)) # false
#print(lista, type(lista)) 
#print(bool([])) # falsy

#         0    1          2          3   4
#        -5    -4         -3        -2   -1
lista = [123, True, 'Luiz Otavio', 1.2, []] 
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))

