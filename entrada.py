entrada = input('[E]ntrar ou [S]air').upper()
senha = input('Digite a senha: ')

if entrada == 'E':
    if senha == '1234':
        print('Acesso permitido')
    else:
        print('Senha incorreta')