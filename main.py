from input_data.culture_type import escolher_cultura

def menu():
    """
    Exibe o menu principal do programa e chama a função para escolher culturas.

    A função `escolher_cultura()` permite ao usuário selecionar duas culturas
    distintas para trabalhar e armazena a escolha.

    Returns:
        None
    """
    cultura = escolher_cultura()

if __name__ == "__main__":
    menu()
