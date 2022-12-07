valor_a  = float(input('Informe o Valor de A: '))
valor_b  = float(input('Informe o Valor de B: '))
valor_c  = float(input('Informe o Valor de C: '))

if (valor_a == 0):
   print('\nNão é uma Equação do 2º Grau...')
else:
   delta = valor_b**2 - 4*valor_a*valor_c
   if (delta < 0):
      print('\nNão há Raizes nos Números Reais...')
   elif (delta == 0):
      print('\nRaízes Reais e Iguais...')
      x = -valor_b / (2*valor_a)
      print(f'\nX1 = X2 = {x}')
   else:
      print('\nRaízes Reais e Diferentes...')
      x1 = (-valor_b + delta**(1/2)) / (2*valor_a)
      x2 = (-valor_b - delta**(1/2)) / (2*valor_a)
      print(f'\nX1 = {x1} e X2 = {x2}')