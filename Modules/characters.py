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
    top_collision: bool = player.top > item.bottom
    bottom_collision: bool = player.bottom > item.top

    # HORIZONTAL COLLISIONS
    # NOTE: These checks only run if the focus is within the y range of the rect, to prevent returning collisions with a rect the player is vertically over or under
    check_range = range(item.top + 2, item.bottom)  # This plus 2 is just so setting the player to the ground does'nt trigger collisions
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
        if h_collisions_list: self.h_collision_rects = h_collisions_list
        else: self.h_collision_rects = self.ground_list

    def movement(self) -> None:
        # Find if the player is grounded, and if not add gravity
        collided_indices = self.rect.collidelistall(self.ground_list)
        if collided_indices:
            self.is_grounded = True
            self.vertical_speed = 0
            collided_rects = [self.ground_list[i] for i in collided_indices]
        else:
            self.is_grounded = False
            self.vertical_speed += self.GRAVITY
            collided_rects = []

        pressed = pygame.key.get_pressed()

        # Boing
        if self.is_grounded and pressed[K_w]:
            self.vertical_speed = self.JUMP_STRENGTH

        # Horizontal movement
        if pressed[K_a]:
            self.horizontal_movement = -self.speed
            new_direction = "-"
        elif pressed[K_d]:
            self.horizontal_movement = self.speed
            new_direction = "+"
        else:
            new_direction = self.direction  # If no movement, keep the current direction
            self.horizontal_movement = 0

        # Check collisions against all recs used for horizontal collisions
        for rect in self.h_collision_rects:
            collision_state = collision_check(self.rect, rect)
            print(collision_state)
            if rect not in collided_rects:
                if collision_state["Left"]:
                    self.is_h_collision = True
                    self.horizontal_movement = 1
                elif collision_state["Right"]:
                    self.is_h_collision = True
                    self.horizontal_movement = -1
                else:
                    self.is_h_collision = False
            else: self.is_h_collision = False
        print("----------------")

        # Determine if image needs to be flipped based on movement direction
        if self.direction != new_direction:
            self.direction = new_direction
            self.image = pygame.transform.flip(self.image, flip_y=False, flip_x=True)

        # Add movement based on speed values
        self.coords[0] += self.horizontal_movement  # X COORDINATE
        if self.is_grounded: self.coords[1] = collided_rects[0].top
        else: self.coords[1] += self.vertical_speed

    def out(self):
        self.movement()
        self.rect.bottomleft = self.coords
        self.screen.blit(self.image, self.rect)
