lst_uf        = ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe']
lst_siglas    = ['AL', 'BA', 'CE', 'MA', 'PE', 'PI', 'RN', 'SE']
lst_populacao = [3365351, 14985284, 9240580, 7153262, 9674793, 3289290, 3560903, 2338474]

print(lst_uf)
print(lst_siglas)
print(lst_populacao)

# Inserir os dados da Paraíba na posição 4 das respectivas listas
# Paraíba / PB / 4059905

lst_uf.insert(4, 'Paraíba')
lst_siglas.insert(4, 'PB')
lst_populacao.insert(4, 4059905)

print(lst_uf)
print(lst_siglas)
print(lst_populacao)