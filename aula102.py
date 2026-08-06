# try, except, else e finaly

try:
    print('ABRIR ARQUIVO')
    # 0/0
except ZeroDivisionError:
    print('DIVIDIU POR ZERO')
else:
    print('NÃO DEU ERRO')
finally:
    print('FECHAR ARQUIVO')

print()
print()