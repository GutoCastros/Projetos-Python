"""
Valores padrão para parametros
Ao definir uma função, os parametros pode
ter valores padrão, Caso o valor não seja 
enviado para o parametro, o valor padrão
será usado.
"""

def soma(x, y, z= None):
    if z is not None:
        print(f'{x= }  {y= }  {z= }', x + y + z)
    else:
        print(f'{x= } {y= }', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 8, 0)
soma(x= 7, y= 8, z= 0)


print()
print()