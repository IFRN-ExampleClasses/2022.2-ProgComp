valor_inicial   = int(input('Informe o valor inicial da P.A. ..............: '))
razao_pa        = int(input('Informe a razão da P.A. ......................: '))

while True:
    qt_elementos_pa = int(input('Informe a quantidade de elementos da P.A. (>0): ')) 
    if qt_elementos_pa > 0: break

contador    = 1
valor_atual = valor_inicial

print('\nElementos da P.A. :')
print(valor_atual, end = ' ; ')

# Exibindo os elementos da P.A.
while contador <= qt_elementos_pa:
    valor_atual += razao_pa
    print(valor_atual, end = ' ; ')
    contador += 1

# Exibindo a classificação da P.A.
if (razao_pa == 0):
    print('\nA P.A. CONSTANTE.')
elif (razao_pa > 0):
    print('\nA P.A. CRESCENTE.')
else:
    print('\nA P.A. DECRESCENTE.')

# Exibindo a soma dos elementos da P.A.
soma = ((valor_inicial + valor_atual) * qt_elementos_pa)/2
print(f'\nA soma dos termos da P.A. é {int(soma)}')

# Exibindo o n-ésimo elemento da P.A.
while True:
    posicao_n = int(input('\nInforme a posição que se deseja saber o elemento da P.A. (>0):'))
    if posicao_n >0: break
    
elemento_n = valor_inicial + (posicao_n - 1) * razao_pa
print(f'O elemento da posição {posicao_n} da P.A. é {elemento_n}')