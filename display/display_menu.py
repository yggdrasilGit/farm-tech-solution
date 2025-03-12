from management.culture_manager import CultureManager
from management.insum_manager import Insumo
from calculation.insum_calculator import InsumoCalculator
from display.display_area import DisplayAreaCalculator
from api_input_data.load_data_statis import RScriptLoader

class DisplayMenu:
    """
    Classe responsável mandar as informacoes para o menu principal.
    """
    def __init__(self):
        self.culture_manager = CultureManager()
        self.display_area_calculador = DisplayAreaCalculator(cultura=self.culture_manager.culturas_escolhidas)
        self.insumos = {}  # Dicionário para armazenar insumos cadastrados por cultura
        self.insumo = Insumo() # instancia insumo para cadastrar 
        self.estatistica = RScriptLoader
    
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
            print("9. Estatistica")
            print("0️⃣ Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.culture_manager.select_culture()
            elif opcao == "2":
                self.culture_manager.register_culture()
            elif opcao == "3":
                self.culture_manager.registered_cultures()
            elif opcao == "4":
                self.display_area_calculador.calculate_area()
            elif opcao == "5":
                self.register_inputs()
            elif opcao == "6":
                self.show_inputs()
            elif opcao == "7":
                self.display_area_calculador.show_areas()
            elif opcao == "8":
                self.calcular_insumo()
            elif opcao == "9":
                self.estatistica = RScriptLoader.chamar_estatistica()
            elif opcao == "0":
                print("👋 Saindo do programa. Até mais!")
                break
            else:
                print("❌ Opção inválida. Tente novamente.")
              
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
            print(self.insumo.exibir_insumos())
    
    
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

            
