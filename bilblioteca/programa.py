from funçoes import *

print("1 - Adicionar livro")
print("2 - Exibir todos os livros")
print("3 - Emprestar livro")
print("4 - Devolver livro")
print("0 - Sair")
op = input("o que deseja fazer? ")
listalivro = []
while True:
    if op == "0":
        print("SAINDO DO PROGRAMA....")
        break
    if op == "1":
        addlivro(listalivro)
        print("1 - Adicionar livro")
        print("2 - Exibir todos os livros")
        print("3 - Emprestar livro")
        print("4 - Devolver livro")
        print("0 - Sair")
        op = input("o que deseja fazer? ")
    elif op == "2":
        exibirlivro(listalivro)
        print("1 - Adicionar livro")
        print("2 - Exibir todos os livros")
        print("3 - Emprestar livro")
        print("4 - Devolver livro")
        print("0 - Sair")
        op = input("o que deseja fazer? ")
    elif op == "3":
        emprestar(listalivro)
        print("1 - Adicionar livro")
        print("2 - Exibir todos os livros")
        print("3 - Emprestar livro")
        print("4 - Devolver livro")
        print("0 - Sair")
        op = input("o que deseja fazer? ")
    elif op == "4":
        devolver(listalivro)
        print("1 - Adicionar livro")
        print("2 - Exibir todos os livros")
        print("3 - Emprestar livro")
        print("4 - Devolver livro")
        print("0 - Sair")
        op = input("o que deseja fazer? ")