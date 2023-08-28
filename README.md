# Python Simple Menu
This is a simple Python program that allows you to display a menu to the user and get their selection. It's a useful utility for creating text-based menu-driven applications.

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **User-Friendly Menu**: Easily display a menu with a specified title and a list of options.
- **Input Validation**: The program validates user input to ensure they select a valid option.
- **Numeric Indices**: Each option is presented with a numeric index for user convenience.

## Usage

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/JaqShanahan/python-simple-menu.git
   ```

2. Import the `display_menu` function into your Python code:

   ```python
   from menu_util import display_menu
   ```

3. Create a list of options you want to display in the menu:

   ```python
   options = ["Option 1", "Option 2", "Option 3"]
   ```

4. Call the `display_menu` function with your menu title and options list:

   ```python
   selected_option = display_menu("Main Menu", options)
   ```

   The function will return the index of the selected option.

5. Use the `selected_option` variable to perform the desired action based on the user's choice.

## How It Works

The `display_menu` function takes two arguments:

- `menu_title`: The title you want to display at the top of the menu.
- `options_list`: A list of strings representing the menu options.

The user is prompted to enter a numeric choice, and the program validates that the input is a valid option. If the user enters an invalid option, they are provided with feedback and prompted to try again. Once a valid option is selected, the function returns the index of the selected option, allowing you to take the appropriate action in your program.

## Contributing

Contributions are welcome! If you have any improvements or feature suggestions, please open an issue or a pull request on [GitHub](https://github.com/JaqShanahan/python-simple-menu).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---