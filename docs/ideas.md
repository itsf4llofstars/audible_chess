# Ideas on Parser PGN Files

## Fast Parsers

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