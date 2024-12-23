import Scenes.main_menu
import Modules.file_handling as fh
import sys
import pygame
pygame.init()

# GET SCREEN DIMENSIONS AND UPDATE USERDATA FILE
screen_data = pygame.display.get_desktop_sizes()
fh.Manager().write_settings({"screen_res": screen_data[0]})


# CREATE WINDOW, FULLSCREEN
window = pygame.display.set_mode((screen_data[0]))
pygame.display.set_caption('How it feels to chew 5 gum')


# Scene manager class
class SceneManager:
    def __init__(self):
        self.curr_scene = "0 - Menu"
        pygame.display.set_caption("MAIN MENU")
        self.quit = False

    def scene_runner(self):
        while not self.quit:
            if self.curr_scene == "0 - Menu":
                if Scenes.main_menu.scn0_menu(window):  # Run main menu, and check if the program should quit
                    self.quit = True


# RUNS FROM HERE
scn_mng = SceneManager()
scn_mng.scene_runner()
pygame.quit()
sys.exit()
