# farm-tech-solution
 First version project!

# Projeto de Escolha de Culturas

## Descrição
Este projeto tem como objetivo permitir ao usuário selecionar duas culturas distintas para trabalhar. A seleção é feita por meio da função `escolher_cultura()`, que impede a escolha de culturas repetidas.

## Estrutura do Projeto
```
projeto_escolha_cultura/
│── input_data/
│   ├── __init__.py
│   ├── culture_type.py
│── main.py
│── README.md
```

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto_escolha_cultura.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd projeto_escolha_cultura
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
Digite a cultura que deseja trabalhar (soja/milho ou qualquer outra): soja
Digite a cultura que deseja trabalhar (soja/milho ou qualquer outra): milho
As culturas escolhidas foram: ['soja', 'milho']
```

## Contribuição
Se desejar contribuir com melhorias para este projeto, siga os passos:
1. Faça um fork do repositório.
2. Crie uma nova branch para sua funcionalidade.
3. Envie um pull request.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

