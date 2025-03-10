from management.culture_manager import CultureManager
from management.insum_manager import Insumo
from calculation.insum_calculator import InsumoCalculator
from display.display_menu import DisplayMenu

class Menu:
    """
    Classe responsável por exibir e gerenciar o menu principal.
    """
    def __init__(self):
        self.culture_manager = CultureManager()
        self.insumos = {}  # Dicionário para armazenar insumos cadastrados por cultura
        self.areas_plantio = {}  # Dicionário para armazenar áreas por cultura
        self.insumo = Insumo() # instancia insumo para cadastrar 
        self.display_menu = DisplayMenu()

    def menu_display(self):
        """Exibe o menu principal e gerencia as opções do usuário."""
        self.display_menu.display()

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
