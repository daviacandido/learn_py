"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""



try:
    hora = int(input("Digite a hora (0-23): ").strip())
    
    manha = 0 <= hora <= 11
    tarde = 12 <= hora <= 17
    noite = 18 <= hora <= 23

    manha_texto = 'Bom dia!'
    tarde_texto = 'Boa tarde!'
    noite_texto =  'Boa tarde!'

    if manha:
        print(manha_texto)
    elif tarde:
        print(tarde_texto)
    elif noite:
        print(noite_texto)
    else:
        print("Valor inserido não corresponde a um horário")
except ValueError:
    print("Valor inválido, insira um horário entre 0-23.")