"""menus.py"""


def endings_menu() -> str:
    return (
        "\n\n\tSelect your game ending:\n"
        "\n\t\t1. Draw"
        "\n\t\t2. White Wins"
        "\n\t\t3. White Wins by Checkmate"
        "\n\t\t4. Black Wins"
        "\n\t\t5. Black Wins by Checkmate"
        "\n\t\t6. Exit\n\n"
    )


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


def move_seconds():
    return "\n\n\tPlease enter the number of seconds between each move: "


def main():
    ...

if __name__ == "__main__":
    import os

    os.system("clear")
    main()
