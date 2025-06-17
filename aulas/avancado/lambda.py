# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

lista = [
    {'id': 5, 'nome': 'Davi', 'sobrenome': 'Candido'},
    {'id': 2, 'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'id': 7, 'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'id': 4, 'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'id': 3, 'nome': 'Aline', 'sobrenome': 'Souza'},
]

lista_ordenada_id = sorted(lista, key=lambda item: item['id'])
lista_ordenada_nome = sorted(lista, key=lambda item: item['nome']) 

def printa_lista(lista):
    for dicionario in lista:
        for chave in dicionario:
            print(f'{chave}: {dicionario[chave]}')
    print()

printa_lista(lista_ordenada_nome)
printa_lista(lista_ordenada_id)