from management.culture_manager import CultureManager
from management.enterprise_name import EnterpriseName
#from calculation.area_calculator import AreaCalculator
from calculation.insumo import Insumo

class Menu:
    """
    Classe responsável por exibir e gerenciar o menu principal.
    """
    def __init__(self):
        self.culture_manager = CultureManager()
     #   self.area_calculator = AreaCalculator()

    def display(self):
        """Exibe o menu principal e gerencia as opções do usuário."""
        while True:

            print("\n📌 MENU PRINCIPAL")
            print("1️⃣ Escolher culturas para trabalhar")
            print("2️⃣ Cadastrar novas culturas")
            print("3️⃣ Ver culturas cadastradas")
            print("4️⃣ Calcular área de plantio")
            print("5️⃣ Calcular insumos necessários")
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
                self.calculate_inputs()
            elif opcao == "0":
                print("👋 Saindo do programa. Até mais!")
                break
            else:
                print("❌ Opção inválida. Tente novamente.")

    def calculate_area(self):
        """Calcula a área para cada cultura escolhida."""
        if not self.culture_manager.culturas_escolhidas:
            print("⚠️ Você precisa escolher as culturas primeiro.")
            return
        
        for cultura in self.culture_manager.culturas_escolhidas:
            print(f"\nCalculando área para a cultura: {cultura.capitalize()}")
            self.area_calculator.calcular_area()

    def calculate_inputs(self):
        """Calcula os insumos necessários para as culturas escolhidas."""
        if not self.culture_manager.culturas_escolhidas:
            print("⚠️ Você precisa escolher as culturas primeiro.")
            return
        
        for cultura in self.culture_manager.culturas_escolhidas:
            print(f"\nCalculando insumos para a cultura: {cultura.capitalize()}")
            insumo = Insumo(cultura)
            insumo.calcular()
            for insumo_info in insumo.obter_insumos():
                print(insumo_info)
