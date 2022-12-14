url = input('Informe a URL: ')
url = url[url.find('//')+2:]

servidor  = url[:url.find('/')]
diretorio = url[url.find('/'):]

arquivo = diretorio[::-1]
arquivo = arquivo[:arquivo.find('/')]
arquivo = arquivo[::-1]

#diretorio = diretorio[:diretorio.find(arquivo)]
#diretorio = diretorio[:len(diretorio)-len(arquivo)]
diretorio = diretorio.replace(arquivo, '')

print('')
print(url)
print('')
print(f'Servidor..: {servidor}')
print(f'Diretório.: {diretorio}')
print(f'Arquivo...: {arquivo}')
print('')
