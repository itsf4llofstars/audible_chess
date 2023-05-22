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
import menus as m
import functions as f
import pgn_parsers as pp
import os
import sys

os.system("clear")

print(m.endings_menu())
user_ending = f.get_users_choice()

print(m.min_max_moves())
user_max_move = f.get_moves()
f.set_max_move(user_max_move)

user_mate = f.strip_mate_query()
user_move_time = f.move_seconds()

print(f"{user_ending = }")
print(f"{user_max_move = }")
print(f"{pp.regex['max_move'] = }")
print(f"{pp.regex['max_move_re'] = }")
print(f"{user_mate = }")
print(f"{user_move_time = }")
