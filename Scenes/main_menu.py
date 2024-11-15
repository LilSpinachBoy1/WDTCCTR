import pygame
import sys
import Modules.ui as ui
import Modules.characters as chars
import Modules.conversions as cvns
cons = cvns.Conversions()
pygame.init()


def butts():
    print("I <3 Butts")


def scn0_menu(window) -> bool:
    FPS = 60
    clock = pygame.time.Clock()
    running = True
    test_butt = ui.Button(
        butts,
        "This is a butt",
        50,
        (40, 40),
        window,
        box_fill=(0, 255, 255),
        pe_padding=0.5
    )
    coords = cons.dual_pe_to_pi((0, 95))
    dimensions = cons.dual_pe_to_pi((100, 10))
    ground_rect = pygame.Rect(coords, dimensions)
    test_snail = chars.Player(window, (15, 20), [ground_rect], scale=25)
    # SCENE LOOP
    while running:
        # EVENT LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If app closed
                pygame.quit()
                sys.exit()

        # Check Key Presses
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            running = False
            return True  # Set to true so the program ends!

        # Update display
        window.fill((255, 255, 255))
        pygame.draw.rect(window, (0, 255, 0), ground_rect)
        test_butt.out()
        test_snail.out()
        pygame.display.update()
        clock.tick(FPS)
    return False  # Set to false so program does not end!
