num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
except:
    print("Não pode converter os números para realizar contas.")

# números e positivos (123445556)
# print(num1.isnumeric())
# print(num2.isnumeric())
