# Fazer um programa que solicite um número inteiro
# e diga se ele é par, ímpar ou nulo

valor = int(input('Informe um valor: '))

if valor == 0:
   print('Valor ZERO...')
elif valor % 2 == 0:
   print('Valor ÍMPAR...')
else:
   print('Valor PAR...')