'''
Constantes e Complexidade de Código
===================================

Constantes são variaveis que não mudam de
valor durante a execução do programa.
Elas são definidas com letras maiúsculas
e são utilizadas para armazenar valores
fixos que podem ser utilizados em
diferentes partes do código.
Por exemplo, se você tem um valor que representa
a taxa de imposto, você pode definir uma
constante para esse valor e usá-la
em diferentes partes do seu código.
'''

# Exemplos de constante:
TAXA_IMPOSTO = 0.2
preco_produto = 100
imposto = preco_produto * TAXA_IMPOSTO
print(f"O imposto sobre o produto é: {imposto}")

# ---------------#


# Complexidade do Código pode tornar o código inlegivel,
# por exemplo, muitas condições no mesmo if.

velocidade_carro = 61
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

# Exemplo de um código complexo e ruim:

'''
if velocidade_carro > RADAR_1:
    print('Velocidade do carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
    velocidade_carro > RADAR_1:
    print('Carro multado em radar 1')
'''

# Exemplo de um código mais limpo:

velocidade_carro_passou_radar_1 = velocidade_carro > RADAR_1

verifica_local_carro_velocidade = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_passou_radar_1:
    print('Velocidade carro passou do radar 1')

if verifica_local_carro_velocidade and velocidade_carro_passou_radar_1:
    print('Carro multado em radar 1')
