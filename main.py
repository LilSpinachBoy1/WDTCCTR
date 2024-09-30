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
v_location, h_location = 50, 50
player_speed = 1
cycle_num = 0  # This is used to prevent spamming of commands
STD_INP_BUFFER = 15  # Puts a buffer of 15 cycles on chosen inputs (0.25 seconds)
last_update = -STD_INP_BUFFER  # Last cycle in which the speed was updated, initially -buffer to negate start buffer
while running:
    cycle_num += 1
    
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

    # Draw (REF3)
    WINDOW.fill(RED)
    coords = (h_location, v_location)
    pygame.draw.rect(WINDOW, GREEN, (*utils.pe2pi(display_inf, coords), 100, 100))

    # Update (REF4)
    FPS_CLOCK.tick(FRAME_RATE)
    pygame.display.update()
