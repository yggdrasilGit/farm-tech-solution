class InsumoCalculator:
    """
    Classe para calcular a quantidade necessária de insumos para uma área de plantio.

    """

    @staticmethod
    def calcular_insumo(insumo, area):
        resultado = {}
        for item in insumo.insumos:
            quantidade_total = float(item["quantidade"]) * area
            resultado[item["nome"]] = f"{quantidade_total} {item['unidade']}"
