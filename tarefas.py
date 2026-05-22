import dados  

def cadastrar_livro(titulo, autor, ano, gênero, prioridade):
    novo_id = len(tarefas) + 1
    livro = {
        "id": novo_id
        "titulo": titulo,
        "ano": ano,
        "autor": autor,
        "genero": genero,
        "prioridade": prioridade

    }
    tarefas.append(livros)
    return livros

    def listar_livros(livros):
        for livros in tarefas:
            if livros ['titulo'].lower() == titulo.lower(): 
                print('\n---- Livros registrados ----')
                print(f"id: {livro['titulo']}")
                print(f"titulo: {livro['titulo']}")
                print(f"ano: {livro['ano']}")
                print(f"autor: {livro['autor']}")
                print(f"genero: {livro['genero']}")
                print(f"prioridade: {livro['prioridade']}")
                print("----------------------")
                return

print(f'livro'{titulo}'não encontrado o cadastro do livro.')

def pedir_livro(titulo):
    for livros in tarefas:
        if livro['titulo'].lower() == titulo.lower():
            pedidos.append(livro)

            print(f'livro '{titulo}' foi feito um pedido com sucesso!')
            return

    print ("livro nao encontrado")

    
def consultar_livro