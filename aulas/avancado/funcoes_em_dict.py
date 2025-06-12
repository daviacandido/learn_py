# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Davi',
    'sobrenome': 'Cândido',
    # 'idade': 0,
}

# len, keys, values, items e suas funcionalidades:

print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

pessoa.setdefault('idade', 18)

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')


# Diferença entre deep e shallow copy:

d1 = {
    'c1': 1,
    'c2': 2
}

d2 = {
    'c1': 100,
    'c2': 200
}

deep_copy_d1 = d1

print(deep_copy_d1)
d1['c1'] = 10
print(deep_copy_d1)

shallow_copy_d2 = d2.copy()

print(shallow_copy_d2)
d2['c1'] = 10
print(shallow_copy_d2)

# dict.pop() e dict.get()

print('pessoa.pop("idade")')
pessoa.pop('idade')
print(pessoa.get('idade', 'Não existe a chave selecionada'))

# dict.popitem()

print(d2)
print('d2.popitem()')
d2.popitem()
print(d2)

# dict.update()

pessoa.update({
    'nome do meio': 'Araújo',
    'idade': 18
})

# ou

pessoa.update(teste='teste')

# ou

tupla_update = ('chave', 'valor'),
pessoa.update(tupla_update)

print(pessoa)
