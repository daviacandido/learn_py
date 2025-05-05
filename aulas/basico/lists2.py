'''
Listas em Python
Tipo list é mutavel
SUporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +

CRUD - Create Read Update Delete
Criar, ler, alterar e apagar algo na lista:
'''

lista = [10, 20, 30, 40]
print(lista)

for i in range(len(lista)):
    if lista[i] == 20:
        lista[i] = 200
    if lista[i] == 40:
        del lista[i] # melhor usar list.pop()
    if lista[i] == 30:
        lista.append(70)
print(lista)

# Ao usar 'del' deve-se tomar cuidado devido
# ao alto processamento que pode ser causado,
# pois o python irá realocar todos os itens 
# que estão na frente do item apagado.
# É interessante que seja apagado ou adicionado
# novos itens apenas no final de uma lista.