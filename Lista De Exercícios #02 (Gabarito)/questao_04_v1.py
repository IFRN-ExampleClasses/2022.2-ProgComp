valor = int(input('Informe um valor inteiro: '))

if (valor == 0):
    print('O valor informado é NULO...')
elif (valor > 0):
    if (valor % 2 == 0):
        print('O valor informado é POSITIVO e PAR...')
    else:
        print('O valor informado é POSITIVO e ÍMPAR...')
else:
    if (valor % 2 == 0):
        print('O valor informado é NEGATIVO e PAR...')
    else:
        print('O valor informado é NEGATIVO e ÍMPAR...')
