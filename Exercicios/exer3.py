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

    if manha:
        print("Bom dia!")
    elif tarde:
        print("Boa tarde!")
    elif noite:
        print("Boa noite!")
    else:
        print("Valor inserido não corresponde a um horário")
except ValueError:
    print("Valor inválido, insira um horário entre 0-23.")