lado_a = float(input('Informe o lado A: '))
lado_b = float(input('Informe o lado B: '))
lado_c = float(input('Informe o lado C: '))

if (lado_a<=0) or (lado_b<=0) or (lado_c<=0):
   print('\nOs lados não podem ser negativos ou nulos...')
elif (lado_a>lado_b+lado_c) or (lado_b>lado_a+lado_c) or (lado_c>lado_a+lado_c):
   print('\nA soma de dois lados não pode ser menor que o terceiro lado...')
elif (lado_a==lado_b) and (lado_b==lado_c):
   print('\nTriângulo Equilátero...')
elif (lado_a!=lado_b) and (lado_b!=lado_c) and (lado_c!=lado_a):
   print('\nTriângulo Escaleno...')
else:
   print('\nTriângulo Isósceles...')