"""
enumerada - enumera iteraveis (indices)
"""
#[(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])


# for tupla_enumerada in enumerate(lista):
#     for valor in tupla_enumerada:
#          print(valor)