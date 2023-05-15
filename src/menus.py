"""menus.py"""


def print_menu() -> None:
    menu_text = (
        "\tSelect your game ending:\n"
        "\t\t1. Draw\n"
        "\t\t2. White Wins\n"
        "\t\t3. White wins by checkmate\n"
        "\t\t4. Black Wins\n"
        "\t\t5. Black wins by checkmate\n"
        "\t\t6. Exit\n"
    )
    print(menu_text)


def get_users_choice() -> int:
    """Error checking required"""
    choice = int(input("\tChoice (1 - 6): "))
    if 0 < choice < 7:
        return choice
    raise ValueError("Choice must be an number between 1 and 6.")


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
    moves = int(input("Enter your max moves (21 - 99):"))
    if 20 < moves < 100:
        moves = f" {str(moves)}. "
        return moves
    raise ValueError("Max Move must be a number between 21 and 99.")


def strip_mate_query() -> bool:
    strip_mate = str(input("Do you wish to strip the last checkmating move? (y/n): "))
    strip_mate = strip_mate.strip()
    strip_mate = strip_mate.lower()

    if strip_mate == 'yes' or strip_mate == 'y':
        return True

    return False


def main():
    print_menu()
    users_ending = get_users_choice()

    os.system("clear")

    min_max_moves()
    max_move = get_moves()

    strip_last_move = None
    if users_ending == 3 or users_ending == 5:
        strip_last_move = strip_mate_query()

    print(f"Endings: {users_ending}\nMove: {max_move}")

    if strip_last_move is not None:
        print(f"Stripe mate: {strip_last_move}")


if __name__ == "__main__":
    import os
    os.system("clear")

    main()
