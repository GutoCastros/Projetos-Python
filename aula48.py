"""
listas em Python
tipo list - Mutavel
Suponha vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos úteis: appendi, insert, pop, del, clean, extend,*
Create, Read, Update, Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#         0   1   2   3 
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
ultimo_valor = lista.pop()
lista.append(60)
lista.append(70)
print(lista)
ultimo_valor = lista.pop(3)
print(lista, 'Removido', ultimo_valor)

