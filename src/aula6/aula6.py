"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Luiz'
idade = 32  # int
altura = 1.80  # float
e_maior = idade > 18  # bool
# bool, quando o booleano for explícito,
# o nome com a primeira letra maiúscula: True e False.
data_1 = True
data_atual = 2019  # int
peso = 80
imc = peso / (altura ** 2)

print('Multiplicação:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

print(idade * altura)

print(nome, 'tem', idade, 'de idade e seu imc é', imc)
