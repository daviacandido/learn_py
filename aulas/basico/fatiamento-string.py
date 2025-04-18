
# Fatiamento de Strings e Length
# ==============================

'''
Fatiamento de strings é uma técnica que permite
extrair partes de uma string original.

A sintaxe básica para fatiar uma string é a seguinte:
string[inicio:fim:passo]
onde:
- inicio: índice inicial (inclusivo) do fatiamento.
- fim: índice final (exclusivo) do fatiamento.
- passo: intervalo entre os índices (opcional).

Exemplos de fatiamento de strings:
'''

variavel = "Python é uma linguagem de programação"
print(variavel[0:6])  # Python
print(variavel[7:10])  # é u
print(variavel[9:22])  # uma linguagem
print(variavel[0:20:2])  # Pto  m iga

variavel = "Aprendendo Python"
print(variavel[0:10])  # Aprendendo
print(variavel[11:17])  # Python
print(variavel[0:17:2])  # Arned yhn
print(variavel[::-1])  # nohtyP odnednerpA


'''
Length é uma função que retorna o tamanho
de uma string, ou seja,
o número total de caracteres
presentes na string.
A sintaxe é a seguinte:
len(string)

Exemplo de uso da função len():
'''


print(len(variavel))  # 17
