"""
Condições IF, ELIF, ELSE
== : igualdade,
> : maior que,
>= : maior igual que,
< : menor que,
<= : menor igual que,
!= : diferente
"""

# var_1 = 'Gustavo'
# var_2 = 'Amorim'

# num_1 = 2  # int
# num_2 = 2  # int

# expressao = (var_1 != var_2)
# print(expressao)

nome = input('Qual o seu nome? ')
idade = int(input('Qual sua idade? '))
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')
