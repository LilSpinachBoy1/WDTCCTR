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
    def __init__(self, func, text: str, text_size: int, pe_coords: (float, float), surf: pygame.surface, text_colour: (int, int, int) = (0, 0, 0), box_fill: (int, int, int) = (255, 255, 255), box_line: (int, int, int) = (0, 0, 0), pe_padding: float = 0.5):
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
        :param pe_padding: The percentage padding of the button, defaults to 0.5
        """
        # Create the text to use
        self.text = Text(text, text_size, pe_coords, surf, colour=text_colour)

        # Get positional values for rects and for text
        self.box_topleft = conv.dual_pe_to_pi(pe_coords)  # Store the topleft coordinates of the box
        pi_padding = conv.dual_pe_to_pi((pe_padding, pe_padding))  # Store the pixel values of padding to add to the text, not self. as it is only used here
        self.text.text_rect.topleft = (self.box_topleft[0] + pi_padding[0], self.box_topleft[1] + pi_padding[1])  # Set the text position

        # Create 2 rects, one as the background, and one as the border
        self.bg_rect = pygame.Rect(self.box_topleft, (self.text.text_rect.width + (2 * pi_padding[0]), self.text.text_rect.height + (2 * pi_padding[1])))  # Create box rect
        self.border_rect = pygame.Rect(self.box_topleft, self.bg_rect.size)  # Create a rect the same as the bg_rect, to be used for the outline

        # Store various other parameters as attributes to use later!
        self.function, self.surf, self.fill_colour, self.outline_colour = func, surf, box_fill, box_line  # Set a load of attributes in one, cus why not

        # Store the valid range of inputs: (low, high)
        self.inp_range_x = range(self.bg_rect.topleft[0], self.bg_rect.topright[0], 1)
        self.inp_range_y = range(self.bg_rect.topleft[1], self.bg_rect.bottomright[1], 1)

    def out(self):
        # Draw the rects and text
        pygame.draw.rect(self.surf, self.fill_colour, self.bg_rect)  # Draw Background rect
        pygame.draw.rect(self.surf, self.outline_colour, self.border_rect, width=2)
        self.text.out()

        # --- Handle processing of functions ---
        # Get details about the mouse usage
        mouse_pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        if pressed[0]:  # Check if the mouse button is pressed: left click
            if mouse_pos[0] in self.inp_range_x and mouse_pos[1] in self.inp_range_y:  # Check if the pointer is in range of the button
                self.function()
