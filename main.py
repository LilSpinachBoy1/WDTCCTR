import sys
import pygame
pygame.init()

# CREATE WINDOW, FULLSCREEN
screen_data = pygame.display.get_desktop_sizes()
window = pygame.display.set_mode((screen_data[0]))
pygame.display.set_caption('How it feels to chew 5 gum')


# Scene manager class
class SceneManager:
    def __init__(self):
        self.curr_scene = "0 - Menu"
        self.quit = False

    def scn0_menu(self):
        FPS = 60
        clock = pygame.time.Clock()
        running = True
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
                self.quit = True  # Set to true so the program ends!

            # Update display
            window.fill((255, 255, 255))
            pygame.display.update()
            clock.tick(FPS)

        print("Left loop")

    def scene_runner(self):
        while not self.quit:
            if self.curr_scene == "0 - Menu":
                self.scn0_menu()
        print("Quit!")


# RUNS FROM HERE
scn_mng = SceneManager()
scn_mng.scene_runner()
pygame.quit()
sys.exit()
