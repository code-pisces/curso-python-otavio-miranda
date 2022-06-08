"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
# lista[5] = 'Qualquer outra coisa.'
# print(lista[5])
# print(lista[::-1])

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(l2)

# l2.append(7)
# l2.insert(0, 'banana')
# l2.pop()

# print(l2)
# l1.extend(l2)
# # l3 = l1 + l2 concatenando listas
# print(l1)
# print(l2)

# l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l2)
# l2.insert(0, 'Banana')
# print(l2)
# del(l2[0])

# print(l2)

# l2 = list(range(0, 10))
# print(l2)

# soma = 0
# for valor in l2:
#     soma += valor
# print(soma)


# l2 = ['String', True, 10, -20.5]

# for elem in l2:
#     print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Aff, a letra "{letra}" não existe na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f"Que legal, você ganhou!!! A palavra era {secreto_temporario}")
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
    print()
