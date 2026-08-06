"""
Flag(Bandeira) - Marcar um local
None - não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""

condição = True
Passou_no_if = None

if condição:
      Passou_no_if = True
      print('faça algo')
else:
      print('não faça algo')

if Passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
