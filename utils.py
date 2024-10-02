"""PYTHON UTILS MODULE
Contains useful functions for pygame
"""

# Import pygame and get display info
import pygame
pygame.init()
display_inf = pygame.display.Info()


def pe2pi(percent) -> tuple:
    """Function to convert percentage screen values to pixels

    :param percent: percentages of screen to convert to pixels
    :return tuple: the passed in percentages, converted to exact pixel coordinates
    """

    height = (percent[1] * 0.01) * display_inf.current_h
    width = (percent[0] * 0.01) * display_inf.current_w
    return int(width), int(height)


def pe2piSINGLE(percent: float, is_width: bool) -> int:
    if is_width:
        x = display_inf.current_w
    else:
        x = display_inf.current_h
    return int(x * percent * 0.01)


def pi2pe(pixels: tuple) -> tuple:
    """ Function to convert exact pixel coordinates to percentages

    :param pixels: the coordinates to convert, as the pixels of the screen
    :return tuple: the passed in pixels, converted to percentage coordinates
    """

    height = (pixels[1] / display_inf.current_h) * 100
    width = (pixels[0] / display_inf.current_w) * 100
    return int(width), int(height)


def pi2peSINGLE(pixels: int, is_width: bool) -> float:
    if is_width:
        x = display_inf.current_w
    else:
        x = display_inf.current_h
    return float(x * pixels * 0.01)


class Enemy:
    def __init__(self, start_y: int, move_range_pcnt: int) -> None:
        self.move_cap = 10 + move_range_pcnt
        self.coords = [10, start_y]  # Written in percentages
        self.direction = 1
        self.rect = pygame.Rect(*pe2pi(self.coords), pe2piSINGLE(5, True), pe2piSINGLE(5, True))

    def process_move(self, speed: int) -> None:
        # Move the enemy based on the current direction
        self.coords[0] += speed * self.direction

        # If we reach the boundaries, reverse direction
        if self.coords[0] >= self.move_cap:
            self.direction = -1  # Move left
        elif self.coords[0] <= 10:
            self.direction = 1  # Move right

    def check_collide(self, player) -> bool:
        return self.rect.colliderect(player)

    def update(self, SURF: pygame.Surface, COLOUR: tuple) -> None:
        self.rect = pygame.Rect(*pe2pi(self.coords), pe2piSINGLE(5, True), pe2piSINGLE(5, True))
        pygame.draw.rect(SURF, COLOUR, self.rect)


# TEST HERE
if __name__ == "__main__":
    pass
