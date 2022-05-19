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

print(nome, 'tem', idade, 'de idade e seu imc é', imc)
# muda o número de casas decimais dos floats
print(f'{nome} tem {idade} de idade e seu imc é {imc:.2f}')
# pega pela ordem, sendo possível repetir o valor pela posição
print('{0} tem {1} de idade e seu imc é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc))
