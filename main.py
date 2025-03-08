from management.enterprise_name import EnterpriseName
from management.menu import Menu

def main():
    """Função principal para iniciar o programa."""
    home = EnterpriseName.display_company_name
    menu = Menu()
    menu.display()

if __name__ == "__main__":
    main()
