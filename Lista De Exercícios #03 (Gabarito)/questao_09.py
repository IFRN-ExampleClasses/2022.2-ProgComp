soma_positivo = 0

while True:
    numero = int(input('Informe um número: '))
    if (numero == 0): break
    if (numero > 0): soma_positivo += numero

print(f'A soma dos números positivos é {soma_positivo}')
