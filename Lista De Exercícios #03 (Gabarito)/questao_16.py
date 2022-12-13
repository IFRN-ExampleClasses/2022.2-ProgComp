valor = int(input('Informe um valor inteiro positivo: '))

if valor > 0:
   # Verificando a  quantidade de dígitos
   auxiliar = valor
   qt_digitos = 0
   while auxiliar > 0:
      auxiliar = int(auxiliar/10)
      qt_digitos += 1

   # Calculando o número de Armstrong
   numero = valor
   num_armstrong  = 0 
   while numero > 0:
      auxiliar = numero % 10
      num_armstrong += auxiliar ** qt_digitos
      numero = int(numero/10)

   print(f'Número Informado...: {valor}')
   print(f'Número de Armstrong: {num_armstrong}')

   if (valor == num_armstrong):
      print('O Número informado é Narcisista...')
   else:
      print('O Número informado Não é Narcisista...')