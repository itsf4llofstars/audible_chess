# Ideas on Parser PGN Files

## Fast Parsers

### Fast 1

Parses the entire file into memory. Chosses a random line and
runs the conditionals and regex patterns until the random line matches
the required conditions.<br>

```python
import os
import sys
import re
import random

filename = os.path.expanduser(
    os.path.join("~", "path", "to", "pgn_file", "pgn_file.pgn")
)
chess_file = []

with open(filename) as read:
    chess_file = read.readlines()

game = ""
runs = 0

while True:
    runs += 1
    game = random.choice(chess_file).strip()
    white = True
    mate = False

    if (
            not re.search(r"1\.\s[a-hN][3-4acfh]3?\s[a-hN][5-6acfh]6?\s2\.\s", game)
            or re.search(r"\s30\.\s", game)
            or not re.search(r"\s20\.\s", game)
            or re.search(r"(\(|\)|{|}|\[|\]|<|>)", game)
            ):
        continue
    elif white and mate and re.search(r"(#\s1-0)$", game):
        break
    elif white and not mate and re.search(r"([^#]\s1-0)$", game):
        break
    elif not white and mate and re.search(r"(#\s0-1)$", game):
        break
    elif not white and not mate and re.search(r"([^#]\s0-1)$", game):
        break

del chess_file
annotates = ["!", "?" "+"]
for annotate in annotates:
    game = game.replace(annotate, "")

split_game = game.split(" ")
print(split_game)
input("...")

for move in split_game:
    os.system("clear")
    input("\n\t" + move + "\n)
```

### Fast 2

Reads each line of the pgn file and parses the line
according to the conditinals and regex pattern. Appends
line if it meets the conditions then picks a random game
and runs a more verbose regex condition

```python
import os
import sys
import re
import random

filename = os.path.join("/", "media", "bumper", "EDD2-E40F", "raspi32", "lichess_201407.pgn")

white = True
if sys.argv[1] == "-b":
    white = False

mate = False
if sys.argv[2] == "-m":
    mate = True

games = []

with open(filename) as read:
    for line in read:
        if (
                not line.startswith("1. ")
                or " 40. " in line
                or " 20. "
                not in line
                or "(" in line
                or "{" in line
                or "[" in line
                or "<" in line
        ):
            continue

        if white:
            if not line.strip().endswith(" 1-0"):
                continue
            if mate:
                if "#" in line:
                    games.append(line.strip())
            else:
                if "#" not in line:
                    games.append(line.strip())
        if not white:
            if not line.strip().endswith(" 0-1"):
                continue
            if mate:
                if "#" in line:
                    games.append(line.strip())
            else:
                if "#" not in line:
                    games.append(line.strip())

random_game = ""

while True:
    random_game = random.choice(games)

    if white and mate:
        if not re.search(r"(#\s1-0)$", random_game):
            continue
    elif white and not mate:
        if not re.search(r"([^#]\s1-0)$", random_game):
            continue
    if not white and mate:
        if not re.search(r"(#\s0-1)$", random_game):
            continue
    elif not white and not mate:
        if not re.search(r"([^#]\s0-1)$", random_game):
            continue

    if re.search(r"1\.\s[a-hN][3-4acfh]3?\s[a-hN][5-6acfh]6?\s2\.\s", random_game):
        annotates = ["!", "?", "+"]

        for annotate in annotates:
            random_game = random_game.replace(annotate, "")

        break

print()
print(random_game)
```