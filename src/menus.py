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
    """Error checking required"""
    return int(input("\tChoice (1, 2, 3, 4, 5): "))


def min_max_moves() -> None:
    move_str = (
        "\n\n\tThe minimum move for a game is currently hard set at 20.\n"
        "\tThe maximum move is left up to you, please enter the maximum\n"
        "\tnumber of moves you want for your study game.\n\n"
        "\tExample: Entering 38 can result in games ending between 20 and 38\n"
        "\tmoves, (inclusive). There is no need to add leading or trailing\n"
        "\tspaces or, a period."
    )
    print(move_str)


def get_moves() -> str:
    """Error checking required
    20[.], nnn[.] not allowed
    """
    moves = str(input("Enter your max moves: "))
    moves = moves.strip()
    if "." in moves:
        moves = moves.replace(".", "")
    return moves


def main():
    print_menu()
    users_ending = get_users_choice()
    print(users_ending)
    os.system("clear")
    min_max_moves()
    max_move = get_moves()
    print(max_move)


if __name__ == "__main__":
    import os
    os.system("clear")

    main()
