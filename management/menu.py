from management.culture_manager import CultureManager
from calculation.area_calculator import AreaCalculator
from management.insum_manager import Insumo

class Menu:
    """
    Classe responsável por exibir e gerenciar o menu principal.
    """
    def __init__(self):
        self.culture_manager = CultureManager()
        self.insumo = Insumo()
        self.insumos = {}  # Dicionário para armazenar insumos cadastrados por cultura

    def display(self):
        """Exibe o menu principal e gerencia as opções do usuário."""
        while True:
            print("\n📌 MENU PRINCIPAL")
            print("1️⃣ Escolher culturas para trabalhar")
            print("2️⃣ Cadastrar novas culturas")
            print("3️⃣ Ver culturas cadastradas")
            print("4️⃣ Calcular área de plantio")
            print("5️⃣ Cadastrar insumos para culturas")
            print("6️⃣ Ver insumos cadastrados")
            print("0️⃣ Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.culture_manager.select_culture()
            elif opcao == "2":
                self.culture_manager.register_culture()
            elif opcao == "3":
                self.culture_manager.registered_cultures()
            elif opcao == "4":
                self.calculate_area()
            elif opcao == "5":
                self.register_inputs()
            elif opcao == "6":
                self.show_inputs()
            elif opcao == "0":
                print("👋 Saindo do programa. Até mais!")
                break
            else:
                print("❌ Opção inválida. Tente novamente.")

    def calculate_area(self):
        """Calcula a área de plantio em hectares para cada cultura escolhida."""
        if not self.culture_manager.culturas_escolhidas:
            print("⚠️ Você precisa escolher as culturas primeiro.")
            return

        for cultura in self.culture_manager.culturas_escolhidas:
            print(f"\nCalculando área para a cultura: {cultura.capitalize()}")

            print("Escolha a forma da área de plantio:")
            print("1️⃣ Quadrado")
            print("2️⃣ Retângulo")
            print("3️⃣ Círculo")
            print("4️⃣ Triângulo")
            print("5️⃣ Polígono Regular")
            print("6️⃣ Trapézio")

            opcao = input("Digite o número da opção: ").strip()

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
                return

            print(f"🌱 A área de plantio para {cultura.capitalize()} é de {area:.2f} hectares.")

    def register_inputs(self):
        """Cadastra insumos para as culturas escolhidas."""
        if not self.culture_manager.culturas_escolhidas:
            print("⚠️ Você precisa escolher as culturas primeiro.")
            return

        for cultura in self.culture_manager.culturas_escolhidas:
            print(f"\nCadastrando insumos para a cultura: {cultura.capitalize()}")
            self.insumo.cadastrar_insumos()
            self.insumos[cultura] = self.insumo  # Armazena o objeto Insumo por cultura

    def show_inputs(self):
        """Exibe os insumos cadastrados para cada cultura."""
        if not self.insumos:
            print("⚠️ Nenhum insumo foi cadastrado ainda.")
            return

        for cultura, insumo in self.insumos.items():
            print(f"\n📋 Insumos cadastrados para a cultura {cultura.capitalize()}:")
            print(f"\n Os insumos são {self.insumo.obter_insumos()}")
            
