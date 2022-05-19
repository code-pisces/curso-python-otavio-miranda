nome = "Gustavo"
idade = 16
altura = 1.87
peso = 70.00
ano_atual = 2022

ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f"{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.")
print(f"O IMC de {nome} é {imc:.2f}")
print(f"{nome} nasceu em {ano_nascimento}.")
