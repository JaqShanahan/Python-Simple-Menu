def display_menu(menu_title, options_list):
    while True:
        # Display the menu title
        print(f"{menu_title}: ")

        # Display the menu options with numeric indices
        for index, option in enumerate(options_list, start=1):
            print(f"    [{index}] {option}")

        while True:
            option = input("User: ")

            try:
                option = int(option)
                if 1 <= option <= len(options_list):
                    # Valid option selected, return it
                    return option
                else:
                    # Invalid option, provide feedback and continue
                    print(f"'{option}' is an invalid option. Please choose a valid option.")
                    input("Press Enter to continue...")
            except ValueError:
                # Non-integer input, provide feedback and continue
                print(f"'{option}' is an invalid option. Please choose a valid option.")
                input("Press Enter to continue...")

