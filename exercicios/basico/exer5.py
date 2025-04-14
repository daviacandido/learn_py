'''
Iterando strings com while
'''

# Crie uma string e faça um loop para imprimir cada letra dela

nome = 'Davi Araujo Cândido'
contador = 0
tamanho_nome = len(nome)
nova_string = ''

while contador < tamanho_nome:
    nova_string += nome[contador]
    contador += 1

print(nova_string)
