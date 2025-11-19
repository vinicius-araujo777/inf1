from funcaoCardapio import *

menu()
op = input('o que deseja fazer? ')
while True:
    if op == '0':
        print('saindo do programa...')
        break
    if op == '1':
        exibir_cardapio(cardapio)
    if op == '2':
        adicionar(cardapio,lista_pedidos)
    if op == '3':
        exibir_pedidos(lista_pedidos)
    if op == '4':
        remover(lista_pedidos)
    op = input('o que deseja fazer? ')


