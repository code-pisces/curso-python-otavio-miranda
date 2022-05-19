"""
Tipos de dados
str - string - 'Assim' "Assim"
int - inteiro 123456 - 0 -10 -20
float - real/ponto flutuante - 10.80 1.5 -10.10
bool - booleano/lógico - True/False - 10 == 10
"""
print('Luiz', type('Luíz'))
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))

# verificando se está vazio
print(bool([]))
print('luiz', type('luiz'), bool('luiz'))

# conversão de string para inteiro
print('10', type(int('10')))

"""
Desafio da aula 4
"""

# Nome: String
print('Gustavo', type('Gustavo'))

# Idade: int
print(16, type(16))

# Altura: float
print(1.87, type(1.87))

# É maior de idade
print(16 > 18, type(16 > 18))
