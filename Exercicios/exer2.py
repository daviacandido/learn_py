"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input("Digite um número inteiro: ").strip()

try:
    numero = int(numero)
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é impar.")
except ValueError:
    print("O valor digitado não é um número inteiro.")

