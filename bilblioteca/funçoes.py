from tabulate import tabulate


def addlivro(listalivro):
    titulo = input("titulo do livro: ")
    autor = input("autor do livro: ")
    livro1 = {
        "titulo": titulo,
        "autor": autor,
        "status": 'disponivel'
    }
    listalivro.append(livro1)

def emprestar(listalivro):
    titulo = input("livro que quer pegar: ")
    for i in listalivro:
        if i in listalivro:
            if i['titulo'] == titulo:
                if i['status'] == 'disponivel':
                    i['status'] = 'emprestado'
                else:
                    print("o livro ja foi pego")
            elif i['titulo'] != titulo:
                print("O LIVRO NÃO EXISTE NA BIBLIOTECA !!!!!!!")
                print(" ")

def devolver(listalivro):
    titulo = input("livro que quer devolver: ")
    for i in listalivro:
        if i['titulo'] == titulo:
            if i['status'] == 'emprestado':
                i['status'] = 'disponivel'
            else:
                print("Esse livro já está disponivel")
        elif i['titulo'] != titulo:
                print("O LIVRO NÃO EXISTE NA BIBLIOTECA !!!!!!!")
                print(" ")


def exibirlivro(listalivro):
    table = tabulate(
        listalivro,
        headers='keys',
        tablefmt='grid' 
    )
    print(table)