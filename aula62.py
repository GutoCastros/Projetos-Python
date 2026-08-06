"""
# Desempacotamento em chamadas
# de metodos e funções
"""
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

salas = [
    # 0             1
    ['Maria',   'Helena',  ],  #  0
    # 0 
    ['Elaine', ], # 1
    # 0         1        2
    ['luiz',  'joão',  'Eduarda',  ], # 2
]

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(string)
# print(tupla)

print(*salas, sep='\n')


print()
print()
print()
print()
print()
print()