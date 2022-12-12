valor = int(input("Digite o númmero de Fibonacci que você deseja: "))
fib_1 = 1
fib_2 = 1
proximo = fib_1 + fib_2

if (valor == 1):
   print(fib_1, end= "; ")
elif (valor > 1):
   print(fib_1, end= "; ")
   print(fib_2, end= "; ")
   while (valor > 2):
      print(proximo, end= "; ")
      fib_1   = fib_2 
      fib_2   = proximo
      proximo = fib_1 + fib_2
      valor   = valor - 1