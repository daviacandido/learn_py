import pprint


def p(variavel):
    pprint.pprint(novos_produtos, sort_dicts=False, width=40)


# lista comum:

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

# list comprehension é uma forma
# criar lista a partir de iteraveis:

lista = [numero * 2 for numero in range(10)]
# print(lista)

# mapeamento em list comprehension:

produtos = [
    {'nome': 'arroz', 'preco': 10},
    {'nome': 'feijao', 'preco': 20},
    {'nome': 'carne', 'preco': 30}
]

novos_produtos = [
    # mapeamento:
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    # filtro:
    if produto['preco'] <= 20
]

p(novos_produtos)
