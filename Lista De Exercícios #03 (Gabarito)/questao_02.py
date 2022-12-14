while True:
    numero = int(input('Informe um número positivo: '))
    if numero > 0: break

contador_divisores = 0
contador           = 1
print(f'Os divisores de {numero}: ', end = '')
while contador <= numero:
    if numero % contador == 0:
        contador_divisores += 1
        print(contador, end = ' ; ')
    contador += 1

if contador_divisores == 2:
    print ('\nO número informado é PRIMO...\n')
else:
    print ('\nO número informado NÃO é PRIMO...\n')
