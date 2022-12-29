lst_uf        = ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe']
lst_siglas    = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
lst_populacao = [3365351, 14985284, 9240580, 7153262, 4059905, 9674793, 3289290, 3560903, 2338474]

print('-'*100)
print(lst_uf)
print(lst_siglas)
print(lst_populacao)
print('-'*100)

# Imprimir na tela os dados obedecendo o seguinte layout:
# 'O estado NOME_ESTADO (SIGLA) possui (QUANTIDADE) habitantes'
# Sendo que em ordem decrescente da quantidade de habitantes
lst_pop_ord = sorted(lst_populacao, reverse=True)
print('LST_POPULACAO: ', lst_populacao)
print('LST_POP_ORD..: ', lst_pop_ord)
print('-'*100)

total_pop = 0
for i in range(len(lst_pop_ord)):
   pos = lst_populacao.index(lst_pop_ord[i])
   print(f'O estado {lst_uf[pos]} ({lst_siglas[pos]}) possui {lst_pop_ord[i]} habitantes')
   total_pop += lst_populacao[i]

# E no final imprimir a seguinte informação:
# 'O Nordeste possui um total de (QUANTIDADE TOTAL) habitantes'
print(f'\nO Nordeste possui um total de {total_pop} habitantes')