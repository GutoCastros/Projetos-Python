"""
 Operadores Lógicos
 and (e) or (ou) not (não)
 and - todos as condições precisam ser verdadeiras
 se qualquer valor for considerado false,
 a expressão inteira será avaliada naquele valor
 são considerados false(que vc já viu)
 0 0.0 '' false
 também existe o tipo None que é usado para representar
 um não valor
"""
"""
entrada = input(' [E]ntrar [S]air: ')
senha_digitada = input(' Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print(' Entrar ')
else:
    print(' Sair ')
"""

    
"""

print(True and False and True)
print(True and 0 and True)
print(bool(''))
"""
# Avaliação de curso circuito
senha = input(' Senha: ') or ' Sem senha '
print( senha )
