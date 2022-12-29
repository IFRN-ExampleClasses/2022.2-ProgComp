lst_uf        = ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe']
lst_siglas    = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
lst_populacao = [3365351, 14985284, 9240580, 7153262, 4059905, 9674793, 3289290, 3560903, 2338474]

# O programa deve solicitar a sigla da uf e exibir as informações
# caso a sigla informada exista na lista obedecendo o seguinte layout:
# 'O estado NOME_ESTADO (SIGLA) possui (QUANTIDADE) habitantes'

sigla = input('Informe a sigla do estado: ').upper()

if sigla in lst_siglas:
   pos = lst_siglas.index(sigla)
   print(f'O estado {lst_uf[pos]} ({lst_siglas[pos]}) possui {lst_populacao[pos]} habitantes')
else:
   print('A sigla não consta na lista...')