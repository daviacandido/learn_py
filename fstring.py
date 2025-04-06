from datetime import datetime

"""
F-Strings
==========

F-strings, ou literais de strings formatadas, são uma maneira de
inserir expressões dentro de strings usando chaves `{}`. Elas são
prefixadas com a letra `f` ou `F`. F-strings fornecem uma maneira
mais legível e concisa de formatar strings em comparação com o
antigo formato `%` e o método `str.format()`.
"""

# Exemplo básico de f-string
nome = "Alice"
idade = 30
saudacao = f"Olá, meu nome é {nome} e eu tenho {idade} anos."
print(saudacao)  # Saída: Olá, meu nome é Alice e eu tenho 30 anos.

# F-strings podem conter expressões
x = 10
y = 5
resultado = f"A soma de {x} e {y} é {x + y}."
print(resultado)  # Saída: A soma de 10 e 5 é 15.

# F-strings podem ser usadas com dicionários
pessoa = {"nome": "Bob", "idade": 25}
informacao = f"{pessoa['nome']} tem {pessoa['idade']} anos."
print(informacao)  # Saída: Bob tem 25 anos.

# F-strings suportam formatação avançada
numero = 123.456789
numero_formatado = f"O número é {numero:.2f}."
print(numero_formatado)  # Saída: O número é 123.46.

# F-strings podem ser usadas com listas
frutas = ["maçã", "banana", "cereja"]
lista_frutas = f"Minhas frutas favoritas são: {', '.join(frutas)}."
print(lista_frutas)
# Saída: Minhas frutas favoritas são: maçã, banana, cereja.

# F-strings podem ser usadas com expressões condicionais
eh_adulto = True
status = f"Você é {'um adulto' if eh_adulto else 'um menor de idade'}."
print(status)  # Saída: Você é um adulto.


# F-strings podem ser usadas com funções
def quadrado(valor):
    return valor * valor


numero = 4
quadrado_numero = f"O quadrado de {numero} é {quadrado(numero)}."
print(quadrado_numero)  # Saída: O quadrado de 4 é 16.

# F-strings suportam formatação de data e hora
agora = datetime.now()
data_formatada = f"A data de hoje é {agora:%Y-%m-%d}."
print(data_formatada)  # Saída: A data de hoje é YYYY-MM-DD.

# F-strings suportam formatação de porcentagem
porcentagem = 0.1234
porcentagem_formatada = f"A porcentagem é {porcentagem:.2%}."
print(porcentagem_formatada)  # Saída: A porcentagem é 12.34%.

# F-strings suportam formatação de moeda
valor = 1234.56
valor_formatado = f"O valor é R${valor:,.2f}."
print(valor_formatado)  # Saída: O valor é R$1.234,56.

# F-strings suportam formatação de números com separadores
numero = 1000000
numero_formatado = f"O número é {numero:,}."
print(numero_formatado)  # Saída: O número é 1.000.000.

# F-strings suportam formatação de números em binário, octal e hexadecimal
numero = 255
binario_formatado = f"A representação binária é {numero:b}."
print(binario_formatado)  # Saída: A representação binária é 11111111.
octal_formatado = f"A representação octal é {numero:o}."
print(octal_formatado)  # Saída: A representação octal é 377.
hexadecimal_formatado = f"A representação hexadecimal é {numero:x}."
print(hexadecimal_formatado)  # Saída: A representação hexadecimal é ff.

# F-strings suportam formatação de números com preenchimento
numero = 42
numero_formatado = f"O número é {numero:05}."
print(numero_formatado)  # Saída: O número é 00042.

# F-strings suportam formatação de strings com alinhamento
texto = "Olá"
texto_formatado = f"{texto:<10} Mundo!"  # Alinhado à esquerda
print(texto_formatado)  # Saída: Olá       Mundo!
texto_formatado = f"{texto:>10} Mundo!"  # Alinhado à direita
print(texto_formatado)  # Saída:       Olá Mundo!
texto_formatado = f"{texto:^10} Mundo!"  # Centralizado
print(texto_formatado)  # Saída:    Olá    Mundo!

# F-strings suportam formatação de strings com truncamento
texto = "Olá, Mundo!"
texto_truncado = f"{texto:.5}"  # Truncado para 5 caracteres
print(texto_truncado)  # Saída: Olá,

# F-strings suportam formatação de strings com substituição
texto = "Olá, {nome}!"
texto_substituido = f"{texto.format(nome='Alice')}"
print(texto_substituido)  # Saída: Olá, Alice!

# F-strings suportam formatação de strings com expressões complexas
texto = "Olá, {nome.upper()}!"
texto_complexo = f"{texto.format(nome='Alice')}"
print(texto_complexo)  # Saída: Olá, ALICE!

# F-strings suportam formatação de strings com expressões aninhadas
texto = "Olá, {nome}!"
texto_aninhado = f"{texto.format(nome='Alice')}"
print(texto_aninhado)  # Saída: Olá, Alice!

# F-strings suportam formatação de strings
# com expressões condicionais aninhadas
texto = "Olá, {nome}!"
texto_condicional = f"{texto.format(nome='Alice' if True else 'Bob')}"
print(texto_condicional)  # Saída: Olá, Alice!

texto_condicional = f"{texto.format(nome='Alice' if False else 'Bob')}"
print(texto_condicional)  # Saída: Olá, Bob!
