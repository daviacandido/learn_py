# Generator Expression, Iterables e Iterators em Python

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)

for i in iterator:
    print(i)

# Aqui irá retornar erro pois o iterator já chegou ao final
# do iterable:
# print(next(iterator))
