'''
Flags, is e is not
==================

Flags - marcar um local
None - não existe
is e is not - é ou não é (um tipo, um valor, etc)
id = identificador/identidade
'''

# Exemplo 1
a = 10
b = 10
print(a is b)  # True - mesmo objeto
print(a is not b)  # False - mesmo objeto
print(id(a))  # id do objeto a
print(id(b))  # id do objeto b
print(a == b)  # True - mesmo valor
print(a == 10)  # True - mesmo objeto
print(a != 10)  # False - mesmo objeto
print(a is None)  # False - a não é None
print(a is not None)  # True - a não é None
print(a is True)  # False - a não é True
print(a is False)  # False - a não é False
print(a is not True)  # True - a não é True
print(a is not False)  # True - a não é False

# Exemplo 2

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Passou")
else:
    print("Não passou")

if passou_no_if is None:
    print("Não passou no if")
else:
    print("Passou no if")
    