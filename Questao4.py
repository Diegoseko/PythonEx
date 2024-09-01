
lista_livro = []
id_global = 0
#FUNCAO DE CADASTRO DE LIVRO, COLOCANDO OS VALORES DO DICIONARIO NA LISTA
def cadastrar_livro(id_global):
    livrosDic = {}
    livrosDic['id'] = id_global
    print(f"ID do Livro: {id_global} ")
    livrosDic['nome'] = input("Digite o nome do livro: ")
    livrosDic['autor'] = input("Digite o autor do livro: ")
    livrosDic['editora'] = input("Digite o editora do livro: ")
    lista_livro.append(livrosDic.copy())   
  
#CONSULTA DOS LIVROS CADASTRADOS, UTILIZA O FOR PARA LISTAR OS ITENS DA LISTA
def consultar_livro():
    while True:
        print('1 - Consultar Todos')
        print('2 - Consultar por ID')
        print('3 - Consultar por Autor')
        print('4 - Voltar ao menu')
        esc = int(input('Digite a opcao: '))
        if(esc != 1 and esc != 2 and esc != 3 and esc != 4):
            print("Opção inválida. Tente novamente.")
            continue    
        if(esc == 1):
            for livrosDic in lista_livro:
                print(f"ID do Livro: {livrosDic['id']}  Nome do Livro: {livrosDic['nome']}  Autor do Livro: {livrosDic['autor']} Editora do Livro: {livrosDic['editora']}  ")
        if(esc == 2):
            conID = int(input("Qual o ID do livro?"))
            for livrosDic in lista_livro:
                if(conID == livrosDic['id']):
                    print(f"ID do Livro: {livrosDic['id']}  Nome do Livro: {livrosDic['nome']}  Autor do Livro: {livrosDic['autor']} Editora do Livro: {livrosDic['editora']}  ")
                else:
                    print('Livro não encontrado')
                    continue
        if(esc == 3):
            conAutor = input("Qual o nome do Autor do livro?")
            for livrosDic in lista_livro:
                if(conAutor == livrosDic['autor']):
                    print(f"ID do Livro: {livrosDic['id']}  Nome do Livro: {livrosDic['nome']}  Autor do Livro: {livrosDic['autor']} Editora do Livro: {livrosDic['editora']}  ")
                else:
                    print('Livro não encontrado')
                    continue
        if(esc == 4):
            break

#REMOVE OS ITEMS PELO IDENTIFICADOR ID
def remover_livro():
    remID = int(input("Qual o ID do livro?"))
    for livrosDic in lista_livro:
        if(remID == livrosDic['id']):
            lista_livro.remove(livrosDic)
        print('Livro removido com sucesso!')

#MENU MAIN
while True:
    print("BEM VINDO A LIVRARIA DO DIEGO OSEKO")
    print("1 - CADASTRAR LIVRO")
    print("2 - CONSULTAR LIVRO")
    print("3 - REMOVER LIVRO")
    print("4 - SAIR")
    opcao = int(input('Digite a opcao: '))
    if(opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4):
        print("Opcao invalida! Tente novamente.")
        continue
    if(opcao == 1):
        cadastrar_livro(id_global)
        id_global = id_global + 1
        print("Livro cadastrado com sucesso!")
    elif(opcao == 2):
        consultar_livro()
    elif(opcao == 3):
        remover_livro()
    elif(opcao == 4):
        print("Programa encerrado.")
        break
