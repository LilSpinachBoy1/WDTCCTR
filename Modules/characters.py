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
    def __init__(self, surface: pygame.Surface, pe_coords: (float, float), scale: int = 30):
        super(Player, self).__init__()
        self.image = pygame.image.load("Assets/Sprites and Animations/Snail/SN_idle.png")  # Import idle snail image
        self.img_scale = scale  # Set the size for the image
        self.image_target_size = (cvt.pe_to_pi(self.img_scale, True), cvt.pe_to_pi(self.img_scale, True))  # Store the target dimensions for the image
        self.image = pygame.transform.scale(self.image, self.image_target_size)  # Resize the image
        self.rect = self.image.get_rect()  # Get the rect for the image to use for coordinates
        self.coords = list(cvt.dual_pe_to_pi(pe_coords))
        self.rect.bottomleft = self.coords  # Set position of rect
        self.screen = surface  # Store the surface to blit to

        # Movement based attributes
        self.is_moving = False  # Used to control animations
        self.vertical_movement = 0
        self.speed = 1
        self.direction = "+"

    def process_movement(self):
        # Set flag for if movement is occurring, in order to determine if an animation should run
        pressed = pygame.key.get_pressed()  # Gets all keys pressed
        self.is_moving = any(pressed[key] for key in movement_keys)  # Sets true if any of the keys in movement_keys are currently pressed

        # Move the sprite based on inputs
        new_direction = self.direction
        if pressed[K_d]:
            self.vertical_movement = self.speed
            new_direction = "+"
        elif pressed[K_a]:
            self.vertical_movement = -self.speed
            new_direction = "-"
        self.coords[0] += self.vertical_movement  # Change x coordinate based on vertical movement variable
        self.rect.bottomleft = self.coords  # Apply coordinate change to rect position
        self.vertical_movement = 0  # End movement if no keys are pressed

        # Determine if image needs to be flipped
        if self.direction != new_direction:
            self.direction = new_direction
            self.image = pygame.transform.flip(self.image, flip_y=False, flip_x=True)

    def out(self):
        self.process_movement()
        self.screen.blit(self.image, self.rect)
