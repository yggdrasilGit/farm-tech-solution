class InsumoCalculator:
    """
    Classe para calcular a quantidade necessária de insumos para uma área de plantio.
    """
    def __init__(self, hectare, quantidade_insumo):
        self.hectare = float(hectare)
        self.quantidade_insumo = float(quantidade_insumo)

    def calcular_insumo(self):
        """
        Calcula a quantidade total de insumo necessária para uma determinada área de plantio.
        
        :return: Quantidade total de insumo necessária.
        """
        quantidade_insumo_hectare = self.hectare * self.quantidade_insumo
        return quantidade_insumo_hectare

