from tabulate import tabulate

cardapio = [
    {"id": 1, "nome": "Hambúrguer", "preco": 12.5},
    {"id": 2, "nome": "Pizza", "preco": 30},
    {"id": 3, "nome": "Refrigerante", "preco": 5}
]


lista_pedidos = []

def exibir_cardapio(cardapio):
    print(tabulate(cardapio, headers="keys", tablefmt="grid"))
    
def adicionar(cardapio,lista_pedidos):
    id = int(input('digite o id do produto escolhido:'))
    for i in cardapio:
        if i["id"] == id:
            escolha = i
    quantidade = int(input('quantidade:'))
    item = escolha["nome"]
    preco = escolha['preco']
    preco_total= quantidade*preco
    pedido = {
        'item':item,
        'quantidade':quantidade,
        'preco':preco_total
    }
    lista_pedidos.append(pedido)

def exibir_pedidos(lista_pedidos):
    print(tabulate(lista_pedidos, headers='keys',tablefmt='grid'))
    total = sum([p['preco']for p in lista_pedidos])
    print(f"TOTAL: R$ {total:.2f}")
    
def remover(lista_pedidos):
    item = input('digite o nome do pedido que quer retirar:')
    for i in lista_pedidos:
        if i['item'] == item:
            lista_pedidos.remove(i)
        else:
            print('você não fez esse pedido.')

def menu():
    print("""
        1 - Ver cardápio
        2 - Adicionar item ao pedido
        3 - Ver pedido
        4 - Remover item
        0 - Finalizar """)
    

