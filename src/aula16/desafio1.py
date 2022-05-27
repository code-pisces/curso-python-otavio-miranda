numero = input('Digite um número inteiro: ')

if numero.isnumeric():
    par = int(numero) % 2 == 0
    if par:
        print(f'O número {numero} é par!')
    else:
        print(f'O número {numero} é ímpar!')
    print(f'O número {numero} é inteiro!')
else:
    print(f'O número {numero} não é inteiro.')
