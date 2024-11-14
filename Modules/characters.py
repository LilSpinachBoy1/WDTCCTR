"""
MODULE THAT WILL CONTAIN CLASSES FOR PLAYER AND ENEMY CHARACTERS
"""
import Modules.conversions as cons
import pygame
from pygame.locals import (
    K_w,
    K_a,
    K_s,
    K_d
)
movement_keys = [K_w, K_a, K_s, K_d]
pygame.init()

cvt = cons.Conversions()


class Player(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.Surface, pe_coords: (float, float)):
        super(Player, self).__init__()
        self.image = pygame.image.load("Assets/Sprites and Animations/Snail/SN_idle.png")  # Import idle snail image
        self.img_scale = 30  # Set the size for the image
        self.image_target_size = (cvt.pe_to_pi(self.img_scale, True), cvt.pe_to_pi(self.img_scale, True))  # Store the target dimensions for the image
        self.image = pygame.transform.scale(self.image, self.image_target_size)  # Resize the image
        self.rect = self.image.get_rect()  # Get the rect for the image to use for coordinates
        self.rect.topleft = cvt.dual_pe_to_pi(pe_coords)  # Set position of rect
        self.screen = surface  # Store the surface to blit to

        # Movement based attributes
        self.is_moving = False  # Used to control animations
        self.vertical_movement = 0

    def process_movement(self):
        events = pygame.event.get()
        # TODO: This doesnt work
        for event in events:
            if event.type == pygame.KEYDOWN and event.key in movement_keys:
                self.is_moving = True
            if event.type == pygame.KEYUP and event.key in movement_keys:
                self.is_moving = False

        print(self.is_moving)

    def out(self):
        self.process_movement()
        self.screen.blit(self.image, self.rect)
