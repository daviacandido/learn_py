# introdução a empacotamento + tuplas:

nomes = ['Maria', 'João', 'Luiz']
nome1, nome2, nome3 = nomes

print(f'Lista:{nomes};\nNome 1: {nome1}\nNome 2: {nome2}\nNome 3: {nome3}')

nomes.append('Davi')

_, _, _, davi, *_ = nomes

print(f'Novo nome: {davi}')

# tuplas são listas imutáveis:

novos_nomes = 'Maria', 'João', 'Luiz'
# ou
novos_nomes = tuple(nomes)

print(novos_nomes)
