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

pygame.init()


class Calculator:
    """
        The main window for the calculator;
    """

    SIZE = [350, 512]
    WIDTH, HEIGHT = SIZE

    BACKGROUND_COLOR = (0, 0, 0)
    ICON = ""

    TITLE = "Calculator"

    CURSOR_IMAGE = pygame.image.load(r"./pictures/cursor/cursor.png")

    def __init__(self, *args):

        # and make sure to remove the frame;
        self.window = pygame.display.set_mode(Calculator.SIZE, pygame.NOFRAME)
        self.running = True

        # hide the the mouse cursor first;
        pygame.mouse.set_visible(False)

        # now create the cursor;
        self.mouse_cursor = Calculator.CURSOR_IMAGE.get_rect()

    def draw(self):
        """
            draw the calculator;

            return None;
        """

        self.window.fill(Calculator.BACKGROUND_COLOR)
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

        return None


def main():

    Calculator().start()


if __name__ == "__main__":
    main()
