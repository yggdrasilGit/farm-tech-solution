import math

class AreaCalculator:
    """
    Classe para calcular áreas de plantio com diferentes formas geométricas.
    Entrada: km
    Saída: hectares (ha)
    """
    
    @staticmethod
    def calcular_quadrado(lado_km):
        area_km2 = lado_km ** 2
        return area_km2 * 100  # 1 km² = 100 ha
    
    @staticmethod
    def calcular_retangulo(base_km, altura_km):
        area_km2 = base_km * altura_km
        return area_km2 * 100  
    
    @staticmethod
    def calcular_circulo(raio_km):
        area_km2 = math.pi * (raio_km ** 2)
        return area_km2 * 100  
    
    @staticmethod
    def calcular_triangulo(base_km, altura_km):
        area_km2 = (base_km * altura_km) / 2
        return area_km2 * 100  
    
    @staticmethod
    def calcular_poligono_regular(n_lados, comprimento_lado_km):
        area_km2 = (n_lados * comprimento_lado_km ** 2) / (4 * math.tan(math.pi / n_lados))
        return area_km2 * 100  
    
    @staticmethod
    def calcular_trapezio(base1_km, base2_km, altura_km):
        area_km2 = ((base1_km + base2_km) * altura_km) / 2
        return area_km2 * 100  
    

# Exemplo de uso:
if __name__ == "__main__":
    print("Área de um quadrado de 2 km de lado:", AreaCalculator.calcular_quadrado(2), "ha")
    print("Área de um retângulo de 3 km x 4 km:", AreaCalculator.calcular_retangulo(3, 4), "ha")
    print("Área de um círculo de 1 km de raio:", AreaCalculator.calcular_circulo(1), "ha")
    print("Área de um triângulo de base 2 km e altura 3 km:", AreaCalculator.calcular_triangulo(2, 3), "ha")
    print("Área de um pentágono regular de lado 1 km:", AreaCalculator.calcular_poligono_regular(5, 1), "ha")
    print("Área de um trapézio com bases 2 km e 3 km, altura 4 km:", AreaCalculator.calcular_trapezio(2, 3, 4), "ha")
