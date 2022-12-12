valor = int(input('Informe um número: '))
valor_informado = valor

if (valor == 1) or (valor == 0):
    print(f'\n{valor}! = 1')
elif (valor < 0):
    print('\nNão existe Fatorial para o número informado...')
else:
    fatorial = valor
    while (valor > 1):
        valor -= 1
        fatorial *= valor

print(f'\n{valor}! = {fatorial}')