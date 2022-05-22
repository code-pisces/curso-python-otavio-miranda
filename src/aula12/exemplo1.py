"""
Operadores Lógicos
and, or, not
in e not in
"""

a = 2
b = 2
c = 3

print(a == b and b < c)  # semelhante a: a == b && b < c
print(not a == b and not b < c)  # semelhante: !(a == b) && !(b < c)
print(a == b or b < c)

# demonstração do not
a = 2
b = 3

if not b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')

d = 'ASA'
e = 0
if not e:
    print('Por favor, preencha o valor de E.')


nome = 'Gustavo Amorim'

# if 'Yuj' in nome:
#     print('Existe.')
# else:
#     print('Não existe.')

if 'Gus' not in nome:
    print('Executei.')
else:
    print('Existe o texto.')
