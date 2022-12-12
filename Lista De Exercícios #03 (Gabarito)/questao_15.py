# Lendo o valor inicial
valor = int(input('Informe o valor: '))

contador   = 1
numero_tri = 0

# Aplicando a Fórmula do Número Triangular
while numero_tri < valor:
   numero_tri = (contador * (contador + 1)) / 2
   contador += 1

# Verificando se o número informado é triangular ou não
if (valor == numero_tri):
   print('É um número triangular')
else:
   print('Não é um número triangular')

