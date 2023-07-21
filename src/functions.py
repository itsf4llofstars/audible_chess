"""The functions.py Python file."""
import os
import re
import sys

try:
    from pgn_parsers import pattern
except ImportError as import_error:
    print(f"{import_error}")


def get_users_choice() -> int:
    """Error checking required"""
    ending_choices = (
        "\n\n\tSelect your game ending:\n"
        "\n\t\t1. Draw"
        "\n\t\t2. White Wins"
        "\n\t\t3. White Wins by Checkmate"
        "\n\t\t4. Black Wins"
        "\n\t\t5. Black Wins by Checkmate"
        "\n\t\t6. Exit\n\n"
    )

    os.system("clear")
    print(ending_choices)

    choice = 6
    while True:
        choice = int(input("\tChoice (1 - 6): "))
        if 0 < choice < 6:
            break
        elif choice == 6:
            sys.exit()
        else:
            print("\n\tEnter a number between 1 and 6.\n")
    return choice


def get_file_path() -> str:
    """get_file_path"""
    file_path_text = (
        "\n\n\tEnter the path to the pgn file relative to your home directory.\n"
        "\tIf your files full path is /home/$USER/chess/pgn_files, you will enter:\n"
        "\tchess/pgn_files"
    )

    os.system("clear")
    print(file_path_text)
    file_path = input("\n\tPath: ")
    return os.path.expanduser(os.path.join("~", file_path))


def get_file_name(file_path: str) -> str:
    """get_file_name"""
    file_name_text = (
        "\n\n\tEnter the name of the pgn file. You do not need to add the .pgn\n"
        "\tto the end."
    )

    os.system("clear")
    print(file_name_text)
    file_name = input("\n\tFile Name: ")
    if not file_name.endswith(".pgn"):
        file_name += ".pgn"
    return os.path.join(file_path, file_name)


def get_moves() -> int:
    """Error checking required"""
    while True:
        file_moves_text = (
            "\n\n\tThe minimum move for a game is currently hard set at 20.\n"
            "\tThe maximum move is left up to you, please enter the maximum\n"
            "\tnumber of moves you want for your study game.\n\n"
            "\tExample: Entering 38 can result in games ending between 20 and 38\n"
            "\tmoves, (inclusive). There is no need to add leading or trailing\n"
            "\tspaces or, a period.\n"
        )

        os.system("clear")
        print(file_moves_text)
        moves = int(input("\tEnter your max moves (21 - 99) 0 to quit: "))
        if 20 < moves < 100:
            moves += 1
            return moves
        elif moves == 0:
            sys.exit()
        else:
            os.system("clear")
            print("\n\tPlease enter a number between 21 and 99 or 0 to quit.\n")
            input("Contnue...")
            os.system("clear")


def strip_mate_query() -> bool:
    """Function docstring"""
    os.system("clear")
    strip_mate = str(
        input(
            '\n\n\tEnter a "y", "yes", to strip the last checkmating move, other letters will result in no: '
        )
    )
    strip_mate = strip_mate.strip().lower()
    strip_mate = strip_mate[0]

    return strip_mate == "y"


def move_seconds() -> int:
    """Error check needed"""
    os.system("clear")
    seconds = int(input("\n\n\tPlease enter the number of seconds between each move: "))
    assert isinstance(seconds, int)
    assert seconds > 4
    return seconds


def regex_pgn_file(filename: str):
    """Read a chess pgn file.

    Return those lines beginning with "^(1\.\s)"
    and end with "(\s[1-0|0-1])$" as a list of str's

    Args:
        filename (str): Path and name of the pgn file

    Returns:
        List(str): Only strings of chess games
    """
    game_begin = re.compile(r"^(1\.\s)")
    game_end = re.compile(r"(\s[0-1]|[0-1])$")
    chess_games = []

    try:
        with open(filename, encoding="utf-8") as read:
            for line in read:
                if re.search(game_begin, line) and re.search(game_end, line.rstrip()):
                    chess_games.append(line.rstrip())
    except FileNotFoundError as fnfe:
        print(f"{fnfe}")

    return chess_games


def fast_pgn_file(filename: str):
    """Read a chess pgn file

    Return those lines that begin with "1. " and end with
    either " 1-0", "0-1", " 1/2-1/2", using no regex for
    fasters parsing of large files.

    Args:
        filename (str): Path and name of the pgn file

    Returns:
        List(str): Only strings of chess games
    """
    start = "1. "
    white = " 1-0"
    black = " 0-1"
    draw = " 1/2-1/2"
    pgn_games = []
    try:
        with open(filename, encoding="utf-8") as read:
            for line in read:
                line = line.strip()
                if line.startswith(start) and (
                    line.endswith(white) or line.endswith(black) or line.endswith(draw)
                ):
                    pgn_games.append(line)
    except FileNotFoundError:
        print("File not found: fast_pgn_file()")
        sys.exit()
    return pgn_games


def set_max_move(max_move):
    """Function docstring"""
    pattern["max_move_re"] = r"\s" + str(max_move) + r"\.\s"
    pattern["max_move"] = f" {max_move}. "


def main():
    """main"""
    u_choice = get_users_choice()
    u_file_path = get_file_path()
    u_file_name = get_file_name(u_file_path)
    u_moves = get_moves()
    u_mate = strip_mate_query()
    u_secs = move_seconds()

    print(u_choice)
    print(u_file_path)
    print(u_file_name)
    print(u_moves)
    print(u_mate)
    print(u_secs)

    # games = regex_pgn_file("/home/bumper/python/audible_chess/docs/test_read_file.pgn")
    # print(games)
    # del games

    # games = fast_pgn_file("/home/bumper/python/audible_chess/docs/test_read_file.pgn")
    # print(games)
    # del games

    # set_max_move("44")


if __name__ == "__main__":
    os.system("clear")
    main()
