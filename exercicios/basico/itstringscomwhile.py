# Qual letra apareceu mais vezes na frase?

frase = 'O python é uma linguagem de programação '\
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'.upper()

i = 0
apareceu_mais_vezes = 0
letra_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    apareceu_mais_vezes_atual = frase.count(letra_atual)

    if apareceu_mais_vezes < apareceu_mais_vezes_atual:
        apareceu_mais_vezes = apareceu_mais_vezes_atual
        letra_mais_vezes = letra_atual

    i += 1

print('A letra que apareceu mais vezes foi: '
      f'"{letra_mais_vezes}", que apareceu '
      f'{apareceu_mais_vezes}x')
