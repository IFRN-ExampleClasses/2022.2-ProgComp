# Lendo a massa inicial
massa_inicial = int(input('Informe a massa inicial (gramas): '))

massa_final    = massa_inicial
tempo_segundos = 0

# Calculando a massa final e o tempo decorrido
while massa_final >= 0.5:
   massa_final = massa_final / 2
   tempo_segundos += 50

# Calculando as horas
tempo_horas    = tempo_segundos // 3600
tempo_segundos = tempo_segundos % 3600

# Calculando os minutos
tempo_minutos  = tempo_segundos // 60
tempo_segundos = tempo_segundos % 60

# Exibindo os dados
print(f'\nMassa inicial : {massa_inicial} gramas')
print(f'\nMassa final ..: {massa_final} gramas')
print(f'\nTempo Total ..: {tempo_horas} h, {tempo_minutos} m, {tempo_segundos} s')

