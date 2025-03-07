from calculation.area_calculator import AreaCalculator

class Insumo(AreaCalculator):
    """
    Classe para calcular a quantidade de insumos necessários com base na área de plantio.
    Herda de AreaCalculator para calcular a área.
    """

    def __init__(self, cultura):
        super().__init__()  # Chama o construtor da classe pai (AreaCalculator)
        self.cultura = cultura.lower()
        self.insumos = []
        
        # Dicionário para armazenar as informações de insumos das culturas
        self.dados_cultura = {
            'milho': {
                'sementes_por_metro': 3.0,
                'fertilizante_por_metro': 0.2,
                'defensivo_por_metro': 0.05,
                'chuva_minima': 150.0
            },
            'soja': {
                'sementes_por_metro': 2.5,
                'fertilizante_por_metro': 0.15,
                'defensivo_por_metro': 0.04,
                'chuva_minima': 120.0
            },
            'cana de açúcar': {
                'sementes_por_metro': 1.5,
                'fertilizante_por_metro': 0.25,
                'defensivo_por_metro': 0.06,
                'chuva_minima': 100.0
            },
            'café': {
                'sementes_por_metro': 3.0,
                'fertilizante_por_metro': 0.18,
                'defensivo_por_metro': 0.07,
                'chuva_minima': 180.0
            }
        }

    def calcular_insumos(self):
        """
        Calcula os insumos necessários com base na área de plantio.
        """
        # Calculando a área de plantio primeiro
        area = self.calculate_area(self.cultura)
        
        # Verifica se a cultura está registrada no dicionário
        if self.cultura in self.dados_cultura:
            dados = self.dados_cultura[self.cultura]
            
            # Calcula os insumos com base na área e dados da cultura
            self.insumos.append(f"Quantidade de sementes para {self.cultura}: {area * dados['sementes_por_metro']} sementes")
            self.insumos.append(f"Quantidade de fertilizante para {self.cultura}: {area * dados['fertilizante_por_metro']} kg")
            self.insumos.append(f"Quantidade de defensivo para {self.cultura}: {area * dados['defensivo_por_metro']} L")
            self.insumos.append(f"Quantidade mínima de chuva para {self.cultura}: {dados['chuva_minima']} mm/mês")
        else:
            self.insumos.append("Cultura não implementada para cálculo de insumos.")
    
    def obter_insumos(self):
        """
        Retorna a lista de insumos calculados.
        """
        return self.insumos
