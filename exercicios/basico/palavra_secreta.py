import os

"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0
acertou = False
acertos = 0
erros = 0

while acertou is False:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra. ')
        continue

    tentativas += 1

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        acertos += 1
    else:
        erros += 1

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '#'

    os.system('clear')

    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:

        print(
            'VOCÊ ACERTOU! FORAM NECESSÁRIAS ', tentativas,
            'TENTATIVAS, SENDO', acertos,
            ' ACERTOS E ', erros, ' ERROS PARA FINALIZAR'
        )

        acertou = True
