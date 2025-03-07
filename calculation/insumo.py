from calculation.area_calculator import AreaCalculator

class Insumo:
    """
    Classe base para cada tipo de insumo.
    """
    def __init__(self, tipo, quantidade_por_metro):
        self.tipo = tipo
        self.quantidade_por_metro = quantidade_por_metro

    def calcular(self, area):
        return area * self.quantidade_por_metro


class InsumoCultura:
    """
    Classe para armazenar os insumos de uma cultura específica.
    """
    def __init__(self, cultura):
        self.cultura = cultura.lower()
        self.insumos = []
        
        # Dicionário para armazenar os tipos de insumos das culturas
        self.dados_cultura = {
            'milho': {
                'sementes': 3.0,  # sementes por metro quadrado
                'fertilizante': 0.2,  # kg de fertilizante por metro quadrado
                'defensivo': 0.05,  # L de defensivo por metro quadrado
                'chuva_minima': 150.0  # mm de chuva mínima por mês
            },
            'soja': {
                'sementes': 2.5,
                'fertilizante': 0.15,
                'defensivo': 0.04,
                'chuva_minima': 120.0
            },
            'cana de açúcar': {
                'sementes': 1.5,
                'fertilizante': 0.25,
                'defensivo': 0.06,
                'chuva_minima': 100.0
            },
            'café': {
                'sementes': 3.0,
                'fertilizante': 0.18,
                'defensivo': 0.07,
                'chuva_minima': 180.0
            }
        }

    def adicionar_insumos(self, tipo, quantidade_por_metro):
        """
        Adiciona um tipo de insumo à lista de insumos da cultura.
        """
        insumo = Insumo(tipo, quantidade_por_metro)
        self.insumos.append(insumo)

    def calcular_insumos(self, area):
        """
        Calcula todos os insumos necessários com base na área de plantio.
        """
        resultado_insumos = []
        
        if self.cultura in self.dados_cultura:
            dados = self.dados_cultura[self.cultura]

            # Para cada tipo de insumo (sementes, fertilizante, defensivo), cria-se o insumo e calcula-se a quantidade necessária
            for tipo, quantidade_por_metro in dados.items():
                if tipo != 'chuva_minima':  # A chuva mínima não precisa ser calculada com base na área
                    self.adicionar_insumos(tipo, quantidade_por_metro)
            
            # Calculando os insumos
            for insumo in self.insumos:
                quantidade = insumo.calcular(area)
                resultado_insumos.append(f"Quantidade de {insumo.tipo} para {self.cultura}: {quantidade} unidades")
            
            # Adiciona a quantidade mínima de chuva
            resultado_insumos.append(f"Quantidade mínima de chuva para {self.cultura}: {dados['chuva_minima']} mm/mês")
        else:
            resultado_insumos.append("Cultura não implementada para cálculo de insumos.")
        
        return resultado_insumos


class InsumoCalculador(AreaCalculator):
    """
    Classe principal para calcular os insumos necessários para uma cultura.
    """
    def __init__(self, cultura):
        super().__init__()  # Chama o construtor da classe pai (AreaCalculator)
        self.cultura = cultura.lower()
        self.insumos_cultura = InsumoCultura(self.cultura)

    def calcular_insumos(self):
        """
        Calcula os insumos necessários com base na área de plantio.
        """
        area = self.calculate_area(self.cultura)
        return self.insumos_cultura.calcular_insumos(area)
