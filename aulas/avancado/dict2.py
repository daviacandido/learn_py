# Manipulando dicionários:

pessoa = {}

pessoa['nome'] = 'Davi'
print(pessoa['nome'])

chave = 'sobrenome'
pessoa[chave] = 'Cândido'
print(pessoa['sobrenome'])

pessoa[chave] = 'Araujo'

print(pessoa)

del pessoa['sobrenome']

print(pessoa)


if pessoa.get('nome') is None:
    print('Não existe!')
else:
    print(pessoa['nome'])
