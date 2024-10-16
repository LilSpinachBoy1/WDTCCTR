import pygame
import conversions
pygame.init()


class Text:
    def __init__(self, text: str, size: int, pos: tuple) -> None:
        self.font = pygame.font.Font(None, size)  # Use default font
        self.text_surface = self.font.render(text, True, pygame.Color('white'))
        self.pos = conversions.pe2pi(pos)

    def update_text(self, new_text: str) -> None:
        self.text_surface = self.font.render(new_text, True, pygame.Color('white'))

    def output(self, surface: pygame.Surface) -> None:
        surface.blit(self.text_surface, self.pos)
