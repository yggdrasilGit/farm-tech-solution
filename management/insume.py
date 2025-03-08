class Insumo:
    """
    Classe para calcular os insumos necessários para uma cultura específica.
    """
    def __init__(self, cultura):
        self.cultura = cultura
        self.insumos = []

    def calcular_insumos(self):
        """Calcula a necessidade de insumos com base na cultura."""
        if self.cultura:
            fertilizante = input(f"Digite a quantidade de fertilizante necessária para {self.cultura.capitalize()} (kg/ha): ")
            pesticida = input(f"Digite a quantidade de pesticida necessária para {self.cultura.capitalize()} (L/ha): ")
            self.insumos.append(f"🌿 Fertilizante: {fertilizante} kg/ha")
            self.insumos.append(f"🛡️ Pesticida: {pesticida} L/ha")
        else:
            print("⚠️ Nenhuma cultura definida para cálculo de insumos.")
    
    def obter_insumos(self):
        """Retorna a lista de insumos calculados."""
        return self.insumos
