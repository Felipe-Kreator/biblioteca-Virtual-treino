from dados import lista_autor, lista_livros, lista_genero, lista_ano, lista_prioridade, stats_priority, status_leitura
from utils import linha, ler_autor, ler_livro, ler_genero, ler_ano, ler_prioridade, ler_status, mostrar_livros

def main():
    while True:
        linha()
        print('Menu de opções:')
        print('1. Cadastrar livro')
        print('2. Mostrar livros cadastrados')
        print('3. Sair')
        linha()
        
        escolha = input('Escolha uma opção: ')
        
        if escolha == '1':
            autor = ler_autor()
            livro = ler_livro()
            genero = ler_genero()
            ano = ler_ano()
            prioridade = ler_prioridade()
            status = ler_status()
            print(f'Livro "{livro}" do autor "{autor}" cadastrado com sucesso!')
        
        elif escolha == '2':
            mostrar_livros()
        
        elif escolha == '3':
            print('Saindo do programa. Até mais!')
            break
        
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

if __name__ == '__main__':
    main()

    
