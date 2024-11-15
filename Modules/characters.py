"""
MODULE THAT WILL CONTAIN CLASSES FOR PLAYER AND ENEMY CHARACTERS
"""
import Modules.conversions as cons
import pygame
from pygame.locals import (
    K_w,
    K_a,
    K_d
)
movement_keys = [K_a, K_d]
pygame.init()

cvt = cons.Conversions()


class Player(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.Surface, pe_coords: (float, float), ground_list: list, scale: int = 30):
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
        self.is_grounded = False  # Used to implement gravity
        self.horizontal_movement = 0  # Holds the direction of movement
        self.vertical_speed = 0  # Holds the magnitude and direction of movement
        self.GRAVITY = 0.4
        self.JUMP_STRENGTH = -10  # This needs to be negative so the character moves upwards
        self.SPEED = 2
        self.direction = "+"
        self.ground_list = ground_list

    def vertical_control(self):
        # WHY THE FUCK DOES THIS WORK? How about we just ball with it...
        if not self.rect.collidelist(self.ground_list):  # If the character is grounded
            self.is_grounded = True
            self.vertical_speed = -0.2  # This negative value just means that if the character clips into a rect, it will slowly push its way back up. If it was larger, it would rise quicker, but would cause bouncing at the surface of the rect
        else:
            self.is_grounded = False
            self.vertical_speed += self.GRAVITY

        # Boing time! (Implementing jumping)
        pressed = pygame.key.get_pressed()
        if pressed[K_w] and self.is_grounded:
            self.vertical_speed += self.JUMP_STRENGTH

        # Change the coordinates based on the new movement
        self.coords[1] += self.vertical_speed

    def horizontal_control(self):
        # Set flag for if movement is occurring, in order to determine if an animation should run
        pressed = pygame.key.get_pressed()  # Gets all keys pressed
        self.is_moving = any(pressed[key] for key in movement_keys)  # Sets true if any of the keys in movement_keys are currently pressed

        # Move the sprite based on inputs
        new_direction = self.direction
        if pressed[K_d]:
            self.horizontal_movement = self.SPEED
            new_direction = "+"
        elif pressed[K_a]:
            self.horizontal_movement = -self.SPEED
            new_direction = "-"
        self.coords[0] += self.horizontal_movement  # Change x coordinate based on vertical movement variable
        self.rect.bottomleft = self.coords  # Apply coordinate change to rect position
        self.horizontal_movement = 0  # End movement if no keys are pressed

        # Determine if image needs to be flipped
        if self.direction != new_direction:
            self.direction = new_direction
            self.image = pygame.transform.flip(self.image, flip_y=False, flip_x=True)

    def out(self):
        self.horizontal_control()
        self.vertical_control()
        self.screen.blit(self.image, self.rect)
