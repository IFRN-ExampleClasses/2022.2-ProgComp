soma_h = soma_m = qt_h = qt_m = 0

while (qt_h+qt_m <= 5):
    idade = int(input('Informe a Idade: '))
    sexo = input('Informe o sexo (H ou M): ')
    if (idade > 0):
        if (sexo == 'H') or (sexo == 'h'):
            soma_h += idade
            qt_h += 1
        elif (sexo == 'M') or (sexo == 'm'):
            soma_m += idade
            qt_m += 1

print(f'\nA média geral das idade é {(soma_h+soma_m)/5}')
print(f'\nA média das idades dos Homens é {soma_h / qt_h}')
print(f'\nA média das idades das Mulheres é {soma_m / qt_m}')