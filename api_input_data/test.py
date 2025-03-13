from pathlib import Path

def encontrar_arquivo(nome_arquivo, raiz_busca="."):
    """Procura recursivamente por um arquivo específico dentro da estrutura do projeto."""
    raiz_busca = Path(raiz_busca).resolve()

    for item in raiz_busca.iterdir():
        if item.is_file() and item.name == nome_arquivo:
            print(f"✅ Arquivo encontrado: {item}")
            return item
        elif item.is_dir():
            resultado = encontrar_arquivo(nome_arquivo, item)  # Chamada recursiva
            if resultado:
                return resultado

    return None

# Teste a função para encontrar o arquivo 'script_statis.R'
encontrar_arquivo("script_statis.R")

