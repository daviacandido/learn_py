'''
Lista de listas e seus índices
'''

salas = [
    ['Maria', 'Helena'],
    ['Claudio', 'Claudia', 'Anderson'],
    ['Luiz', 'Davi']
]

for i, sala in enumerate(salas):
    for i, aluno in enumerate(sala):
        print(i, aluno)
    print(i, sala)