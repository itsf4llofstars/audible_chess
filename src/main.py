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
import os

os.system("clear")

m.print_menu()
user_end_choice = m.get_users_choice()

os.system("clear")

m.min_max_moves()

max_move = m.get_moves()

strip_mate = None
if user_end_choice == 3 or user_end_choice == 5:
    strip_mate = m.strip_mate_query()

if strip_mate is not None:
    print(f"{user_end_choice = } {max_move = } {strip_mate = }")
else:
    print(f"{user_end_choice = } {max_move = }")
