import math

class AreaCalculator:
    """
    Classe para calcular áreas de plantio com diferentes formas geométricas.
    """
    def __init__(self, cultura):
        self.cultura = cultura.capitalize()
        self.unidade = input(f"Digite a unidade de medida para o plantio da cultura {self.cultura} (ex: metros, centímetros): ").strip()
    
    def get_float_input(self, mensagem):
        """ Obtém entrada numérica validada do usuário. """
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("❌ Entrada inválida! Digite um número válido.")
    
    def calcular_quadrado(self):
        lado = self.get_float_input("Digite o comprimento do lado do quadrado: ")
        return lado ** 2
    
    def calcular_retangulo(self):
        base = self.get_float_input("Digite a base do retângulo: ")
        altura = self.get_float_input("Digite a altura do retângulo: ")
        return base * altura
    
    def calcular_circulo(self):
        raio = self.get_float_input("Digite o raio do círculo: ")
        return math.pi * (raio ** 2)
    
    def calcular_triangulo(self):
        base = self.get_float_input("Digite a base do triângulo: ")
        altura = self.get_float_input("Digite a altura do triângulo: ")
        return (base * altura) / 2
    
    def calcular_poligono_regular(self):
        n_lados = int(self.get_float_input("Digite o número de lados do polígono regular: "))
        comprimento_lado = self.get_float_input("Digite o comprimento de cada lado do polígono: ")
        return (n_lados * comprimento_lado ** 2) / (4 * math.tan(math.pi / n_lados))
    
    def calcular_trapezio(self):
        base1 = self.get_float_input("Digite o comprimento da primeira base do trapézio: ")
        base2 = self.get_float_input("Digite o comprimento da segunda base do trapézio: ")
        altura = self.get_float_input("Digite a altura do trapézio: ")
        return ((base1 + base2) * altura) / 2
    
    def calcular_area(self):
        """
        Permite ao usuário calcular a área de plantio com base na forma escolhida.
        """
        opcoes = {
            "1": ("Quadrado", self.calcular_quadrado),
            "2": ("Retângulo", self.calcular_retangulo),
            "3": ("Círculo", self.calcular_circulo),
            "4": ("Triângulo", self.calcular_triangulo),
            "5": ("Polígono Regular", self.calcular_poligono_regular),
            "6": ("Trapézio", self.calcular_trapezio)
        }
        
        print("\nEscolha o tipo de área de plantio para calcular:")
        for key, (nome, _) in opcoes.items():
            print(f"{key}️⃣ {nome}")
        
        escolha = input("Digite o número correspondente à forma: ").strip()
        
        if escolha in opcoes:
            nome_forma, funcao_calculo = opcoes[escolha]
            area = funcao_calculo()
            print(f"\n✅ A área de plantio do {nome_forma.lower()} para a cultura {self.cultura} é: {area:.2f} {self.unidade}²")
        else:
            print("❌ Opção inválida. Tente novamente.")
