peso   = float(input('Informe o seu peso (kg) .: '))
altura = float(input('Informe a sua altura (m) : '))
idade  = int(input('Informe a sua idade .....: '))

if (peso<=0) or (altura<=0) or (idade < 18):
    print('Valores informados inválidos...')
else:
    imc = peso / (altura**2)
    print(f'\nA pessoa de altura {altura}m e peso {peso}kg tem IMC = {imc}')
    if (imc < 18.5):
        print('\nAbaixo do Peso...')
    elif (imc < 24.9):
        print('\nPeso Normal...')
    elif (imc < 29.9):
        print('\nSobrepeso...')
    elif (imc < 34.9):
        print('\nObesidade Grau I...')
    elif (imc < 39.9):
        print('\nObesidade Grau II...')
    else:
        print('\nObesidade Grau III ou Mórbida...')