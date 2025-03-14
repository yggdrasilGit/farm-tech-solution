from management.culture_manager import CultureManager
from calculation.area_calculator import AreaCalculator
from management.insum_manager import Insumo
from calculation.insum_calculator import InsumoCalculator

class Menu:
    """
    Classe responsável por exibir e gerenciar o menu principal.
    """
    def __init__(self):
        self.culture_manager = CultureManager()
        self.insumos = {}  # Dicionário para armazenar insumos cadastrados por cultura
        self.areas_plantio = {}  # Dicionário para armazenar áreas por cultura
        self.insumo = Insumo() # instancia insumo para cadastrar 

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
            print("7️⃣ Ver áreas de plantio cadastradas")
            print("8️⃣ Calcular insumo")
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
            elif opcao == "7":
                self.show_areas()
            elif opcao == "8":
                self.calcular_insumo()
            elif opcao == "0":
                print("👋 Saindo do programa. Até mais!")
                break
            else:
                print("❌ Opção inválida. Tente novamente.")

    def calculate_area(self):
        """Calcula a área de plantio em hectares para cada cultura escolhida."""
        if not self.culture_manager.cultura_escolhida:
            print("⚠️ Você precisa escolher as culturas primeiro.")
            return

        for cultura in self.culture_manager.cultura_escolhida:
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
                print("❌ Opção inválida. Voltando ao menu principal.")
                continue  # Volta para o início do loop

            # Salvando a área calculada no dicionário
            self.areas_plantio[cultura] = area
            print(f"🌱 A área de plantio para {cultura.capitalize()} é de {area:.2f} hectares.")

    def register_inputs(self):
        """Cadastra insumos para as culturas escolhidas."""
        if not self.culture_manager.cultura_escolhida:
            print("⚠️ Você precisa escolher as culturas primeiro.")
            return

        for cultura in self.culture_manager.cultura_escolhida:
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
            print(self.insumo.exibir_insumos())
    
    def show_areas(self):
        """Exibe as áreas de plantio calculadas para cada cultura."""
        if not self.areas_plantio:
            print("⚠️ Nenhuma área de plantio foi cadastrada ainda.")
            return

        print("\n📏 Áreas de plantio cadastradas:")
        for cultura, area in self.areas_plantio.items():
            print(f"🌱 Cultura: {cultura.capitalize()} - Área: {area:.2f} hectares")
    
    def calcular_insumo(self):
        """Calcula a quantidade necessária de insumos para cada cultura cadastrada."""
        if not self.areas_plantio:
            print("⚠️ Nenhuma área de plantio foi cadastrada ainda.")
            return

        if not self.insumos:
            print("⚠️ Nenhum insumo foi cadastrado ainda.")
            return

        for cultura, area in self.areas_plantio.items():
            if cultura not in self.insumos:
                print(f"⚠️ Nenhum insumo cadastrado para a cultura {cultura.capitalize()}.")
                continue
            
            print(f"\n📊 Calculando insumos para a cultura {cultura.capitalize()}...")
            insumo = self.insumos[cultura]
            
            for nome_insumo, quantidade_por_hectare in insumo.obter_insumos().items():
                quantidade_total = InsumoCalculator.calcular_insumo(quantidade_por_hectare, area)
                print(f"🔹 {nome_insumo}: {quantidade_total:.2f} unidades necessárias para {area:.2f} hectares.")
