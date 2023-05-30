"""fast_pgn_parsers.py file"""


def plarse_pgn_file(filename, min_move: str = " 20. ", max_move: str = " 40. ", white: bool = True, mate: bool False):
    try:
        with open(filename) as read:
            for line in read:
                line = line.strip()
    except FileNotFoundError as fnfe:
        pritn(f"{fnfe}")
    else:
        pass
    finally:
        pass



def main():
    pass


if __name__ == "__main__":
    main()
