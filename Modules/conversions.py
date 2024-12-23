"""
CONVERSIONS MODULE: Holds a class to handle conversions between percentages and coordinate values
"""
import Modules.file_handling as fh

# Get the data from settings
FileManager = fh.Manager("UserData/")
all_data = FileManager.read_settings()
screen_data = all_data["screen_res"]


class Conversions:
    # Get the screen data to keep locally
    def __init__(self):
        self.screen_width = int(screen_data[0])
        self.screen_height = int(screen_data[1])

    # Take a pair of coordinates and convert them TO PIXEL VALUES
    def dual_pe_to_pi(self, coords: (float, float)) -> (int, int):
        pi_width = (coords[0] / 100) * self.screen_width
        pi_height = (coords[1] / 100) * self.screen_height
        return int(pi_width), int(pi_height)

    # Take a pair of coordinates and convert them TO PERCENTAGE VALUES
    def dual_pi_to_pe(self, coords: (int, int)) -> (float, float):
        pe_width = (coords[0] / self.screen_width) * 100
        pe_height = (coords[1] / self.screen_height) * 100
        return pe_width, pe_height

    # Take a single percentage, and convert it TO A PIXEL VALUE
    def pe_to_pi(self, pe: float, is_width: bool) -> int:
        mult = self.screen_width if is_width else self.screen_height
        return int((pe / 100) * mult)

    # Take a single pixel pos, and convert it TO A PERCENTAGE
    def pi_to_pe(self, pi: int, is_width: bool) -> float:
        div = self.screen_width if is_width else self.screen_height
        return (pi / div) * 100
