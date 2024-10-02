"""PYTHON UTILS MODULE
Contains useful functions for pygame
"""

import pygame


def pe2pi(screen_data, percent: tuple) -> tuple:
    """Function to convert percentage screen values to pixels

    :param screen_data: gathered screen data, inc. width and height
    :param percent: percentages of screen to convert to pixels
    :return tuple: the passed in percentages, converted to exact pixel coordinates
    """

    height = (percent[1] * 0.01) * screen_data.current_h
    width = (percent[0] * 0.01) * screen_data.current_w
    return int(width), int(height)


def pi2pe(screen_data, pixels: tuple) -> tuple:
    """ Function to convert exact pixel coordinates to percentages

    :param screen_data: gathered screen data, inc. width and height
    :param pixels: the coordinates to convert, as the pixels of the screen
    :return tuple: the passed in pixels, converted to percentage coordinates
    """

    height = (pixels[1] / screen_data.current_h) * 100
    width = (pixels[0] / screen_data.current_w) * 100
    return int(width), int(height)


class Enemy:
    def __init__(self, start_y):
        self.rect = pygame.Rect(50, start_y, 50, 50)

    def process_move(self):
            pass  # Finish this later

    def update(self, SURF, COLOUR):
        pygame.draw.rect(SURF, COLOUR, self.rect)


# TEST HERE
if __name__ == "__main__":
    pass

