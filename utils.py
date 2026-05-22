from dados import lista_autor, lista_livros, lista_genero, lista_ano, lista_prioridade, stats_priority, status_leitura

def linha():
    print('-' * 50)

def ler_autor():
    autor = input('Digite o nome do autor: ')
    lista_autor.append(autor)
    return autor

def ler_livro():
    livro = input('Digite o nome do livro: ')
    lista_livros.append(livro)
    return livro

def ler_genero():
    genero = input('Digite o gênero do livro: ')
    lista_genero.append(genero)
    return genero

def ler_ano():
    while True:
        try:
            ano = int(input('Digite o ano de publicação do livro: '))
            lista_ano.append(ano)
            return ano
        except ValueError: 
            print('Por favor, digite um número válido para o ano.')

def ler_prioridade():
    while True:
        prioridade = input('Digite a prioridade de leitura (baixo, medio, alto): ').lower()
        if prioridade in stats_priority:
            lista_prioridade.append(prioridade)
            return prioridade
        else:
            print('Prioridade inválida. Por favor, escolha entre baixo, medio ou alto.')

def ler_status():
    while True:
        status = input('Digite o status de leitura (a ler, lendo, concluido): ').lower()
        if status in status_leitura:
            return status
        else:
            print('Status inválido. Por favor, escolha entre a ler, lendo ou concluido.')

def mostrar_livros():
    if not lista_livros:
        print('Nenhum livro cadastrado.')
        return
    for i in range(len(lista_livros)):
        print(f'Livro: {lista_livros[i]}, Autor: {lista_autor[i]}, Gênero: {lista_genero[i]}, Ano: {lista_ano[i]}, Prioridade: {lista_prioridade[i]}')
