numero = int(input('Informe um valor inteiro: '))

if numero < 0: numero *= -1

qt_digitos = 0
auxiliar   = 1

while auxiliar < numero:
   auxiliar   *= 10
   qt_digitos += 1

print(qt_digitos)
