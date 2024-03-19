from database import Database
from livroModel import livroModel

db = Database(database="relatorio_5", collection="livros")
livroModel = livroModel(database=db)

controle = True
#Menu
while controle:
    print('1 -para criar \n'
          '2- informações Livro\n'
          '3- Update\n'
          '4- deletar Livro\n'
          '5- Sair')
    op = int(input("digite a opcao: "))
    if(op == 1):
        titulo = input("informe o Titulo: ")
        autor = input("informe o autor: ")
        ano = int(input("informe o ano: "))
        preco = float(input("informe o preco com a casa decimal: "))
        livroModel.create_livro(titulo, autor, ano, preco)
    if (op == 2):
        id = input("informe o id: ")
        livroModel.read_livro_by_id(id)
    if (op == 3):
        id = input("informe o id: ")
        titulo = input("informe o Titulo: ")
        autor = input("informe o autor: ")
        ano = int(input("informe o ano: "))
        preco = float(input("informe o preco com a casa decimal: "))
        livroModel.update_livro(id,titulo,autor,ano,preco)
    if(op == 4):
        id = input("informe o id:")
        livroModel.delete_livro(id)
    if (op == 5):
        controle = False
