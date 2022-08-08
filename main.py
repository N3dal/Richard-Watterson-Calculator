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
from sys import exit

# TODO: create json file to store all the images paths into it.

# set the Defaults.
WIN_WIDTH = 442
WIN_HEIGHT = 540
X_START_POSITION = 1500
Y_START_POSITION = 250
WIN_BG = "#e7eaef"

BTN_PROPERTIES = {

    "border": 0,
    "highlightthickness": 0,
    "bg": WIN_BG,
    "activebackground": WIN_BG,

}

LABEL_PROPERTIES = {

    "border": 0,
    "highlightthickness": 0,
    "bg": WIN_BG

}

SCREEN_VALUE_LABEL_PROPERTIES = {

    "bg": "#cdd0ba",
    "fg": "#626457",
    "font": ("Calbri", 29, "bold"),
    "width": 14,
    "anchor": "e"

}


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

    return None


clear()


def start_app(root: tkinter.Tk, **options):
    """"""
    root.mainloop()

    return None


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
    """return all the needed images,
    as dictionary."""

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


def clear_screen(screen_var: tkinter.StringVar, state: int = 1):
    """clear the calculator screen either one digit or the whole screen,
    depending on the state param where:
    1 => clear one digit the last digit.
    0 => clear the whole screen all digits.
    and the function by default clear the last digit.
    """

    if state:
        # clear the last digit, by taking the string without the last element.
        temp_string = screen_var.get()[:-1]
        screen_var.set(temp_string)

    else:
        screen_var.set('')

    return None


def print_to_screen(text: str, screen_var: tkinter.StringVar):
    """print any value to the calculator screen."""

    current_screen_value = screen_var.get()

    current_screen_value += text

    screen_var.set(current_screen_value)

    return None


def main_window():

    root = tkinter.Tk()

    # setup the window size and start position.
    root.geometry(
        f"{WIN_WIDTH}x{WIN_HEIGHT}+{X_START_POSITION}+{Y_START_POSITION}")

    # set the window background color.
    root.configure(bg=WIN_BG)

    # remove the title-bar.
    root.overrideredirect(1)

    # load all the pictures.
    images = load_images()

    # print(images.keys()) # DEBUG.

    # now create the frame.
    main_window_frame = tkinter.Label(
        root, name="main_window_frame_label", image=images["frame"], **LABEL_PROPERTIES)
    main_window_frame.place(x=0, y=0)

    # now create the title-bar.

    # first the title.
    title_bar_title = tkinter.Label(
        root, name="title_bar_title_label", image=images["title"], **LABEL_PROPERTIES)
    title_bar_title.place(x=12, y=12)

    # second the title-bar buttons.
    minimize_btn = tkinter.Button(
        root, name="title_bar_minimize_btn", image=images["minimize"], **BTN_PROPERTIES)
    minimize_btn.place(x=315, y=12)

    maximize_btn = tkinter.Button(
        root, name="title_bar_maximize_btn", image=images["maximize"], **BTN_PROPERTIES)
    maximize_btn.place(x=355, y=12)

    close_btn = tkinter.Button(
        root, name="title_bar_close_btn", image=images["close"], command=exit, **BTN_PROPERTIES)
    close_btn.place(x=395, y=12)

    # create the calculator_screen_variable.
    calculator_screen_var = tkinter.StringVar(root)

    # init the calculator_screen_var
    calculator_screen_var.set('')

    # now create the screen.
    calculator_screen = tkinter.Label(
        root, name="calculator_screen_label", image=images["screen"], **LABEL_PROPERTIES)
    calculator_screen.place(x=12, y=50)

    # now create the screen_value label.
    calculator_screen_value_label = tkinter.Label(
        root, name="calculator_screen_value_label", textvariable=calculator_screen_var,
        **SCREEN_VALUE_LABEL_PROPERTIES)
    calculator_screen_value_label.place(x=30, y=65)

    # now create the buttons.

    addition_btn = tkinter.Button(root, name="addition_btn",
                                  command=None, image=images["addition"], **BTN_PROPERTIES)

    backspace_btn = tkinter.Button(root, name="backspace_btn",
                                   command=None, image=images["backspace"], **BTN_PROPERTIES)

    clear_all_btn = tkinter.Button(root, name="clear_all_btn",
                                   command=lambda: clear_screen(calculator_screen_var, state=0), image=images["clear_all"], **BTN_PROPERTIES)

    clear_digit_btn = tkinter.Button(root, name="clear_digit_btn",
                                     command=lambda: clear_screen(calculator_screen_var, state=1), image=images["clear_digit"], **BTN_PROPERTIES)

    close_parentheses_btn = tkinter.Button(root, name="close_parentheses_btn",
                                           command=None, image=images["close_parentheses"], **BTN_PROPERTIES)

    divide_btn = tkinter.Button(root, name="divide_btn",
                                command=None, image=images["divide"], **BTN_PROPERTIES)

    dot_btn = tkinter.Button(root, name="dot_btn",
                             command=None, image=images["dot"], **BTN_PROPERTIES)

    equal_btn = tkinter.Button(root, name="equal_btn",
                               command=None, image=images["equal_btn"], **BTN_PROPERTIES)

    multiply_btn = tkinter.Button(root, name="multiply_btn",
                                  command=None, image=images["multiply"], **BTN_PROPERTIES)

    open_parentheses_btn = tkinter.Button(root, name="open_parentheses_btn",
                                          command=None, image=images["open_parentheses"], **BTN_PROPERTIES)

    percentage_btn = tkinter.Button(root, name="percentage_btn",
                                    command=None, image=images["percentage"], **BTN_PROPERTIES)

    positive_negative_btn = tkinter.Button(root, name="positive_negative_btn",
                                           command=None, image=images["positive_negative"], **BTN_PROPERTIES)

    subtraction_btn = tkinter.Button(root, name="subtraction_btn",
                                     command=None, image=images["subtraction"], **BTN_PROPERTIES)

    num0_btn = tkinter.Button(root, name="num0_btn",
                              command=lambda: print_to_screen("0", calculator_screen_var), image=images["num0"], **BTN_PROPERTIES)

    num1_btn = tkinter.Button(root, name="num1_btn",
                              command=lambda: print_to_screen("1", calculator_screen_var), image=images["num1"], **BTN_PROPERTIES)

    num2_btn = tkinter.Button(root, name="num2_btn",
                              command=lambda: print_to_screen("2", calculator_screen_var), image=images["num2"], **BTN_PROPERTIES)

    num3_btn = tkinter.Button(root, name="num3_btn",
                              command=lambda: print_to_screen("3", calculator_screen_var), image=images["num3"], **BTN_PROPERTIES)

    num4_btn = tkinter.Button(root, name="num4_btn",
                              command=lambda: print_to_screen("4", calculator_screen_var), image=images["num4"], **BTN_PROPERTIES)

    num5_btn = tkinter.Button(root, name="num5_btn",
                              command=lambda: print_to_screen("5", calculator_screen_var), image=images["num5"], **BTN_PROPERTIES)

    num6_btn = tkinter.Button(root, name="num6_btn",
                              command=lambda: print_to_screen("6", calculator_screen_var), image=images["num6"], **BTN_PROPERTIES)

    num7_btn = tkinter.Button(root, name="num7_btn",
                              command=lambda: print_to_screen("7", calculator_screen_var), image=images["num7"], **BTN_PROPERTIES)

    num8_btn = tkinter.Button(root, name="num8_btn",
                              command=lambda: print_to_screen("8", calculator_screen_var), image=images["num8"], **BTN_PROPERTIES)

    num9_btn = tkinter.Button(root, name="num9_btn",
                              command=lambda: print_to_screen("9", calculator_screen_var), image=images["num9"], **BTN_PROPERTIES)

    # place the buttons:

    # first column:
    backspace_btn.place(x=13, y=125)
    num7_btn.place(x=9, y=207)
    num4_btn.place(x=11, y=289)
    num1_btn.place(x=11, y=366)
    num0_btn.place(x=14, y=445)

    # second column:
    clear_all_btn.place(x=94, y=125)
    num8_btn.place(x=92, y=207)
    num5_btn.place(x=92, y=285)
    num2_btn.place(x=92, y=363)

    # third column:
    clear_digit_btn.place(x=179, y=124)
    num9_btn.place(x=178, y=207)
    num6_btn.place(x=178, y=287)
    num3_btn.place(x=178, y=366)
    dot_btn.place(x=176, y=448)

    # forth column:
    positive_negative_btn.place(x=264, y=125)
    divide_btn.place(x=264, y=209)
    multiply_btn.place(x=264, y=287)
    subtraction_btn.place(x=263, y=366)
    addition_btn.place(x=264, y=448)

    # fifth column:
    percentage_btn.place(x=348, y=124)
    open_parentheses_btn.place(x=350, y=207)
    close_parentheses_btn.place(x=350, y=285)
    equal_btn.place(x=350, y=371)

    start_app(root)

    return None


def main():
    main_window()


if __name__ == "__main__":
    main()
