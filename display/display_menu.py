from api_input_data.load_api_metereologica import RClimateDataLoader
from api_input_data.load_data_meteriologist import MeteorologistDataLoader
from api_input_data.loard_api_geolocalizacao import RGeolocationLoader
from management.culture_manager import CultureManager
from management.insum_manager import Insumo
from calculation.insum_calculator import InsumoCalculator
from display.display_area import DisplayAreaCalculator
from api_input_data.load_data_statis import RScriptLoader
from display.display_meteriologica import Cidade

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
                nome_cidade = input("Digite o nome da cidade: ")
                cidade = Cidade(nome_cidade)
                print(cidade.mostrar_cidade())
                print(cidade.buscar_informacoes())
                caminho_arquivo = cidade.salvar_em_json()
                print(f"Informações salvas em {caminho_arquivo}")
                geo_loader = RGeolocationLoader()
                geo_loader.executar_geolocalizacao()
                loader = RClimateDataLoader()
                loader.executar_script()
                nome_arquivo = "clima_portugues.json"  # Nome do arquivo JSON
                loader = MeteorologistDataLoader(nome_arquivo)
                dados_clima = loader.carregar_arquivo_json()
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
            print(f"\n📝 Cadastrando insumos para a cultura: {cultura.capitalize()}")
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
        """Calcula a quantidade necessária de insumos para cada cultura selecionada."""
        if not self.culture_manager.cultura_escolhida:
            print("⚠️ Você precisa escolher as culturas primeiro.")
            return

        if not self.insumos:
            print("⚠️ Nenhum insumo foi cadastrado ainda.")
            return

        for cultura in self.culture_manager.cultura_escolhida:
            if cultura not in self.insumos:
                print(f"⚠️ Nenhum insumo cadastrado para a cultura {cultura.capitalize()}.")
                continue

            area = self.display_area_calculador.get_area(cultura)
            if area is None:
                print(f"⚠️ Área de plantio não cadastrada para a cultura {cultura.capitalize()}.")
                continue

            insumo = self.insumos[cultura]
            quantidade_necessaria = insumo.calcular_quantidade(area)
            print(f"\n📊 Quantidade necessária de insumo para {cultura.capitalize()} em {area:.2f} hectares:")
            for nome_insumo, quantidade in quantidade_necessaria.items():
                print(f"➡️ {nome_insumo}: {quantidade}")
