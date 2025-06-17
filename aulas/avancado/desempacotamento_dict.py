pessoa = {
    'Nome': 'Davi',
    'Sobrenome': 'Cândido'
}

dados_pessoa = {
    'Altura': 1.69,
    'Peso': 99
}

# para desempacotar, podemos fazer da seguinte forma:

dados_pessoa_completo = {**pessoa, ** dados_pessoa}

for chave, item in dados_pessoa_completo.items():
    print(f'{chave}: {item}')

# usando kwargs (nomeados) e args (não nomeados):


def mostra_argumentos(*args, **kwargs):
    print('Não nomeados: ', args)
    print()
    print('Nomeados:')
    for chave, item in kwargs.items():
        print(f'{chave}: {item}')


mostra_argumentos(1, 2, 3, Nome='Davi', Sobrenome='Cândido')
