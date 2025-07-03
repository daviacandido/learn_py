# Introdução a Generator Funcion em python
# generator functinos conseguem pausar
# ao invés de parar no return

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return


gen = generator()
for n in gen:
    print(n)

# Yield From:


def gen1():
    print('COMEÇOU GEN1')
    yield 1
    yield 2
    yield 3
    yield from gen3()
    print('ACABOU GEN1')


def gen2(gen):
    print('COMEÇOU GEN2')
    yield from gen()
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


def gen3():
    print('COMEÇOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


g = gen2(gen1)
for n in g:
    print(n)
