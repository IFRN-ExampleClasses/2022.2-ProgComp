cateto_a = float(input('Informe o valor do Cateto A: '))
cateto_b = float(input('Informe o valor do Cateto B: '))

if (cateto_a > 0) and (cateto_b > 0):
    hipotenusa = ((cateto_a**2) + (cateto_b**2))**(0.5)
    print(f'A Hipotenusa do Triângulo é {hipotenusa}')
elif (cateto_a < 0):
    print('Foi informado um valor inválido para o Cateto A...')
else:
    print('Foi informado um valor inválido para o Cateto B...')
