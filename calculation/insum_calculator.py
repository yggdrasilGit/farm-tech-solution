from calculation.area_calculator import AreaCalculator
from management.insum_manager import Insumo
from management.culture_manager import CultureManager

class InsumoCalculator(CultureManager):
    """
    Classe para calcular a quantidade total de insumos necessária para o plantio,
    considerando a área calculada em hectares e valores médios de consumo por hectare.
    """
    
    

    # Base de dados fictícia de consumo médio por hectare para cada insumo
    consumo_medio_por_ha = {
        "adubo": 200,  # kg/ha
        "sementes": 50,  # kg/ha
        "herbicida": 2,  # litros/ha
        "inseticida": 1.5,  # litros/ha
        "calcário": 500  # kg/ha
    }

    def __init__(self):
        """
        Inicializa o calculador de insumos com um dicionário de áreas por cultura.
        """
        self.cultura = CultureManager()
        self.insumo = Insumo()

    def adicionar_cultura(self, cultura, tipo_area, *params):
        """
        Adiciona uma cultura e calcula sua área correspondente.

        :param cultura: Nome da cultura (ex: soja, milho)
        :param tipo_area: Tipo de cálculo de área (ex: quadrado, retângulo)
        :param params: Parâmetros necessários para o cálculo da área
        """
        metodos_calculo = {
            "quadrado": AreaCalculator.calcular_quadrado,
            "retangulo": AreaCalculator.calcular_retangulo,
            "circulo": AreaCalculator.calcular_circulo,
            "triangulo": AreaCalculator.calcular_triangulo,
            "poligono": AreaCalculator.calcular_poligono_regular,
            "trapezio": AreaCalculator.calcular_trapezio
        }

        if tipo_area in metodos_calculo:
            self.areas_por_cultura[cultura] = metodos_calculo[tipo_area](*params)
        else:
            print(f"⚠️ Tipo de área '{tipo_area}' não reconhecido.")

    def calcular_consumo_total(self, tipo_insumo):
        """
        Calcula a quantidade total necessária de um insumo para todas as culturas escolhidas.

        :param tipo_insumo: Nome do insumo a ser calculado.
        :return: Quantidade total necessária do insumo para todas as culturas.
        """
        if tipo_insumo not in self.consumo_medio_por_ha:
            print(f"⚠️ Insumo '{tipo_insumo}' não encontrado na base de dados.")
            return None

        consumo_total = sum(
            area * self.consumo_medio_por_ha[tipo_insumo]
            for area in self.areas_por_cultura.values()
        )

        return consumo_total
