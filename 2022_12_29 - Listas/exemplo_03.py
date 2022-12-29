lst_uf        = ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe']
lst_siglas    = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
lst_populacao = [3365351, 14985284, 9240580, 7153262, 4059905, 9674793, 3289290, 3560903, 2338474]

lst_nordeste = list()

for pos in range(len(lst_uf)):
   #lst_nordeste.append( [lst_uf[pos], lst_siglas[pos], lst_populacao[pos]] )
   lst_nordeste.append( list(lst_uf[pos], lst_siglas[pos], lst_populacao[pos]) )

print(lst_nordeste)