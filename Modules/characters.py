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


def collision_check(focus: pygame.Rect, item: pygame.Rect) -> dict:
    top_collision: bool = focus.top < item.bottom
    bottom_collision: bool = focus.bottom > item.top
    left_collision: bool = focus.left < item.right
    right_collision: bool = focus.right > item.left
    collisions = {"Top": top_collision, "Bottom": bottom_collision, "Left": left_collision, "Right": right_collision}
    if top_collision or bottom_collision or left_collision or right_collision:  # If there is a collision
        collisions["Rect"] = item
    return collisions


def vertical_collision_check(focus: pygame.Rect, ground: list) -> dict:
    current_rects_y = []  # List to store the y values of the rects that the player is over

    # Find all the rects that the player is over
    for rect in ground:  # Check each rect in the list
        x_range = range(rect.left, rect.right)  # Get the range of x values for the current rect
        if focus.left in x_range or focus.right in x_range:  # Check if the focus rect is within the x range of the current rect
            current_rects_y.append([rect, rect.top])  # If it is, add the y value of the current rect to the list

    # Find the highest rect that the player is over
    highest_rect = None  # Initialize the variable to store the highest rect
    for rect in current_rects_y:  # Check each rect in the list
        if highest_rect is None:  # If the highest rect is not set, set it to the current rect
            highest_rect = rect
        elif rect[1] < highest_rect[1]:  # If the current rect is higher than the highest rect, set the highest rect to the current rect
            highest_rect = rect

    # Check if the player is colliding with the highest rect
    if highest_rect is not None:  # If the highest rect is set
        current_collision_state = collision_check(focus, highest_rect[0])  # Check if the player is colliding with the highest rect
        return current_collision_state  # Return the collision state
    else:  # If the highest rect is not set
        return {"Top": False, "Bottom": False, "Left": False, "Right": False, "Rect": None}  # Return that the player is not colliding with anything


# Procedure to set the character rect to the top of the ground rect
def set_to_ground(focus: pygame.Rect, item: pygame.Rect) -> None:
    focus.bottom = item.top


class Player(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.Surface, pe_coords: (float, float), ground_list: list, h_collisions_list: list, scale: int = 30):
        """
        Class for the player character
        :param surface: The surface to blit the player to
        :param pe_coords: The starting coordinates for the player
        :param ground_list: The list of rects that the player can collide with (VERTICALLY)
        :param h_collisions_list: The list of rects that the player can collide with (HORIZONTALLY)
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
        self.horizontal_movement = 0  # Holds the direction of movement
        self.vertical_speed = 0  # Holds the magnitude and direction of movement
        self.GRAVITY = 0.6
        self.JUMP_STRENGTH = -20  # This needs to be negative so the character moves upwards
        self.SPEED_DEF_VALUE = 4  # Default speed value
        self.speed = self.SPEED_DEF_VALUE  # Speed value that can be changed
        self.direction = "+"
        self.ground_list = ground_list
        self.h_collision_rects = h_collisions_list

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

        # TODO: Move the rect up when it intersects with terrain

        pressed = pygame.key.get_pressed()

        # Boing
        if self.is_grounded and pressed[K_w]:
            self.vertical_speed = self.JUMP_STRENGTH

        # TODO: Implement horizontal collision detection

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

        # Determine if image needs to be flipped based on movement direction
        if self.direction != new_direction:
            self.direction = new_direction
            self.image = pygame.transform.flip(self.image, flip_y=False, flip_x=True)

        # Add movement based on speed values
        self.coords[0] += self.horizontal_movement
        self.coords[1] += self.vertical_speed

    def out(self):
        self.movement()
        self.rect.topleft = self.coords
        self.screen.blit(self.image, self.rect)
