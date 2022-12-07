x1 = int(input('Informe a Coordenada X1: '))
y1 = int(input('Informe a Coordenada Y1: '))

x2 = int(input('Informe a Coordenada X2: '))
y2 = int(input('Informe a Coordenada Y2: '))

distancia = ((x2-x1)**2 + (y2-y1)**2)**(0.5)

print(f'A Distância entre os pontos ({x1},{y1}) e ({x2},{y2}) é {distancia}')
