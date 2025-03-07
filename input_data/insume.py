class Insumo:
    def __init__(self, cultura):
        self.cultura = cultura

    def calcular_insumos(self):
        """
        Placeholder method to calculate inputs needed for planting.
        """
        print(f"\nCalculando insumos para a cultura {self.cultura.capitalize()}...\n")
        # Exemplo fictício de insumos
        insumos = [
            f"🌾 Sementes para {self.cultura.capitalize()}: 10 kg/ha",
            f"💧 Fertilizante para {self.cultura.capitalize()}: 50 kg/ha",
            f"🌱 Defensivo para {self.cultura.capitalize()}: 5 L/ha"
        ]
        return insumos

    def obter_insumos(self):
        """
        Returns the calculated inputs for the selected culture.
        """
        return self.calcular_insumos()
