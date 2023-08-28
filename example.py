from main import display_menu

# Example usage:
menu_title = "Main Menu"
options = ["Option 1", "Option 2", "Option 3"]
selected_option = display_menu(menu_title, options)

while True:
    if selected_option == 1:
        print(f"Selected {selected_option}")
        break
