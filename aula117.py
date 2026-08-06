# count é um iterador sem fim.
from itertools import count

c1 = count(step=8, start=8)
n1 = range(8, 100, 8)

#print(next(c1))
print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('n1', hasattr(n1, '__iter__'))
print('n1', hasattr(n1, '__next__'))

print()
print()

print('count')
for i in c1:
    if i >= 100:
        break

    print(i)
print()
print('range')
for i in n1:
     print(i)


print()
print()
print()
print()