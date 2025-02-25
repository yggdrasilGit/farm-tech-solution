



def escolher_cultura():
    culturas = []
    while len(culturas) < 2:
        cultura = input("Digite a cultura que deseja trabalhar (soja/milho ou qualquer outra): ").lower()
        if cultura not in culturas:
            culturas.append(cultura)
        else:
            print("Cultura já escolhida. Por favor, escolha uma cultura diferente.")
    print(f"As culturas escolhidas foram: {culturas}")
    return culturas
