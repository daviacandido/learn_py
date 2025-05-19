"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1


def escopo():
    # nesse caso, o x está fora da função
    # por isso, é possível puxar o valor:
    y = 1
    print(x)


escopo()

# print (y) aqui retornaria erro
# pois se encontra dentro da funcao e
# nao é uma variavel global
