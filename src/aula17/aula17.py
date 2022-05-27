"""
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Números flutuantes (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^) (QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

# num_1 = 10
# num_2 = 3
# divisao = num_1 / num_2

nome = 'Gustavo Amorim'
# print('{:.2f}'.format(divisao))
# print(f'{divisao:.2f}')
# print(f'{nome:s}')

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0>10}')
print(f'{num_2:0<10}')
print(f'{num_2:0^10}')

# Formatar strings int para float
print(f'{num_2:.2f}')
print(f'{num_2:0>10.2f}')

# strings
print(f'{nome:#^50}')
sobrenome = 'Amorim'
nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobrenome)
print(nome_formatado)

nome = nome.ljust(20, '#')
print(nome.lower())
print(nome.upper())
print(nome.title())
