lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
print(lista)

print()
print()


lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista)


print()
print()


lista = [
    [x for y in range(3)]
    for x in range(3)
]
print(lista)

print()
print()


lista = [
    [(x,letra) for letra in 'Luiz']
    for x in range(3)
]
print(lista)

print()
print()