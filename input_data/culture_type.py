from calculation.area_calculator import AreaCalculator
from calculation.insumo import Insumo  # Importando a classe Insumo

class CultureSelection:
    """
    Class to manage agricultural cultures and calculate planting areas.

    The user can:
    1️⃣ Choose two distinct cultures to work with.
    2️⃣ Register new available cultures.
    3️⃣ View all registered cultures.
    4️⃣ Calculate the area for planting based on selected cultures.
    5️⃣ Calculate the necessary inputs (seeds, fertilizer, defensive, etc.) based on the area.
    """

    def __init__(self):
        self.culturas_disponiveis = set()  # Culturas disponíveis para escolha
        self.culturas_escolhidas = set()   # Culturas escolhidas pelo usuário
        self.area_calculator = AreaCalculator()  # Instancia a classe de cálculo de área

    def select_culture(self):
        """
        Allows the user to select two distinct cultures to work with.
        The user can only choose cultures that are already registered.

        Returns:
            list: A list containing the two cultures selected by the user.
        """
        if not self.culturas_disponiveis:
            print("⚠️ Nenhuma cultura cadastrada. Cadastre primeiro antes de escolher.")
            return
        
        self.culturas_escolhidas.clear()  # Limpa seleções anteriores
        while len(self.culturas_escolhidas) < 2:
            self.registered_cultures()
            cultura = input("Digite a cultura que deseja trabalhar: ").strip().lower()

            if cultura not in self.culturas_disponiveis:
                print("❌ Cultura não cadastrada. Cadastre primeiro antes de escolher.")
            elif cultura in self.culturas_escolhidas:
                print("⚠️ Cultura já escolhida. Escolha uma diferente.")
            else:
                self.culturas_escolhidas.add(cultura)

        print(f"✅ As culturas escolhidas foram: {', '.join(map(str.capitalize, self.culturas_escolhidas))}")

    def register_culture(self):
        """
        Permite ao usuário cadastrar novas culturas disponíveis para escolha.
        """
        while True:
            cultura = input("Digite o nome da cultura para cadastrar (ou 'sair' para voltar ao menu): ").strip().lower()
            if cultura == "sair":
                break
            if cultura in self.culturas_disponiveis:
                print("⚠️ Cultura já cadastrada.")
            else:
                self.culturas_disponiveis.add(cultura)
                print(f"✅ Cultura '{cultura.capitalize()}' cadastrada com sucesso!")

    def registered_cultures(self):
        """
        Exibe as culturas cadastradas até o momento.
        """
        if self.culturas_disponiveis:
            print(f"🌱 Culturas cadastradas: {', '.join(map(str.capitalize, self.culturas_disponiveis))}")
        else:
            print("⚠️ Nenhuma cultura cadastrada até o momento.")

    def menu(self):
        """
        Exibe o menu principal para o usuário escolher uma ação.
        """
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
                self.select_culture()
            elif opcao == "2":
                self.register_culture()
            elif opcao == "3":
                self.registered_cultures()
            elif opcao == "4":
                self.calculate_area_for_selected_cultures()
            elif opcao == "5":
                self.calculate_inputs_for_selected_cultures()
            elif opcao == "0":
                print("👋 Saindo do programa. Até mais!")
                break
            else:
                print("❌ Opção inválida. Tente novamente.")

    def calculate_area_for_selected_cultures(self):
        """
        Chama o cálculo de área separadamente para cada cultura escolhida.
        """
        if not self.culturas_escolhidas:
            print("⚠️ Você precisa escolher as culturas primeiro.")
            return
        
        for cultura in self.culturas_escolhidas:
            print(f"\nCalculando área para a cultura: {cultura.capitalize()}")
            self.area_calculator.calculate_area(cultura)  # Passa a cultura para o método de cálculo

    def calculate_inputs_for_selected_cultures(self):
        """
        Calcula os insumos necessários para as culturas escolhidas.
        """
        if not self.culturas_escolhidas:
            print("⚠️ Você precisa escolher as culturas primeiro.")
            return
        
        for cultura in self.culturas_escolhidas:
            print(f"\nCalculando insumos para a cultura: {cultura.capitalize()}")
            insumo = Insumo(cultura)  # Cria uma instância de Insumo para a cultura
            insumo.calcular_insumos()  # Calcula os insumos para a cultura
            for insumo_info in insumo.obter_insumos():
                print(insumo_info)  # Exibe os insumos calculados
