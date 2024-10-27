"""
UI MODULE: Holds classes for useful assets like text and buttons
"""
# Setup pygame
import pygame
pygame.init()

# Constants - Note: File addresses are relative to main.py, not this script
BASE_FILE_ADDR = "Assets/Fonts/"

# Class for basic text
class Text:
    def __init__(self, text: str, size: int, coords: (float, float), colour: (int, int, int) = (0, 0, 0), font: str = "PlayfulTime-BLBB8.ttf") -> None:
        """ Initialises a text object

        :param text: The text to be displayed
        :param size: The size of the text
        :param coords: The position of the text, passed in as a percentage, to be converted to actual pixel values
        :param colour: The colour of the text, passed as an RGB value
        :param font: The font to use, just the file name, as the file path will be attached bellow
        """
        # Error handling: ensure font can be found and created
        try:
            self.font_addr = BASE_FILE_ADDR + font  # Create full font address
            self.font_obj = pygame.font.Font(self.font_addr, size)  # Create an object of the target font

            # Create the text object and get the rect of it
            self.text_obj = self.font_obj.render(text, True, colour)
            self.text_rect = self.text_obj.get_rect()

        except FileNotFoundError as e:
            print(f"ERROR: Unable to find font for text...\n{e}")