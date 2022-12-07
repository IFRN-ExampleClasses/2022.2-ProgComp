valor = int(input('Informe um valor inteiro: '))

if (valor == 0):
    print('O valor informado é NULO...')
elif (valor > 0) and (valor % 2 == 0):
    print('O valor informado é POSITIVO e PAR...')
elif (valor > 0) and (valor % 2 != 0):
    print('O valor informado é POSITIVO e ÍMPAR...')
elif (valor < 0) and (valor % 2 == 0):
    print('O valor informado é NEGATIVO e PAR...')
else:
    print('O valor informado é NEGATIVO e ÍMPAR...')
