from ..display.display_meteriologica import Cidade

def informacao_meteorologicas():
    nome_cidade = input('digite o nome da cidade: ')
    cidade = Cidade(nome_cidade)
    cidade.mostrar_cidade()

informacao_meteorologicas()


