from funcao import*
from colorama import Fore, Style, init
init()
g = Fore.GREEN
r = Fore.RED	
y = Fore.YELLOW	
reset = Style.RESET_ALL

print("1-Cadastrar aluno e notas    2-Exibir relatório    0-SAIR ")
op = input("o que voce deseja fazer ? ")

while True:
    if op == "0":
        break

    if op == "1":
        lnalunos = []
        lnotas = []
        nome = input("nome do aluno: ")
        for i in range(3):
            lnotas.append(int(input("nota do aluno: ")))
        notadic = {nome:[lnotas]}
        lnalunos.append(notadic)

    elif op == "2":
        print("a media do aluno foi")
        print(media(lnotas))
        mediaa = media(lnotas)
        print("De acordo com as notas o aluno esta:")
        print(vermed(mediaa))

    print("1-Cadastrar aluno e notas    2-Exibir relatório    0-SAIR ")
    op = input("o que voce deseja fazer ? ")
