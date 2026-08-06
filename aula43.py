"""
iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# texto = iter('Luiz') # ___iter___()

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

# for letra in texto
texto = 'Luiz' # iteravel
# iteratador = iter(texto) # iterator

# while True:
#    try:
#         letra = next(iteratador)
#         print(letra)
#    except StopIteration:
#        break 

for letra in texto:
    print(letra)