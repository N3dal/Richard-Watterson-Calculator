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
    tuple contain picture-name and the tkinter.PhotoImage object"""

    # get the picture name.
    picture_name = path.split('/')[-1]

    # now remove the file extension.
    picture_name = picture_name.split(".")[0]

    img = tkinter.PhotoImage(file=path, name=picture_name)

    return picture_name, img


def load_images():
    """return all the needed images."""

    pictures_paths = (

        # frame.
        "./pictures/frame.png",

        # buttons.
        "./pictures/buttons/addition.png",
        "./pictures/buttons/backspace.png",
        "./pictures/buttons/clear_all.png",
        "./pictures/buttons/clear_digit.png",
        "./pictures/buttons/close_parentheses.png",
        "./pictures/buttons/divide.png",
        "./pictures/buttons/dot.png",
        "./pictures/buttons/equal_btn.png",
        "./pictures/buttons/multiply.png",
        "./pictures/buttons/num0.png",
        "./pictures/buttons/num1.png",
        "./pictures/buttons/num2.png",
        "./pictures/buttons/num3.png",
        "./pictures/buttons/num4.png",
        "./pictures/buttons/num5.png",
        "./pictures/buttons/num6.png",
        "./pictures/buttons/num7.png",
        "./pictures/buttons/num8.png",
        "./pictures/buttons/num9.png",
        "./pictures/buttons/open_parentheses.png",
        "./pictures/buttons/percentage.png",
        "./pictures/buttons/positive_negative.png",
        "./pictures/buttons/subtraction.png",

        # title-bar.
        "./pictures/title_bar/close.png",
        "./pictures/title_bar/maximize.png",
        "./pictures/title_bar/minimize.png",
        "./pictures/title_bar/title.png",

        # screen.
        "./pictures/screen/screen.png"

    )

    return {get_image(path)[0]: get_image(path)[-1] for path in pictures_paths}


def main_window():

    root = tkinter.Tk()

    # setup the window size and start position.
    root.geometry(
        f"{WIN_WIDTH}x{WIN_HEIGHT}+{X_START_POSITION}+{Y_START_POSITION}")

    # set the window background color.
    root.configure(bg=WIN_BG)

    # remove the title-bar.
    root.overrideredirect(1)

    d = load_images()

    print(d)

    start_app(root)


def main():
    main_window()


if __name__ == "__main__":
    main()
