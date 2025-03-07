from input_data.enterprise_name import EnterpriseName
from input_data.culture_selection import CultureSelection

def menu():
    """
    Displays the main menu of the program and allows the user to choose actions.
    
    Returns:
        None
    """
    # Displays the company name at the beginning of the menu
    company_name = EnterpriseName.display_company_name()
    print(company_name)  # Here, we print the string returned by the function
    
    # Creates an instance of CultureSelection
    selection = CultureSelection()

    while True:
        try:
            # Calls the menu method of the instance to display the interactive menu
            selection.menu()
        except Exception as e:
            print(f"❌ Ocorreu um erro: {e}")
            continue  # Keeps the loop running if any error occurs
        break

if __name__ == "__main__":
    # Calls the menu function
    menu()
