class CultureManager:
    """
    Classe para gerenciar o cadastro e a seleção de culturas.
    """
    def __init__(self):
        self.culturas_disponiveis = set()
        self.cultura_escolhida = set()

    def register_culture(self):
        """Permite ao usuário cadastrar novas culturas."""
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
        """Exibe as culturas cadastradas até o momento."""
        if self.culturas_disponiveis:
            print(f"🌱 Culturas cadastradas: {', '.join(map(str.capitalize, self.culturas_disponiveis))}")
        else:
            print("⚠️ Nenhuma cultura cadastrada até o momento.")

    def select_culture(self):
        """Permite ao usuário selecionar duas culturas."""
        if not self.culturas_disponiveis:
            print("⚠️ Nenhuma cultura cadastrada. Cadastre primeiro antes de escolher.")
            return

        self.cultura_escolhida.clear()
        while len(self.cultura_escolhida) < 2:
            self.registered_cultures()
            cultura = input("Digite a cultura que deseja trabalhar: ").strip().lower()

            if cultura not in self.culturas_disponiveis:
                print("❌ Cultura não cadastrada. Cadastre primeiro antes de escolher.")
            elif cultura in self.cultura_escolhida:
                print("⚠️ Cultura já escolhida. Escolha uma diferente.")
            else:
                self.cultura_escolhida.add(cultura)

        print(f"✅ As culturas escolhidas foram: {', '.join(map(str.capitalize, self.cultura_escolhida))}")
