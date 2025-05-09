import os

"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

lista = []
continua = True
while continua is True:
    opcao = input(
        '- [A]pagar\n- [I]nserir\n- [L]istar\n[S]air\nSelecione uma opção: '
        )
    opcao_real = opcao.upper()

    if opcao_real == 'I':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao_real == 'A':
        indice_str = input('Escolha o íncide para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
            os.system('clear')
            print('Lista agora:')

            for id_indice, valor in enumerate(lista):
                print(id_indice, valor)

        except ValueError:
            os.system('clear')
            print('Por favor, digite um número inteiro.')
        except IndexError:
            os.system('clear')
            print('Indice não existe.')
    elif opcao_real == 'L':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for id_indice, valor in enumerate(lista):
            print(id_indice, valor)
    elif opcao_real == 'S':
        conitnua = False
    else:
        print('Por favor, escolha I, A ou L')
