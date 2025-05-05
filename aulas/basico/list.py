'''
Listas em Python
Tipo list é mutavel
SUporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
'''

string = 'ABCDE'
print(len(string))

lista1 = []
print(lista1)
print(bool(lista1))

lista2 = [123, 'Davi', True, 1.2, [ 123, 'Davi', 1.2]]

for i in lista2:
    print(i)

print(bool(lista2), lista2[1], type(lista2[2]))
