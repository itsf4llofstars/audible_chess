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
import sys

try:
    import functions as f
except ImportError as import_error:
    print(f"{import_error}")

# Print/get game endings
game_endings = f.get_users_choice()

# Print/get mate
strip_mate: bool = None
if game_endings == 3 or game_endings == 5:
    strip_mate = f.strip_mate_query()

# Print/get file path
files_path = f.get_file_path()

# Print/get file name
path_file = f.get_file_name(files_path)

# Print/get max moves
max_moves = f.get_moves()
f.set_max_move(max_moves)

# Print/get move times
os.system("clear")
move_times = f.move_seconds()
