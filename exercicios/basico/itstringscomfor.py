# Qual letra apareceu mais vezes na frase?

frase = 'O python é uma linguagem de programação '\
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'.upper().replace(" ", "")


qtd_vezes_letra = 0
mais_vezes_letra = ''
for i in range(len(frase)):
    letra_atual = frase[i]

    contador_letra = frase.count(letra_atual)
    if qtd_vezes_letra < contador_letra:
        qtd_vezes_letra = contador_letra
        mais_vezes_letra = letra_atual

print(f'A letra "{mais_vezes_letra}" aparece {qtd_vezes_letra}x')
