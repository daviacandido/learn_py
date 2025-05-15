lista = ['Maria', 'Helena', 'Eduarda']
salas = [
    ['Maria', 'Helena'],
    ['Claudio', 'Claudia', 'Anderson'],
    ['Luiz', 'Davi']
]

print(*salas, sep='\n')
print(*lista, end='\n', sep=', ')
