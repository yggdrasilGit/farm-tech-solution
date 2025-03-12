import rpy2.robjects as robjects
import os
import json
from tabulate import tabulate


""" Esta classe tem por objetivo carregar scripts r para python 

Metodos:
    __init__
        diretorio: colocar o caminho do diretorio onde estão os 
                    scripts em r
        nome_script: colocar o nome do arquivo.R

    carregar_script:
        
        Ele busca executa e carrega o script.r
"""
class RScriptLoader:
    def __init__(self, diretorio,  subdiretorio, nome_script):
        self.diretorio = diretorio
        self.nome_script = nome_script
        self.subdiretorio = subdiretorio
        self.script_path = os.path.join(diretorio, subdiretorio, nome_script )

    def carregar_script(self):
        try:
            robjects.r.source(self.script_path)
            print(f"Script '{self.nome_script}' carregado com sucesso.")
        except Exception as e:
            print(f"Erro ao carregar o script: {e}")
    
    def carregar_arquivo_json(self):
        try:
            with open(self.script_path, 'r') as arquivo:
                dados = json.load(arquivo)

            # Transforma o dicionário no formato tabular
            tabela = []
            for chave, valores in dados.items():
                tabela.append([chave, valores["media"][0], valores["desvio_padrao"][0]])

            # Define os cabeçalhos
            headers = ["Parâmetro", "Média", "Desvio Padrão"]

            # Exibe a tabela no terminal
            print("\n\n\nDados estatístico das áreas plantadas")
            print(tabulate(tabela, headers=headers, tablefmt="grid"))
            print("\n\n")

            return dados
        except Exception as e:
            print(f"Erro ao carregar o arquivo JSON: {e}")
            return None
    
    def chamar_estatistica():
        diretorio = "farm-tech-solution-R/"
        sub_diretorio_1 = "R/"
        sub_diretorio_2 = "data/"
        script_1 = "script_statis.R"
        data = "estatisticas.json"
        loader = RScriptLoader(diretorio, sub_diretorio_1 ,script_1)
        loader_json = RScriptLoader(diretorio, sub_diretorio_2, data)
        loader.carregar_script()
        
        return loader_json.carregar_arquivo_json()

        
