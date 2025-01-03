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


def collision_check(player: pygame.Rect, item: pygame.Rect) -> dict:
    # VERTICAL COLLISIONS
    # NOTE: This is relative to the x location of the player, so will only return collisions if the player is within the x range of the rect
    x_range = range(item.left, item.right)
    if player.left in x_range or player.right in x_range:
        top_collision: bool = player.top > item.bottom
        bottom_collision: bool = player.bottom > item.top
    else:
        top_collision: bool = False
        bottom_collision: bool = False

    # HORIZONTAL COLLISIONS
    # NOTE: These checks only run if the focus is within the y range of the rect, to prevent returning collisions with a rect the player is vertically over or under
    check_range = range(item.top + 2, item.bottom)  # This plus 2 is just so setting the player to the ground doesn't trigger collisions
    if player.bottom in check_range or player.top in check_range:
        left_collision: bool = player.left < item.right
        right_collision: bool = player.right > item.left
    else:
        left_collision: bool = False
        right_collision: bool = False

    # POPULATING DICT
    collisions = {"Top": top_collision, "Bottom": bottom_collision, "Left": left_collision, "Right": right_collision}
    if top_collision or bottom_collision or left_collision or right_collision:  # If there is a collision
        collisions["Rect"] = item
    return collisions


# Procedure to set the character rect to the top of the ground rect
def set_to_ground(focus: pygame.Rect, item: pygame.Rect) -> None:
    focus.bottom = item.top


class Player(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.Surface, pe_coords: (float, float), ground_list: list, h_collisions_list: list = None, scale: int = 30):
        """
        Class for the player character
        :param surface: The surface to blit the player to
        :param pe_coords: The starting coordinates for the player
        :param ground_list: The list of rects that the player can collide with (VERTICALLY)
        :param h_collisions_list: The list of rects that the player can collide with (HORIZONTALLY), defaults to none, and is set to be same as ground rects if not provided
        :param scale: Scale of the image to use
        """
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
        self.is_h_collision = False  # Holds weather there is a horizontal collision
        self.horizontal_movement = 0  # Holds the direction of movement
        self.vertical_speed = 0  # Holds the magnitude and direction of movement
        self.GRAVITY = 0.6
        self.JUMP_STRENGTH = -20  # This needs to be negative so the character moves upwards
        self.SPEED_DEF_VALUE = 4  # Default speed value
        self.speed = self.SPEED_DEF_VALUE  # Speed value that can be changed
        self.direction = "+"
        self.ground_list = ground_list
        self.collided_rects = []
        self.pressed = pygame.key.get_pressed()  # Gets the current input status
        if h_collisions_list: self.h_collision_rects = h_collisions_list
        else: self.h_collision_rects = self.ground_list

    def movement(self):
        """ COLLISIONS """
        # Check horizontal collisions
        self.is_h_collision = False
        for rect in self.h_collision_rects:
            state = collision_check(self.rect, rect)
            if state["Left"] or state["Right"]:
                self.is_h_collision = True
                self.horizontal_movement = -1
                break  # Leave the for loop if a collision is found

        # Check vertical collisions
        self.is_grounded = False
        for rect in self.ground_list:
            ground_state = collision_check(self.rect, rect)
            if ground_state["Bottom"]:
                self.is_grounded = True
                self.vertical_speed = 0
                collision_rect = ground_state["Rect"]
                break  # Leave the for loop if a collision is found

        # Determine weather the player needs to be moved upwards
        if self.is_h_collision and self.is_grounded:
            self.vertical_speed = 0
        else:
            set_to_ground(self.rect, collision_rect)

        """ MOVEMENT """
        pressed = pygame.key.get_pressed()  # get the currently pressed keys

        # Only allow horizontal movement if there is no collision
        new_direction = self.direction
        if not self.is_h_collision:
            if pressed[K_a]:
                self.horizontal_movement = -self.speed
                new_direction = "-"
            elif pressed[K_d]:
                self.horizontal_movement = self.speed
                new_direction = "+"

        # Change player direction if necessary
        if self.direction != new_direction:
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction = new_direction

        # Jumping
        if pressed[K_w] and self.is_grounded:
            self.vertical_speed += self.JUMP_STRENGTH

        """ ADJUST COORDINATES """
        self.coords[0] += self.horizontal_movement
        self.coords[1] += self.vertical_speed

    def out(self):
        self.pressed = pygame.key.get_pressed()
        self.movement()
        self.rect.bottomleft = self.coords
        self.screen.blit(self.image, self.rect)
