# %s - string
# %d - inteiro
# %f - float
# %x - hexadecimal
# %X - hexadecimal (letras maiúsculas)
# %e - notação científica
# %E - notação científica (letras maiúsculas)
# %g - notação científica (sem zeros à direita)
# %G - notação científica (sem zeros à direita, letras maiúsculas)
# %r - representação
# %a - representação (com aspas)
# % - formatação

nome = 'Davi'
preco = 1000.503
variavel = '%s, o preço é R%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %i é %08X' % (1500, 1500))
