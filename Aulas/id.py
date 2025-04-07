'''
ID - Identidade do valor na memória
===================================

ID é uma função embutida do Python
que retorna o endereço de memória de um objeto.
O endereço de memória é um número inteiro
que representa a localização do objeto
na memória do computador.
O ID é único para cada objeto durante
o tempo de vida do objeto, ou seja,
enquanto o objeto existir na memória.
'''

# Exemplo de uso da função id()
a = 10
b = 15
c = a
print(f'O ID de a é: {id(a)}')
print(f'O ID de b é: {id(b)}')
print(f'O ID de c é: {id(c)}')