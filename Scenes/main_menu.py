import pygame
import sys
import Modules.ui as ui
pygame.init()


def scn0_menu(window) -> bool:
    FPS = 60
    clock = pygame.time.Clock()
    running = True
    test_text = ui.Text("Hello", 50, (40, 40), window)
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
        test_text.out()
        pygame.display.update()
        clock.tick(FPS)
    return False  # Set to false so program does not end!
