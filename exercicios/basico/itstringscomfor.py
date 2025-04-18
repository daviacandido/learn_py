# Qual letra apareceu mais vezes na frase?

frase = 'O python é uma linguagem de programação '\
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'.upper().replace(" ", "")

letra_mais_vezes = ''
qtd_letra = 0

for letra in frase:

    contador_letra = frase.count(letra)

    if qtd_letra < contador_letra:
        qtd_letra = contador_letra
        letra_mais_vezes = letra

print(f'A letra {letra_mais_vezes} apareceu {qtd_letra}x')
