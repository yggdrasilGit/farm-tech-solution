from management.culture_manager import CultureManager
from calculation.area_calculator import AreaCalculator
from calculation.insumo import Insumo

class Menu:
    """
    Classe responsável por exibir e gerenciar o menu principal.
    """
    def __init__(self):
        self.culture_manager = CultureManager()
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
                print("\ud83d\udc4b Saindo do programa. Até mais!")
                break
            else:
                print("❌ Opção inválida. Tente novamente.")

    def calculate_area(self):
        """Calcula a área para cada cultura escolhida."""
        if not self.culture_manager.culturas_escolhidas:
            print("⚠️ Você precisa escolher as culturas primeiro.")
            return

        unidade = input("Digite a unidade de medida para o plantio (ex: metros, centímetros): ").strip()

        for cultura in self.culture_manager.culturas_escolhidas:
            print(f"\nCalculando área para a cultura: {cultura.capitalize()}")
            area_calculator = AreaCalculator(cultura, unidade)
            area_calculator.calcular_area()

    def register_inputs(self):
        """Cadastra insumos para as culturas escolhidas."""
        if not self.culture_manager.culturas_escolhidas:
            print("⚠️ Você precisa escolher as culturas primeiro.")
            return

        for cultura in self.culture_manager.culturas_escolhidas:
            print(f"\nCadastrando insumos para a cultura: {cultura.capitalize()}")
            insumo = Insumo(cultura)
            insumo.cadastrar_insumos()
            self.insumos[cultura] = insumo  # Armazena o objeto Insumo por cultura

    def show_inputs(self):
        """Exibe os insumos cadastrados para cada cultura."""
        if not self.insumos:
            print("⚠️ Nenhum insumo foi cadastrado ainda.")
            return

        for cultura, insumo in self.insumos.items():
            print(f"\nInsumos cadastrados para a cultura {cultura.capitalize()}:")
            insumo.listar_insumos()
