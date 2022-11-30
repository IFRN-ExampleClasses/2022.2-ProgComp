numero = int(input('Informe um valor inteiro: '))

if numero < 0: numero *= -1

while numero > 0:
   auxiliar = numero % 10
   print(auxiliar)
   numero = int(numero/10)