# metodos em instancias de classes Python
# Classe - Molde (geralmente sem dados)
# Instancia da classe (objeto) - Tem os dados
# Uma classe pode gerar várias instancias
# Na classe o self e a propria instancia.
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando....')
    
string = 'Luiz'
print(string.upper())

fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)
# print(fusca.nome)
# fusca.acelerar()

print()

celta = Carro('Celta')
celta.acelerar()
Carro.acelerar(celta)
# print(celta.nome)
# celta.acelerar()

print()
print()
