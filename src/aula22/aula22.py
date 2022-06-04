"""
For in em python
Iterando strings com for
função range(start=0, stop, step=1)
"""
texto = 'python'

for n in range(0, 100, 8):
    print(n)

print("########")

for n in range(100):
    if n % 8 == 0:
        print(n)

print('########')

texto = 'Python'
nova_string = ''

# continue - pule pro próximo laço
# break - para o laço

for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)
# for n, letra in enumerate(texto):
#     print(n, letra)
