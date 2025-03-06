# coding: utf-8
from input_data.culture_type import SelecaoCultura

def menu():
    """
    Exibe o menu principal do programa e chama a função para escolher culturas.

    A função `escolher_cultura()` permite ao usuário selecionar duas culturas
    distintas para trabalhar e armazena a escolha.

    Returns:
        None
    """
    # Cria uma instância de SelecaoCultura
    selecao = SelecaoCultura()
    
    # Chama o método escolher_cultura da instância
    selecao.escolher_cultura()

if __name__ == "__main__":
    menu()
