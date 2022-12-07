ang_a = float(input('Informe o ângulo A: '))
ang_b = float(input('Informe o ângulo B: '))
ang_c = float(input('Informe o ângulo C: '))

if (ang_a<=0) or (ang_b<=0) or (ang_c<=0):
   print('\nOs ângulos não podem ser negativos ou nulos...')
elif (ang_a + ang_b + ang_c != 180):
   print('\nA soma dos ângulos de um triângulo deve ser igual a 180...')
elif (ang_a==90) or (ang_b==90) or (ang_c==0):
   print('\nTriângulo Retângulo...')
elif (ang_a>90) or (ang_b>90) or (ang_c>90):
   print('\nTriângulo Obtusângulo...')
else:
   print('\nTriângulo Acutângulo...')