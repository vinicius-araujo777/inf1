from funcao import *

listaviagens = []

while True:
    menu()  # Mostra o menu
    op = input("Escolha uma opção: ")

    if op == "0":
        print("Saindo do programa...")
        break

    if op == "1":
        registro_viagens(listaviagens)
    elif op == "2":
        exibir_viagens(listaviagens)
    elif op == "3":
        resultados = buscar_por_motorista(listaviagens, "")  
        print(resultados)
    elif op == "4":
        if listaviagens:  
            viagem_cara = viagem_mais_cara(listaviagens)
            print("Viagem com maior consumo de combustível:", viagem_cara)
        else:
            print("Não há viagens registradas ainda!")
    elif op == "5":
        if listaviagens:  
            media = media_consumo(listaviagens)
            print(f"Média de consumo médio de todas as viagens: {media:.2f}")
        else:
            print("Não há viagens registradas ainda!")
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")