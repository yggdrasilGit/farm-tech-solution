


def escolher_cultura():
    while True:
        cultura = input("Digite a cultura que deseja trabalhar (soja/milho): ").lower()
        if cultura in ["soja", "milho"]:
            return cultura
        print("Cultura inválida! Escolha entre soja e milho.")