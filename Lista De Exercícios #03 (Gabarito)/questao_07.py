valor_inicial   = int(input('Informe o valor inicial da P.G. ..............: '))
razao_pg        = int(input('Informe a razão da P.G. ......................: '))

while True:
    qt_elementos_pg = int(input('Informe a quantidade de elementos da P.G. (>0): ')) 
    if qt_elementos_pg > 0: break

contador    = 1
valor_atual = valor_inicial

print('\nElementos da P.G. :')
print(valor_atual, end = ' ; ')

# Exibindo os elementos da P.A.
while contador <= qt_elementos_pg:
    valor_atual = valor_atual * razao_pg
    print(valor_atual, end = ' ; ')
    contador += 1

# Exibindo a classificação da P.G.
if (razao_pg == 1):
    print('\nA P.G. CONSTANTE.')
elif (razao_pg < 0):
    print('\nA P.G. OSCILANTE.')
elif (razao_pg > 0) and valor_inicial > 0:
    print('\nA P.G. CRESCENTE.')
else:
    print('\nA P.G. DECRESCENTE.')

# Exibindo a soma dos elementos da P.G.
soma = (valor_inicial * ((razao_pg ** qt_elementos_pg) - 1)) / (razao_pg - 1)
print(f'\nA soma dos termos da P.G. é {int(soma)}')

# Exibindo o n-ésimo elemento da P.G.
while True:
    posicao_n = int(input('\nInforme a posição que se deseja saber o elemento da P.G. (>0): '))
    if posicao_n > 0: break

elemento_n = valor_inicial * (razao_pg ** (posicao_n - 1))
print(f'O elemento da posição {posicao_n} da P.G. é {elemento_n}')
