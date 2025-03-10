from management.menu import Menu
from management.enterprise_name import EnterpriseName

def main():
    """Função principal para iniciar o programa."""
    enterprice = EnterpriseName()
    print(enterprice.display_company_name())
    menu = Menu()
    menu.menu_display()

if __name__ == "__main__":
    main()
