nome = input('Digite seu primeiro nome: ')
numero_letras_nome = len(nome)

if numero_letras_nome <= 4:
    print('Seu nome é curto.')
elif numero_letras_nome >= 5 and numero_letras_nome <= 6:
    print('Seu nome é normal.')
elif numero_letras_nome > 6:
    print('Seu nome é muito grande.')
