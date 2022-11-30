# Fazer um programa que solicite 2 notas (considerar notas inteiras) 
# e calcule a média ponderada das 2 notas (considerar peso 2 para
# a primeira nota e peso 3 para a segunda nota)

nota_1 = int(input('Informe a 1ª Nota: '))
nota_2 = int(input('Informe a 2ª Nota: '))

media  = (nota_1*2 + nota_2*3) / 5

print(f'A média foi {media}')