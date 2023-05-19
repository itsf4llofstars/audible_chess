#!/usr/bin/env python3
<<<<<<< HEAD
"""main.py

Audible Chess Project main Python file
version 0.0.0

Licensed under the:
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

itsf4llofstars
irooted4hal@mailfence.com
2023
"""
import menus as m
import functions as f
import pgn_parsers as pp
import os
import sys

os.system("clear")

# m.print_menu()
# user_end_choice = m.get_users_choice()
user_end_choice = 2

os.system("clear")

# m.min_max_moves()

# max_move = m.get_moves()
max_move = 30

strip_mate = None
if user_end_choice == 3 or user_end_choice == 5:
    strip_mate = m.strip_mate_query()

# if strip_mate is not None:
#     print(f"{user_end_choice = } {max_move = } {strip_mate = }")
# else:
#     print(f"{user_end_choice = } {max_move = }")

f.set_max_move(max_move)

pgn_file = os.path.expanduser(
    os.path.join("/", "media", "bumper", "EDD2-E40F", "raspi32", "lichess_short.pgn")
)
all_games = f.fast_pgn_file(pgn_file)
[print(game) for game in all_games]

sys.exit()
=======
import os
import menus as m

os.system("clear")

<<<<<<< HEAD
m.ending_menu()
>>>>>>> 9c8b621 (Format menu_text)
=======
print(m.ending_menu())
>>>>>>> 39b9a69 (Change ending_menu to return str)
