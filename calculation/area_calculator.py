import math

class AreaCalculator:
    """
    Classe para calcular áreas de plantio.
    O usuário pode escolher diferentes formas geométricas para o cálculo.
    """
    
    def __init__(self):
        self.unidade = ""
    
    def solicitar_medida(self, mensagem):
        """Solicita ao usuário uma medida numérica válida."""
        while True:
            try:
                valor = float(input(mensagem))
                if valor > 0:
                    return valor
                else:
                    print("⚠️ O valor deve ser maior que zero.")
            except ValueError:
                print("❌ Entrada inválida. Digite um número válido.")
    
    def calculate_area(self, cultura):
        """
        Permite ao usuário calcular a área de plantio com base na cultura escolhida.
        """
        self.unidade = input(f"Digite a unidade de medida para o plantio da cultura {cultura.capitalize()} (ex: metros, centímetros): ").strip()

        formas = {
            "1": ("Quadrado", self.area_quadrado),
            "2": ("Retângulo", self.area_retangulo),
            "3": ("Círculo", self.area_circulo),
            "4": ("Triângulo", self.area_triangulo),
            "5": ("Polígono Regular", self.area_poligono_regular),
            "6": ("Trapézio", self.area_trapezio)
        }

        print("\nEscolha o tipo de área de plantio para calcular:")
        for key, (nome, _) in formas.items():
            print(f"{key}️⃣ {nome}")
        
        escolha = input("Digite o número correspondente à forma: ").strip()
        
        if escolha in formas:
            nome, funcao = formas[escolha]
            area = funcao()
            print(f"A área de plantio do {nome.lower()} para a cultura {cultura.capitalize()} é: {area:.2f} {self.unidade}²")
        else:
            print("❌ Opção inválida. Tente novamente.")
    
    def area_quadrado(self):
        lado = self.solicitar_medida("Digite o comprimento do lado do quadrado: ")
        return lado ** 2
    
    def area_retangulo(self):
        base = self.solicitar_medida("Digite a base do retângulo: ")
        altura = self.solicitar_medida("Digite a altura do retângulo: ")
        return base * altura
    
    def area_circulo(self):
        raio = self.solicitar_medida("Digite o raio do círculo: ")
        return math.pi * (raio ** 2)
    
    def area_triangulo(self):
        base = self.solicitar_medida("Digite a base do triângulo: ")
        altura = self.solicitar_medida("Digite a altura do triângulo: ")
        return (base * altura) / 2
    
    def area_poligono_regular(self):
        n_lados = int(self.solicitar_medida("Digite o número de lados do polígono regular: "))
        comprimento_lado = self.solicitar_medida("Digite o comprimento de cada lado do polígono: ")
        return (n_lados * comprimento_lado ** 2) / (4 * math.tan(math.pi / n_lados))
    
    def area_trapezio(self):
        base1 = self.solicitar_medida("Digite o comprimento da primeira base do trapézio: ")
        base2 = self.solicitar_medida("Digite o comprimento da segunda base do trapézio: ")
        altura = self.solicitar_medida("Digite a altura do trapézio: ")
        return ((base1 + base2) * altura) / 2

# Exemplo de uso:
if __name__ == "__main__":
    calculadora = AreaCalculator()
    cultura = input("Digite o nome da cultura para o plantio: ")
    calculadora.calculate_area(cultura)

