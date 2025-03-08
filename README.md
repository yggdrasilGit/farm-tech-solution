# farm-tech-solution
First version project!

## Projeto de Escolha de Culturas

Este projeto tem como objetivo permitir ao usuário selecionar duas culturas distintas para trabalhar. A seleção é feita por meio da função `escolher_cultura()`, que impede a escolha de culturas repetidas. O usuário pode cadastrar novas culturas e visualizá-las antes de fazer a escolha.

## Estrutura do Projeto
```
projeto_escolha_cultura/
|
|-- calculation/
|
│── input_data/
│   ├── __init__.py
│   ├── culture_type.py
|   |-- enterprise_name.py
│── main.py
│── README.md
```

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/yggdrasilGit/farm-tech-solution
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd projeto_escolha_cultura
   ```

3. Crie um ambiente virtual (recomendado):

  Para Windows:
```bash
  python -m venv venv
  venv\Scripts\activate
```
Para Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

4. Instale dependências de projeto 
```bash
pip install -r requirements.txt
```


## Como Usar
1. Execute o script principal:
   ```bash
   python main.py
   ```
2. Digite as culturas que deseja trabalhar quando solicitado.

## Arquivos Principais
- **`culture_type.py`**: Contém a função `escolher_cultura()`, que solicita ao usuário que escolha duas culturas distintas.
- **`main.py`**: Importa e executa a função `escolher_cultura()` a partir de um menu principal.

## Exemplo de Uso
```bash
🌿 🌱
FARM TECH SOLUTION
🌱 🌿

📌 MENU PRINCIPAL
1️⃣ Escolher culturas para trabalhar
2️⃣ Cadastrar novas culturas
3️⃣ Ver culturas cadastradas
0️⃣ Sair

```

## Contribuição
Se desejar contribuir com melhorias para este projeto, siga os passos:
1. Faça um fork do repositório.
2. Crie uma nova branch para sua funcionalidade.
3. Envie um pull request.

## Licença
Este projeto está licenciado sob a [](LICENSE).

## Tipos de insumos 

1️⃣ Sementes ou Mudas
Sementes certificadas (ex: milho, feijão, soja)
Mudas (ex: café, frutíferas, hortaliças)
2️⃣ Fertilizantes e Corretivos de Solo
Adubo orgânico (esterco, composto orgânico)
Fertilizantes químicos (NPK 20-10-10, ureia, superfosfato)
Calcário (para correção do pH do solo)
Gesso agrícola (para corrigir alumínio tóxico no solo)
3️⃣ Defensivos Agrícolas (Agrotóxicos ou Alternativos)
Herbicidas (ex: glifosato para controle de ervas daninhas)
Inseticidas (ex: cipermetrina para controle de pragas)
Fungicidas (ex: mancozebe para prevenir doenças fúngicas)
Biodefensivos (ex: extrato de nim, bacillus thuringiensis)
4️⃣ Irrigação e Conservação da Umidade
Sistema de irrigação (gotejamento, aspersão)
Mulching (palha, plástico para retenção de umidade)
5️⃣ Equipamentos e Ferramentas
Enxada, foice, rastelo
Pulverizador manual ou motorizado
Trator e implementos (se for produção em larga escala)
6️⃣ Mão de Obra e Serviços
Contratação de trabalhadores rurais
Análise de solo e assistência técnica

