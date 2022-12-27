# Criando uma lista de números
# pares entre 1 e 100
# MODO CLÁSSICO

numeros = list()

for x in range(1, 101):
   if x % 2 == 0: numeros.append(x)

print(numeros)