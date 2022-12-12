while True:
    numero = int(input('\nInforme um Número: '))
    if (numero == 0): break
    if (numero % 2 == 0):
        print(f'O número {numero} é PAR...')
    else:
        print(f'O número {numero} é ÍMPAR...')
