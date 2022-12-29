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
lst_nordeste.sort(key=lambda l:l[2]  ,reverse=True)

#lst_nordeste_2 = sorted(lst_nordeste, key=lambda l:l[2]  ,reverse=True)

total_pop = 0
for estado in lst_nordeste:
   print(f'O estado {estado[0]} ({estado[1]}) possui {estado[2]} habitantes')
   total_pop += estado[2]   

print(f'\nO Nordeste possui um total de {total_pop} habitantes')