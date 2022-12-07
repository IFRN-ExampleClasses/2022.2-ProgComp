ano = int(input('Informe um valor inteiro entre 1900 e 2100: '))

if ano < 1900 or ano > 2100:
    print('Foi informado um valor inválido...')
elif (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0)):
    print('O ano informado é BISSEXTO...')
else:
    print('O ano informado é NÃO é BISSEXTO...')