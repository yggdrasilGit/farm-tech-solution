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

            
    # def __init__(self, hectare, quantidade_insumo):
    #     self.hectare = float(hectare)
    #     self.quantidade_insumo = float(quantidade_insumo)

    # def calcular_insumo(self):
    #     """
    #     Calcula a quantidade total de insumo necessária para uma determinada área de plantio.
        
    #     :return: Quantidade total de insumo necessária.
    #     """
    #     quantidade_insumo_hectare = self.hectare * self.quantidade_insumo
    #     return quantidade_insumo_hectare

