#!/usr/bin/env python3
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
import os

import functions as f
import menus as m

os.system("clear")

# Print/get game endings
print(m.endings_menu())
game_endings = f.get_users_choice()

# Print/get file path
print(m.file_path())
files_path = f.get_file_path()

# Print/get file name
print(m.file_name())
path_file = f.get_file_name(files_path)

# Print/get max moves
print(m.min_max_moves())
max_moves = f.get_moves()
f.set_max_move(max_moves)

move_times = f.move_seconds()
