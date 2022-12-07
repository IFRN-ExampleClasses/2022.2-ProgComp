coord_X = int(input('Informe a Coordenada X: '))
coord_Y = int(input('Informe a Coordenada Y: '))

if   (coord_X > 0)  and (coord_Y > 0): 
   print(f'O ponto ({coord_X},{coord_Y}) está no 1º Quadrante')
elif (coord_X < 0)  and (coord_Y > 0):
   print(f'O ponto ({coord_X},{coord_Y}) está no 2º Quadrante')
elif (coord_X < 0)  and (coord_Y < 0):
   print(f'O ponto ({coord_X},{coord_Y}) está no 3º Quadrante')
elif (coord_X > 0)  and (coord_Y < 0):
   print(f'O ponto ({coord_X},{coord_Y}) está no 4º Quadrante')
elif (coord_X > 0)  and (coord_Y == 0):
   print(f'O ponto ({coord_X},{coord_Y}) está no Eixo X (Positivo)')
elif (coord_X < 0)  and (coord_Y == 0):
   print(f'O ponto ({coord_X},{coord_Y}) está no Eixo X (Negativo)')
   print('O ponto ({0},{1}) está no Eixo X (Negativo)'.format(coord_X, coord_Y))
elif (coord_X == 0) and (coord_Y > 0):
   print(f'O ponto ({coord_X},{coord_Y}) está no Eixo Y (Positivo)')
elif (coord_X == 0) and (coord_Y < 0):
   print(f'O ponto ({coord_X},{coord_Y}) está no Eixo Y (Negativo)')
else:
   print(f'O ponto ({coord_X},{coord_Y}) está na Origem do Plano Cartesiano')
