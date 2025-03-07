import math

class AreaCalculator:
    """
    Classe para calcular áreas de plantio.
    O usuário pode escolher diferentes formas geométricas para o cálculo.
    """

    def calculate_area(self, cultura):
        """
        Permite ao usuário calcular a área de plantio com base na cultura escolhida.
        Cada cultura pode ter uma área de plantio específica.
        """
        # Perguntar a unidade de medida
        unidade = input(f"Digite a unidade de medida para o plantio da cultura {cultura.capitalize()} (ex: metros, centímetros): ").strip()

        # Perguntar o tipo de área a ser calculada
        print("\nEscolha o tipo de área de plantio para calcular:")
        print("1️⃣ Quadrado")
        print("2️⃣ Retângulo")
        print("3️⃣ Círculo")
        print("4️⃣ Triângulo")
        print("5️⃣ Polígono Regular")
        print("6️⃣ Trapézio")
        
        escolha_area = input("Digite o número correspondente à forma: ").strip()

        if escolha_area == "1":
            lado = float(input("Digite o comprimento do lado do quadrado: "))
            area = lado ** 2
            print(f"A área de plantio do quadrado para a cultura {cultura.capitalize()} é: {area} {unidade}²")
        elif escolha_area == "2":
            base = float(input("Digite a base do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            area = base * altura
            print(f"A área de plantio do retângulo para a cultura {cultura.capitalize()} é: {area} {unidade}²")
        elif escolha_area == "3":
            raio = float(input("Digite o raio do círculo: "))
            area = math.pi * (raio ** 2)
            print(f"A área de plantio do círculo para a cultura {cultura.capitalize()} é: {area:.2f} {unidade}²")
        elif escolha_area == "4":
            base = float(input("Digite a base do triângulo: "))
            altura = float(input("Digite a altura do triângulo: "))
            area = (base * altura) / 2
            print(f"A área de plantio do triângulo para a cultura {cultura.capitalize()} é: {area} {unidade}²")
        elif escolha_area == "5":
            n_lados = int(input("Digite o número de lados do polígono regular: "))
            comprimento_lado = float(input("Digite o comprimento de cada lado do polígono: "))
            area = (n_lados * comprimento_lado ** 2) / (4 * math.tan(math.pi / n_lados))
            print(f"A área de plantio do polígono regular para a cultura {cultura.capitalize()} é: {area:.2f} {unidade}²")
        elif escolha_area == "6":
            base1 = float(input("Digite o comprimento da primeira base do trapézio: "))
            base2 = float(input("Digite o comprimento da segunda base do trapézio: "))
            altura = float(input("Digite a altura do trapézio: "))
            area = ((base1 + base2) * altura) / 2
            print(f"A área de plantio do trapézio para a cultura {cultura.capitalize()} é: {area} {unidade}²")
        else:
            print("❌ Opção inválida. Tente novamente.")
