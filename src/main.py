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
print(game_endings)

# Print/get file path

# Print/get file name
