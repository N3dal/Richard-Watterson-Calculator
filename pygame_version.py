#!/usr/bin/python3
# -----------------------------------------------------------------
#
# richard-watterson calculator clone using pygame;
#
#
# Author:N84.
#
# Create Date:Mon Mar 20 02:13:26 2023.
# ///
# ///
# ///
# -----------------------------------------------------------------

import pygame
from sys import exit

pygame.init()


class Button:
    """
        Custom button;
    """

    def __init__(self, parent, coords: tuple, func=None, args: tuple = None, text="", image=None):

        self.parent = parent
        self.text = text
        self.image = image
        self.func = func
        self.args = args

        self.x, self.y = coords

        # get the width and the height of the button;
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self):
        """
            draw the button on the parent window;

            return None;
        """
        self.parent.blit(self.image, (self.x, self.y))

    def move(self, x: int, y: int):
        """
            move the button on the parent window;
            x=> int;
            y=> int;

            return None;
        """
        self.x = x
        self.y = y

    def mouse_click_event(self, mouse_x: int, mouse_y: int):
        """
            check if the mouse is on the button and then,
            call the command when we click on the button;

            return None;
        """

        EXTRA_SPACE = 1

        # check out if we on the button or not;
        if mouse_x in range(self.x, self.x+self.width + EXTRA_SPACE) and mouse_y in range(self.y, self.y + self.height + EXTRA_SPACE):

            if self.args is None:
                self.func()

            else:
                self.func(*self.args)

        return None


class TitleBar:
    """
        Docstring;
    """
    TITLE_IMAGE = pygame.image.load(r"./pictures/title_bar/title.png")
    MINIMIZE_IMAGE = pygame.image.load(r"./pictures/title_bar/minimize.png")
    MAXIMIZE_IMAGE = pygame.image.load(r"./pictures/title_bar/maximize.png")
    CLOSE_IMAGE = pygame.image.load(r"./pictures/title_bar/close.png")

    MINIMIZE_IMAGE_COORDS = (320, 10)
    MAXIMIZE_IMAGE_COORDS = (360, 10)
    CLOSE_IMAGE_COORDS = (400, 10)

    def __init__(self, parent):

        self.parent = parent
        self.minimize_btn = Button(
            parent=self.parent,
            coords=TitleBar.MINIMIZE_IMAGE_COORDS,
            image=TitleBar.MINIMIZE_IMAGE,
            func=self.minimize_event)

        self.maximize_btn = Button(
            parent=self.parent,
            coords=TitleBar.MAXIMIZE_IMAGE_COORDS,
            image=TitleBar.MAXIMIZE_IMAGE,
            func=self.maximize_event)

        self.close_btn = Button(
            parent=self.parent,
            coords=TitleBar.CLOSE_IMAGE_COORDS,
            image=TitleBar.CLOSE_IMAGE,
            func=self.close_event)

    def draw(self):
        """
            draw the title bar;
        """

        self.parent.blit(TitleBar.TITLE_IMAGE, (15, 15))
        self.minimize_btn.draw()
        self.maximize_btn.draw()
        self.close_btn.draw()

    def close_event(self):
        exit(0)

    def minimize_event(self):
        print("minimize!!")

    def maximize_event(self):
        print("maximize!!")


class Calculator:
    """
        The main window for the calculator;
    """

    SIZE = [442, 538]
    WIDTH, HEIGHT = SIZE

    BACKGROUND_COLOR = (228, 231, 236)
    ICON = ""

    TITLE = "Calculator"

    CURSOR_IMAGE = pygame.image.load(r"./pictures/cursor/cursor.png")
    FRAME_IMAGE = pygame.image.load(r"./pictures/frame.png")

    def __init__(self, *args):

        # and make sure to remove the frame;
        self.window = pygame.display.set_mode(Calculator.SIZE, pygame.NOFRAME)
        self.running = True

        # hide the the mouse cursor first;
        pygame.mouse.set_visible(False)

        # now create the cursor;
        self.mouse_cursor = Calculator.CURSOR_IMAGE.get_rect()

        self.title_bar = TitleBar(parent=self.window)

    def draw(self):
        """
            draw the calculator;

            return None;
        """

        self.window.fill(Calculator.BACKGROUND_COLOR)
        self.window.blit(Calculator.FRAME_IMAGE, (0, 0))
        self.title_bar.draw()
        self.draw_cursor()

        pygame.display.update()

        return None

    def draw_cursor(self):
        """
            draw the mouse cursor on the screen;

            return None;
        """

        self.mouse_cursor.center = pygame.mouse.get_pos()
        self.window.blit(Calculator.CURSOR_IMAGE, self.mouse_cursor)

        return None

    def start(self):
        """
            start the calculator;

            return None;
        """

        while self.running:

            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:

                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.title_bar.minimize_btn.mouse_click_event(
                        mouse_x=mouse_x, mouse_y=mouse_y)

                    self.title_bar.maximize_btn.mouse_click_event(
                        mouse_x=mouse_x, mouse_y=mouse_y)

                    self.title_bar.close_btn.mouse_click_event(
                        mouse_x=mouse_x, mouse_y=mouse_y)

        return None


def main():

    Calculator().start()


if __name__ == "__main__":
    main()
