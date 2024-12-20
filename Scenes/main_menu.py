import pygame
import sys
import Modules.ui as ui
import Modules.characters as chars
import Modules.conversions as cvns
cons = cvns.Conversions()
pygame.init()


def scn0_menu(window) -> bool:
    FPS = 60
    clock = pygame.time.Clock()
    running = True

    # Make ground
    coords = cons.dual_pe_to_pi((0, 95))
    dimensions = cons.dual_pe_to_pi((100, 10))
    ground_rect = pygame.Rect(coords, dimensions)

    # Make more ground
    coords2 = cons.dual_pe_to_pi((70, 85))
    dimensions2 = cons.dual_pe_to_pi((30, 10))
    ground_rect2 = pygame.Rect(coords2, dimensions2)

    # Make even more ground
    coords3 = cons.dual_pe_to_pi((0, 85))
    dimensions3 = cons.dual_pe_to_pi((30, 10))
    ground_rect3 = pygame.Rect(coords3, dimensions3)

    # Make snel
    test_snail = chars.Player(window, (35, 20), [ground_rect, ground_rect2, ground_rect3], scale=25)
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
            return True  # Set to true so the program ends!

        # Update display
        window.fill((255, 255, 255))
        pygame.draw.rect(window, (0, 255, 0), ground_rect)
        pygame.draw.rect(window, (0, 255, 0), ground_rect2)
        pygame.draw.rect(window, (0, 255, 0), ground_rect3)
        test_snail.out()
        pygame.display.update()
        clock.tick(FPS)
    return False  # Set to false so program does not end!
