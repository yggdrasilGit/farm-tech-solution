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
        self.display_area_calculador = DisplayAreaCalculator(cultura=self.culture_manager.cultura_escolhida)
        self.insumos = {}  # Dicionário para armazenar insumos cadastrados por cultura
        self.insumo = Insumo() # instancia insumo para cadastrar 
        self.estatistica = RScriptLoader
        self.area_plantio = self.display_area_calculador
    
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
            print("9️⃣ Estatistica")
            print("🔟 Informações meteriologicas")
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
            elif opcao == "10":
                pass
            elif opcao == "0":
                print("👋 Saindo do programa. Até mais!")
                break
            else:
                print("❌ Opção inválida. Tente novamente.")
              
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
    
    
    def calcular_insumo(self):
        """Calcula a quantidade necessária de insumos para cada cultura cadastrada."""
        if not self.area_plantio:
            print("⚠️ Nenhuma área de plantio foi cadastrada ainda.")
            return

        if not self.insumos:
            print("⚠️ Nenhum insumo foi cadastrado ainda.")
            return

        for cultura in self.culture_manager.cultura_escolhida:
            area = self.area_plantio.area
            if cultura not in self.insumos:
                print(f"⚠️ Nenhum insumo cadastrado para a cultura {cultura.capitalize()}.")
                continue
            
            print(f"\n📊 Calculando insumos para a cultura {cultura.capitalize()}...")
            _quantidade = len(self.insumo.exibir_insumos())

            for i in range(_quantidade):
                print(i)
                area_plantada = self.area_plantio.area
                print(area_plantada[0])
                area = area_plantada[i]
                quantidade_insumo = self.insumo.quantidade_insumo()
                print(quantidade_insumo, area)
                quantidade_total = InsumoCalculator(area, quantidade_insumo)

                print(f"🔹 {self.insumo.exibir_insumos()}: {quantidade_total.calcular_insumo():.2f} unidades necessárias para {area:.2f} hectares.")

            
