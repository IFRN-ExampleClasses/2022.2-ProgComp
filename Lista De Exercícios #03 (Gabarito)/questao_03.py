valor = int(input('Informe um valor inteiro positivo: '))

if (valor > 1):
    print(f'\nCalculando os primos até {valor}...\n')
    auxiliar = 1
    while (auxiliar <= valor+1):
        divisores = 0
        divisor   = 1
        while (divisor <= valor+1):
            if (auxiliar % divisor == 0): divisores += 1
            if (divisores > 2): break
            divisor += 1
        if (divisores <= 2): print(auxiliar, end='; ')
        auxiliar += 1
else:
    print('Informe um valor inteiro positivo maior que 1...')