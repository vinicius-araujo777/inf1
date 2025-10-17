from operacoes import *

op = input("1: soma, 2: subtração, 3: multiplicação, 4:divisão, 5: sair da calculadora:")
while True:
    if op == "5":
        print("saindo .... volte sempre")
        break
    n1 = float(input("numero: "))
    n2 = float(input("numero: "))
    if op=="1":
        print(soma(n1,n2))
    elif op == "2":
        print(subtracao(n1,n2))
    elif op == "3":
        print(multiplicacao(n1,n2))
    elif op == "4":
        print(divisao(n1,n2))
    elif op == "5":
        break
    op = input("1: soma, 2: subtração, 3: multiplicação, 4:divisão, 5: sair da calculadora:")
    