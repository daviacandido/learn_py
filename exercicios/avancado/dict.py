# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


def verifica_acerto(escolha, resposta, lista_opcoes):
    qtd_opcoes = len(lista_opcoes)
    if escolha is not None:
        if escolha >= 0 and escolha < qtd_opcoes:
            if lista_opcoes[escolha] == resposta:
                return True


acertos = 0

for pergunta in perguntas:

    print(f'Pergunta: {pergunta["Pergunta"]}')
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    escolha = None
    while escolha is None:
        try:
            escolha_input = input(f'Escolha a resposta entre 0 e {len(opcoes) - 1}: ')
            escolha = int(escolha_input)
            if escolha < 0 or escolha >= len(opcoes):
                print(f'Escolha um valor válido entre 0 e {len(opcoes) - 1}')
                escolha = None
        except ValueError:
            print(f'Entrada inválida! Escolha um valor inteiro entre 0 e {len(opcoes) - 1}')

    if verifica_acerto(escolha, pergunta['Resposta'], opcoes):
        acertos += 1
        print('Acertou!')
    else:
        print('Errou!')
    print()

print(f'Você acertou {acertos} de {len(perguntas)} questões')
