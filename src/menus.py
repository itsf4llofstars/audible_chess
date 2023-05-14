"""menus.py"""


def print_menu() -> None:
    menu_text = (
        "\tSelect your game ending:\n"
        "\t\t1. Draw\n"
        "\t\t2. White Wins\n"
        "\t\t3. White wins by checkmate\n"
        "\t\t4. Black Wins\n"
        "\t\t5. Black wins by checkmate\n"
    )
    print(menu_text)


def get_users_choice() -> int:
    return int(input("\tChoice (1, 2, 3, 4, 5): "))


def main():
    print_menu()
    users_ending = get_users_choice()
    print(users_ending)


if __name__ == "__main__":
    main()
