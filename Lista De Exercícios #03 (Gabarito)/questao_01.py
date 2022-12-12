valor_decimal = int(input('Digite um numero decimal: '))

binario  = ''
auxiliar = valor_decimal

while auxiliar >= 1:
  binario = str(auxiliar % 2) + binario
  auxiliar = auxiliar // 2

print(f'\n O valor {valor_decimal} (base10) em binário é: {binario}')
