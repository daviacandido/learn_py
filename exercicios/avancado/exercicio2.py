# Crie uma função que duplique, triplique e quadriplique
# o número informado.

def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = cria_multiplicador(2)
triplicar = cria_multiplicador(3)
quadriplicar = cria_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))
