# Manipulando chaves e valores em dicionarios

pessoa = {}

##
##

chave = 'nome'

pessoa['nome'] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])
#print(pessoa['nome1'])

pessoa[chave] = 'Maria'

print(pessoa)

del pessoa['sobrenome']
print(pessoa)

print(pessoa['nome'])


#print(pessoa.get('sobrenome', 'Não existe'))

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE !!!')
else:
    print(pessoa['sobrenome'])

# print('ISSO NÃO VAI')





print()
print()