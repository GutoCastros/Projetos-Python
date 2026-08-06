"""
https://docs.python.org/pt-br/3/libary/stdtypes.html
Imutaveis que vimos: str, int, float, bool
"""
string = 'luis Otávio'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
#string[3] = 'ABC'

print(string)
print(outra_variavel)
print(string.capitalize())
print(string.zfill(10))