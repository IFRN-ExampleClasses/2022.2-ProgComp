lst_nordeste = [
	               ['Alagoas'            , 'AL', 3365351], 
	               ['Bahia'              , 'BA', 14985284], 
	               ['Ceará'              , 'CE', 9240580], 
	               ['Maranhão'           , 'MA', 7153262], 
	               ['Paraíba'            , 'PB', 4059905], 
	               ['Pernambuco'         , 'PE', 9674793], 
	               ['Piauí'              , 'PI', 3289290], 
	               ['Rio Grande do Norte', 'RN', 3560903], 
	               ['Sergipe'            , 'SE', 2338474]
               ]

lst_nordeste.sort(key=lambda l:l[1])

# O programa deve solicitar a sigla da uf e exibir as informações
# caso a sigla informada exista na lista obedecendo o seguinte layout:
# 'O estado NOME_ESTADO (SIGLA) possui (QUANTIDADE) habitantes'

sigla = input('Informe a sigla do estado: ').upper()

retorno = list()
for estado in lst_nordeste:
	if sigla in estado:
		retorno = estado
		break

if len(retorno) > 0:
	print(f'O estado {retorno[0]} ({retorno[1]}) possui {retorno[2]} habitantes')
else:
	print('A sigla não consta na lista...')
