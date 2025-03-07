from input_data.culture_type import CultureSelection
from input_data.enterprise_name import EnterpriseName


def menu():
    """
    Displays the main menu of the program and allows the user to choose actions.
    
    Returns:
        None
    """
    # Displays the company name at the beginning of the menu
    company_name = EnterpriseName.display_company_name()
    print(company_name)  # Here, we print the string returned by the function5
    

    # Creates an instance of SelecaoCultura
    selection = CultureSelection()
    
    # Calls the menu method of the instance to display the interactive menu
    selection.menu()

if __name__ == "__main__":
    # Calls the menu function
    menu()

