#!/usr/bin/python3
# -----------------------------------------------------------------
# simple try to make richard watterson calculator using,
# python/Tkinter
#
# link to the Episode:
# https://www.youtube.com/watch?v=YeAp15OmW2s
#
#
# Author:N84.
#
# Create Date:Fri Jul 22 12:12:38 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------


from os import name as OS_NAME
from os import system
import tkinter


def clear():
    """wipe terminal screen."""

    if OS_NAME == "posix":
        # for *nix machines.
        system("clear")

    elif OS_NAME == "windows":
        system("cls")

    else:
        # for all other OS in the world.
        # system("your-command")
        pass


def main_window():
    pass


def main():
    main_window()


if __name__ == "__main__":
    main()
