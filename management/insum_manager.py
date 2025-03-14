from management.culture_manager import CultureManager


class Insumo:
    """
    Classe para gerenciar os insumos necessários para o plantio de uma cultura.
    """
    def __init__(self):
        self.insumos = []  # Lista de insumos cadastrados para a cultura
        self.cultura = CultureManager()
    
    def cadastrar_insumos(self):
        """Permite ao usuário cadastrar os tipos de insumos para a cultura."""
        print(f"\n🔹 Cadastro de insumos para a cultura: {self.cultura.cultura_escolhida}")
        while True:
            nome_insumo = input("Digite o nome do insumo (ou 'sair' para finalizar): ").strip()
            if nome_insumo.lower() == 'sair':
                break
            quantidade = input(f"Digite a quantidade necessária de {nome_insumo}: ").strip()
            unidade = input(f"Digite a unidade de medida para {nome_insumo} (ex: kg, litros): ").strip()
            self.insumos.append({"nome": nome_insumo, "quantidade": quantidade, "unidade": unidade})
            print(f"✅ Insumo '{nome_insumo}' cadastrado com sucesso!")
    
    def obter_insumos(self):
        """Retorna a lista de insumos cadastrados para a cultura."""
        return self.insumos if self.insumos else "Nenhum insumo cadastrado ainda."
    
    def exibir_insumos(self):
        """Exibe os insumos cadastrados de forma organizada."""
        if not self.insumos:
            print("⚠️ Nenhum insumo cadastrado para esta cultura.")
            return
        print(f"\n📌 Insumos cadastrados para a cultura: {self.cultura.cultura_escolhida}")
        for insumo in self.insumos:
            print(f"- {insumo['nome']}: {insumo['quantidade']} {insumo['unidade']}")
