valor = int(input('Informe um número: '))

if (valor > 3):
    anterior = atual = 1
    print(anterior, end= "; ")
    print(atual, end= "; ")

    posicao = 3
    while (posicao <= valor):
        proximo = anterior + atual
        print(proximo, end= "; ")
        anterior = atual
        atual    = proximo
        posicao  += 1
        