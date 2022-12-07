# Só funciona com variáveis do tipo inteiro - Lógica XOR    

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))

print('\nValor de A (antes da troca): ', a)
print('Valor de B (antes da troca): ', b)

a ^= b
b ^= a
a ^= b

print('\nValor de A (depois da troca): ', a)
print('Valor de B (depois da troca): ', b)