# lista comum:

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)
# list comprehension é uma forma
# criar lista a partir de iteraveis:

lista = [numero * 2 for numero in range(10)]
print(lista)

# mapeamento em list comprehension:

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 30},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep='\n')
