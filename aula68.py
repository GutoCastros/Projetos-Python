"""
Argumentos nomeados e não nomeados em funcoes Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
def soma(x, y, z):
    print(x + y + z)
    print(f'x = {x}  y = {y} z ={z}',   '  |', ' x + y  + z= ', x + y + z)



soma(1, 2, 3)
soma(3, 2, 1)

print(1, 2, 3, sep='-')

print()
print()
#print(soma(2, 3))
