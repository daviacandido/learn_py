# Enumerate - enumera iteraveis (indices)

lista = ['João', 'Maria', 'José']

lista.append('Helena')

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(f'Indice é {item[0]} com valor "{item[1]}"')
print('---')

# Nesse ponto do código, a lista enumerada já foi "consumida"
# dessa forma, se faz necessário os seguintes contornos se for
# necessário o uso novamente:

nova_lista_enumerada = list(enumerate(lista, start=20))
for item in nova_lista_enumerada:
    print(f'Indice é {item[0]} com valor "{item[1]}"')
print('---')

for indice, nome in enumerate(lista):
    print(indice, nome)
print('---')

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)
print('---')

for item in enumerate(lista):
    for valor in item:
        print(valor)
