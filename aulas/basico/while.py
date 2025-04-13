'''
While e Break
=============

O loop while executa um bloco
de código enquanto uma condição for
verdadeira. O loop break interrompe o loop
antes que ele tenha terminado.
O loop while é útil quando não sabemos
quantas iterações serão necessárias.
O loop break é útil quando queremos
interromper o loop antes que ele tenha
terminado.

Exemplo:
'''

condicao = True
while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é {nome}')
    if nome == 'sair':
        break

contador = 0
while contador < 10:
    print(f'Contador: {contador}')
    contador += 1

print('Loop encerrado')
