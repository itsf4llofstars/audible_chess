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

try:
    import functions as f
    import menus as m
except ImportError as ie:
    print(f"{ie}")

os.system("clear")

# Print/get game endings
print(m.endings_menu())
game_endings = f.get_users_choice()

# Print/get mate
strip_mate: bool = None
if game_endings == 3 or game_endings == 5:
    os.system("clear")
    strip_mate = f.strip_mate_query()

print(strip_mate)
input()

# Print/get file path
os.system("clear")
print(m.file_path())
files_path = f.get_file_path()

# Print/get file name
os.system("clear")
print(m.file_name())
path_file = f.get_file_name(files_path)

# Print/get max moves
os.system("clear")
print(m.min_max_moves())
max_moves = f.get_moves()
f.set_max_move(max_moves)

# Print/get move times
os.system("clear")
move_times = f.move_seconds()
