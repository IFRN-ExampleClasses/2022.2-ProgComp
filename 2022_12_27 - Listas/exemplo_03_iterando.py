lst_uf        = ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe']
lst_siglas    = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
lst_populacao = [3365351, 14985284, 9240580, 7153262, 4059905, 9674793, 3289290, 3560903, 2338474]

# Imprimir na tela os dados obedecendo o seguinte layout:
# 'O estado NOME_ESTADO (SIGLA) possui (QUANTIDADE) habitantes'

total_pop = 0
for i in range(len(lst_uf)):
   print(f'O estado {lst_uf[i]} ({lst_siglas[i]}) possui {lst_populacao[i]} habitantes')
   total_pop += lst_populacao[i]

# E no final imprimir a seguinte informação:
# 'O Nordeste possui um total de (QUANTIDADE TOTAL) habitantes'
print(f'\nO Nordeste possui um total de {total_pop} habitantes')