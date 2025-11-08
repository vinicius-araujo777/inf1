from tabulate import tabulate

def registro_viagens(listaviagens):
    motorista = input("Digite o nome do motorista: ")
    destino = input("Digite o destino da viagem: ")
    distancia = float(input("Digite a distância da viagem em km: "))
    conbustivel = float(input("Digite o consumo de combustível em litros: "))
    consumo_medio = distancia / conbustivel
    viagem ={
        "motorista": motorista,
        "destino": destino,
        "distancia": distancia,
        "conbustivel": conbustivel,
        "consumo_medio": consumo_medio
    }
    listaviagens.append(viagem)

def exibir_viagens(listaviagens):
    print(tabulate(listaviagens, headers="keys", tablefmt="grid"))
    
def buscar_por_motorista(listaviagens, motorista):
    motorista = input("Digite o nome do motorista para busca: ")
    resultados = []
    for viagem in listaviagens:
        if viagem["motorista"] == motorista:
            resultados.append(viagem)
    return resultados

def viagem_mais_cara(listaviagens):
    viagem_maior_consumo = listaviagens[0]
    for viagem in listaviagens:
        if viagem["conbustivel"] > viagem_maior_consumo["conbustivel"]:
            viagem_maior_consumo = viagem
    return viagem_maior_consumo

def media_consumo(listaviagens):
    total_consumo = 0
    for viagem in listaviagens:
        total_consumo += viagem["consumo_medio"]
    media = total_consumo / len(listaviagens)
    return media

def menu():
    print("1. Registrar nova viagem")
    print("2. Exibir todas as viagens")
    print("3. Buscar viagens por motorista")
    print("4. Listar viagem mais cara")
    print("5. Calcular média de consumo médio de todas as viagens")
    print("0. Sair")