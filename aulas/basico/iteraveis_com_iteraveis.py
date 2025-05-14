'''
Lista de listas e seus índices
'''

salas = [
    ['Maria', 'Helena'],
    ['Claudio', 'Claudia', 'Anderson'],
    ['Luiz', 'Davi']
]

for numero_da_sala, alunos_na_sala in enumerate(salas):
    for numero_aluno, aluno in enumerate(alunos_na_sala):
        print(f'Sala: {numero_da_sala}\nAluno: {aluno}')
