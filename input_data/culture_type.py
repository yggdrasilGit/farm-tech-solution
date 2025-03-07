# coding: utf-8

class CultureSeletion:
    """
    Class to manage agricultural cultures.

    The user can:
    1️⃣ Choose two distinct cultures to work with.
    2️⃣ Register new available cultures.
    3️⃣ View all registered cultures.
    """


    def __init__(self):
        self.culturas_disponiveis = set()  # Culturas disponíveis para escolha
        self.culturas_escolhidas = set()   # Culturas escolhidas pelo usuário

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
            self.culturas_cadastradas()
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
            print("0️⃣ Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.select_culture()
            elif opcao == "2":
                self.register_culture()
            elif opcao == "3":
                self.registered_cultures()
            elif opcao == "0":
                print("👋 Saindo do programa. Até mais!")
                break
            else:
                print("❌ Opção inválida. Tente novamente.")

# Exemplo de uso:
# selecao = CultureSeletion
# selecao.menu()
