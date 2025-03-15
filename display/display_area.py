from calculation.area_calculator import AreaCalculator

class DisplayAreaCalculator():
    """
    Classe responsável mandar as informacoes para o menu principal.
    """
    def __init__(self, cultura):
       self.culture_manager = cultura
       self.areas_plantio = {}  # Dicionário para armazenar áreas por cultura
       self.area = []

    
    def calculate_area(self):
        """Calcula a área de plantio em hectares para cada cultura escolhida."""
        if not self.culture_manager:
            print(self.culture_manager)
            print("⚠️ Você precisa escolher as culturas primeiro.")
            return

        for cultura in self.culture_manager:
            print(f"\nCalculando área para a cultura: {cultura.capitalize()}")

            print("Escolha a forma da área de plantio:")
            print("1️⃣ Quadrado")
            print("2️⃣ Retângulo")
            print("3️⃣ Círculo")
            print("4️⃣ Triângulo")
            print("5️⃣ Polígono Regular")
            print("6️⃣ Trapézio")

            opcao = input("Digite o número da opção: ").strip()

            area = 0
            if opcao == "1":
                lado = float(input("Digite o lado do quadrado (km): "))
                area = AreaCalculator.calcular_quadrado(lado)
            elif opcao == "2":
                base = float(input("Digite a base do retângulo (km): "))
                altura = float(input("Digite a altura do retângulo (km): "))
                area = AreaCalculator.calcular_retangulo(base, altura)
            elif opcao == "3":
                raio = float(input("Digite o raio do círculo (km): "))
                area = AreaCalculator.calcular_circulo(raio)
            elif opcao == "4":
                base = float(input("Digite a base do triângulo (km): "))
                altura = float(input("Digite a altura do triângulo (km): "))
                area = AreaCalculator.calcular_triangulo(base, altura)
            elif opcao == "5":
                n_lados = int(input("Digite o número de lados do polígono regular: "))
                comprimento_lado = float(input("Digite o comprimento de cada lado (km): "))
                area = AreaCalculator.calcular_poligono_regular(n_lados, comprimento_lado)
            elif opcao == "6":
                base1 = float(input("Digite a base maior do trapézio (km): "))
                base2 = float(input("Digite a base menor do trapézio (km): "))
                altura = float(input("Digite a altura do trapézio (km): "))
                area = AreaCalculator.calcular_trapezio(base1, base2, altura)
            else:
                print("❌ Opção inválida. Tente novamente.")
                continue  # Volta para o início do loop

            # Salvando a área calculada no dicionário
            self.areas_plantio[cultura] = area
            print(f"🌱 A área de plantio para {cultura.capitalize()} é de {area:.2f} hectares.")

    def show_areas(self):
        """Exibe as áreas de plantio calculadas para cada cultura."""
        if not self.areas_plantio:
            print("⚠️ Nenhuma área de plantio foi cadastrada ainda.")
            return

        print("\n📏 Áreas de plantio cadastradas:")
        for cultura, area in self.areas_plantio.items():
            print(area)
            self.area.append(area)
            print(self.area)
            print(f"🌱 Cultura: {cultura.capitalize()} - Área: {area:.2f} hectares")