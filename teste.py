import pip

def instalar_dependencias():
    # Instalar pacotes usando o arquivo requirements.txt
    pip.main(['install', '-r', 'requirements.txt'])

# Chama a função para instalar as dependências
instalar_dependencias()