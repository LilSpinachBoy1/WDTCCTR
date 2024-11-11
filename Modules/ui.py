"""
UI MODULE: Holds classes for useful assets like text and buttons
"""
# Import myyyyy stuff
import Modules.conversions as con

# Setup pygame
import pygame
pygame.init()

# Constants - Note: File addresses are relative to main.py, not this script
BASE_FILE_ADDR = "Assets/Fonts/"

# Set up conversions
conv = con.Conversions()


# Class for basic text
class Text:
    def __init__(self, text: str, size: int, coords: (float, float), surf: pygame.Surface, colour: (int, int, int) = (0, 0, 0), font: str = "PlayfulTime-BLBB8.ttf") -> None:
        """ Initialises a text object

        :param text: The text to be displayed
        :param size: The size of the text
        :param coords: The position of the text, passed in as a percentage, to be converted to actual pixel values
        :param surf: The surface to render the text to
        :param colour: The colour of the text, passed as an RGB value
        :param font: The font to use, just the file name, as the file path will be attached bellow
        """
        # Error handling: ensure font can be found and created
        try:
            self.surface = surf
            self.colour = colour
            self.font_addr = BASE_FILE_ADDR + font  # Create full font address
            self.font_obj = pygame.font.Font(self.font_addr, size)  # Create an object of the target font

            # Create the text object and get the rect of it
            self.text_obj = self.font_obj.render(text, True, colour)
            self.text_rect = self.text_obj.get_rect()
            self.pi_coords = conv.dual_pe_to_pi(coords)
            self.text_rect.topleft = self.pi_coords

        except FileNotFoundError as e:
            print(f"ERROR: Unable to find font for text...\n{e}")

    def update_text(self, new_text: str) -> None:
        self.text_obj = self.font_obj.render(new_text, True, self.colour)
        self.text_rect = self.text_obj.get_rect()

    def out(self):
        self.surface.blit(self.text_obj, self.text_rect)


class Button:
    def __init__(self, func, text: str, text_size: int, pe_coords: (float, float), surf: pygame.surface, text_colour: (int, int, int) = (0, 0, 0), box_fill: (int, int, int) = (255, 255, 255), box_line: (int, int, int) = (0, 0, 0)):
        """
        Class to create a functioning button
        :param func: The function to run on press of the button
        :param text: The text to display on the button
        :param text_size: The size of the text
        :param pe_coords: The percentage coordinates of the button
        :param surf: The surface to draw to
        :param text_colour: The colour of the text passed as RGB, defaults to black
        :param box_fill: The fill colour of the button passed as RGB, defaults to white
        :param box_line: The outline colour of the button passed as RGB, defaults to black
        """
        self.text = Text(text, text_size, pe_coords, surf, colour=text_colour)
        #TODO: Create rect to use as button
