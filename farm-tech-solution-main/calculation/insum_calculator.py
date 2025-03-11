class InsumoCalculator:
    """
    Classe para calcular a quantidade necessária de insumos para uma área de plantio.
    """

    @staticmethod
    def calcular_insumo(quantidade_por_hectare, area):
        """
        Calcula a quantidade total de insumo necessária para uma determinada área de plantio.
        
        :param quantidade_por_hectare: Quantidade de insumo necessária por hectare (em unidades).
        :param area: Área de plantio (em hectares).
        :return: Quantidade total de insumo necessária.
        """
        return quantidade_por_hectare * area
