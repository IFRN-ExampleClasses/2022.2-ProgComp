valor    = int(input("Digite o número que você quer fatorial: "))
contador = 2
fatorial = 1

if(valor < 0):
    print('Não existe fatorial de número negativo...')
else:
   while (contador <= valor):
      fatorial *= contador
      contador +=  + 1
   print(f'\n{valor}! = {fatorial}')
