# Variáveis
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = input('Digite sua idade: ')
nascimento = input('Digite seu ano de nascimento: ')
altura_metros = input('Digite sua altura em metros: ')
peso = input('Digite seu peso em kg: ')


# Objetos
class Pessoa:
    def __init__(self, nome, sobrenome, idade,
                 nascimento, altura_metros, peso):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.nascimento = nascimento
        self.altura_metros = altura_metros
        self.nome_completo = f'{nome} {sobrenome}'
        self.peso = peso


pessoa = Pessoa(nome, sobrenome, idade, nascimento,
                float(altura_metros), float(peso))


# Funções
def verifica_imc(pessoa):
    return 'Seu IMC é de {:.2f}'.format(
        pessoa.peso / (pessoa.altura_metros**2))


print(verifica_imc(pessoa))
