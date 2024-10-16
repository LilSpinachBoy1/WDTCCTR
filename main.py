""" SPEEDY PYGAME SHIZZZZZ LETS RECAP GANG WOOOOOO """

# Imports
import pygame
from pygame.locals import *
import sys
import utils

# Initialise libraries
pygame.init()

# Set up colour constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create a window and clock
FPS_CLOCK = pygame.time.Clock()
FRAME_RATE = 60
# This way is good because it does not change the resolution of the screen but still goes fullscreen
display_inf = pygame.display.Info()
WINDOW = pygame.display.set_mode((display_inf.current_w, display_inf.current_h))

""" 
THE GAME LOOP:
REF1 - Event loop, deals with all events (e.g: key presses and quitting)
REF2 - Processing. Any calculations or updating of values.
REF3 - Draw. Render display items to the screen
REF4 - Update. Refresh screen and tick clocks.
"""
running = True
v_location, h_location = 90, 45  # THESE VALUES SHOULD BE PERCENTAGES
player_speed = 1
cycle_num = 0  # This is used to prevent spamming of commands
STD_INP_BUFFER = 15  # Puts a buffer of 15 cycles on chosen inputs (0.25 seconds)
last_update = -STD_INP_BUFFER  # Last cycle in which the speed was updated, initially -buffer to negate start buffer

enemy_1 = utils.enemies.Enemy(25, 75)
cycle_count_text = utils.text.Text("placeholder", 100, (2, 2))
while running:
    cycle_num += 1
    seconds = cycle_num // FRAME_RATE
    coords = (h_location, v_location)
    player_rect = pygame.Rect(*utils.conversions.pe2pi(coords), utils.conversions.pe2piSINGLE(5, True), utils.conversions.pe2piSINGLE(5, True))
    finish_rect = pygame.Rect(*utils.conversions.pe2pi((20, 0)), *utils.conversions.pe2pi((60, 10)))

    # Establish movement variables
    v_movement, h_movement = 0, 0
    # Event loop (REF1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:  # Check for keyboard input
            # If escape pressed, send quit event to queue
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    # Processing (REF2)
    keys = pygame.key.get_pressed()
    if keys[K_a]:
        h_movement = -player_speed
    if keys[K_d]:
        h_movement = player_speed
    if keys[K_w]:
        v_movement = -player_speed
    if keys[K_s]:
        v_movement = player_speed

    h_location += h_movement
    v_location += v_movement

    # Update player speed if 1 or 2 are pressed
    if cycle_num >= last_update + STD_INP_BUFFER:
        if keys[K_1]:
            player_speed -= 1
            last_update = cycle_num
        if keys[K_2]:
            player_speed += 1
            last_update = cycle_num

    # COLLISION LOGIC
    is_finished = player_rect.colliderect(finish_rect)  # Player vs finish
    is_hit_enemy1 = enemy_1.check_collide(player_rect)  # Player vs enemy1
    if is_finished or is_hit_enemy1:
        pygame.event.post(pygame.event.Event(QUIT))

    # Update Enemies and Text
    enemy_1.process_move(1)
    cycle_count_text.update_text(f"Time: {str(seconds)}")

    # Draw (REF3)
    WINDOW.fill(BLACK)

    # Draw the target, enemies and text
    pygame.draw.rect(WINDOW, GREEN, finish_rect)
    enemy_1.update(WINDOW, RED)
    cycle_count_text.output(WINDOW)

    # Draw the character
    pygame.draw.rect(WINDOW, BLUE, player_rect)

    # Update (REF4)
    FPS_CLOCK.tick(FRAME_RATE)
    pygame.display.update()
    