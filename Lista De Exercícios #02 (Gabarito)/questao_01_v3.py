# Só funciona com variáveis do tipo inteiro ou float

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))

print('\nValor de A (antes da troca): ', a)
print('Valor de B (antes da troca): ', b)

b = a - b
a = a - b
b = a + b

print('\nValor de A (depois da troca): ', a)
print('Valor de B (depois da troca): ', b)