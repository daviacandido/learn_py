'''
Tomar cuidado com tipos mutáveis em listas:
'''

lista_a = ['João', 'Maria']
lista_b = lista_a


lista_a.append('Qualquer coisa')

print(lista_b)

# Note que a saída desse print é:
# ['João', 'Maria', 'Qualquer coisa']
# Isso ocorre pois a lista, quando recebe outra lista
# como variavel, na verdade em memória ela está recebendo
# o mesmo endereço de memória que a outra variável.
# Se for necessário copiar uma lista para outra variável:

# Em caso de listas simples:

lista_1 = [1, 2]
lista_2 = lista_1.copy()

lista_1.append(3)

print(lista_2)
print(lista_1)
