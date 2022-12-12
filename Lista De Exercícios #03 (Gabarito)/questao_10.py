valor = int(input('Informe um número: '))

menor = maior = soma = valor 
contador = 1

while True:
    valor = int(input('Informe um número: '))
    if (valor == 0): break
    if (valor > maior):
        maior = valor
    elif (valor < menor):
        menor = valor
    contador += 1
    soma += valor

print(f'\nO Maior número digitado foi {maior}')
print(f'\nO Menor número digitado foi {menor}')
print(f'\nA Média dos valores digitador é {soma/contador}')