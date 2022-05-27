hora = input('Digite a hora atual: ')
if hora.isdigit():
    hora_formatada = int(hora)
    if hora_formatada < 0 or hora_formatada > 23:
        print('Prescisa estar entre 0 e 23')
    else:
        if hora_formatada <= 11:
            print('Bom dia!')
        elif hora_formatada >= 12 and hora_formatada <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print('Formato de dado inesperado, digite um número!')
