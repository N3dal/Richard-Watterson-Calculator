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

# set the Defaults.
WIN_WIDTH = 442
WIN_HEIGHT = 540
X_START_POSITION = 1500
Y_START_POSITION = 250
WIN_BG = "#e7eaef"


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


clear()


def start_app(root: tkinter.Tk, **options):
    """"""
    root.mainloop()


def get_image(path: str):
    """get an image using the path and return it as,
    tkinter.PhotoImage object."""

    # get the picture name.
    picture_name = path.split('/')[-1]

    img = tkinter.PhotoImage(file=path, name=name)

    return img


def main_window():

    root = tkinter.Tk()

    # setup the window size and start position.
    root.geometry(
        f"{WIN_WIDTH}x{WIN_HEIGHT}+{X_START_POSITION}+{Y_START_POSITION}")

    # set the window background color.
    root.configure(bg=WIN_BG)

    # remove the title-bar.
    root.overrideredirect(1)

    start_app(root)


def main():
    main_window()


if __name__ == "__main__":
    main()
