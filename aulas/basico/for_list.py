# for in com listas

lista = ['João', 'Maria', 'José']

for nome in lista:
    print(nome)
    if nome == 'José':
        lista.append('Davi')
print(lista)