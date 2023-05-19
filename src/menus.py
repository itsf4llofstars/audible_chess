"""menus.py"""


def ending_menu() -> str:
    return (
        "\n\n\tSelect your game ending:\n"
        "\n\t\t1. Draw"
        "\n\t\t2. White Wins"
        "\n\t\t3. White Wins by Checkmate"
        "\n\t\t4. Black Wins"
        "\n\t\t5. Black Wins by Checkmate"
        "\n\t\t6. Exit\n\n"
    )


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
        "\tspaces or, a period.\n"
    )
    print(move_str)


def get_moves() -> int:
    """Error checking required"""
    moves = int(input("\tEnter your max moves (21 - 99): "))
    if 20 < moves < 100:
        moves += 1
        return moves
    raise ValueError("Max Move must be a number between 21 and 99.")


def max_moves() -> str:
    return (
        "\n\n\tThe minimum number of move is hard set at 20. for now.\n"
        "\tYou can enter the maximun number of moves you would like to\n"
        "\tstudy. If you want between 20 - 35 please enter 35. Your move\n"
        "\tmust be above 20 and below 100.\n\n"
        "\tEnter your maximum number of moves: \n"
    )


def strip_mate_query() -> bool:
    """Error check required"""
    strip_mate = str(input("Do you wish to strip the last checkmating move? (y/n): "))
    strip_mate = strip_mate.strip().lower()

    if strip_mate == "yes" or strip_mate == "y":
        return True

    return False


def move_seconds():
    return "\n\n\tPlease enter the number of seconds between each move: "


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
