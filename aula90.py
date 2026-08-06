# Empacotamento e desempacotamento de dicionarios
# a, b = 1, 2
# a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# a, b = pessoa.values()
# print(a, b)   

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)


# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 15,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}

#print(pessoa_completa)
print()


# args e Kwargs
# args (já vimos)
# kwargs - keyboard arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)
    print()

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome='Joana', qlq=123)

#mostro_argumentos_nomeados(**pessoa_completa)


configuracoes = {
    'args1:' : 1,
    'args2:' : 2,
    'args3:' : 3,
    'args4:' : 4,
}

mostro_argumentos_nomeados(**configuracoes)


print()