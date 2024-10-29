"""
FILE HANDLING MODULE: Holds functions to read and write to files
"""

# File location constants. NOTE: Files relative to main.py, not here
USERDATA_ROOT = "UserData/"
TESTING_ROOT = "../UserData/"
SETTINGS = "settings.txt"

"""
A NOTE ON THE SETTINGS FILE:
The first line of data is the screen resolution, by default full screen, but may be changed by the user
"""
lines = 1


# Read settings
#TODO: Change to just read the dict from the file, and then return to non testing form
def read_settings() -> dict:
    # Get all the data from settings
    settings_addr = TESTING_ROOT + SETTINGS
    file = open(settings_addr, "r")

    # Get screen resolution values and use location of comma to convert to usable values
    screen_res = file.readline()
    comma_index = 0
    for i in range(len(screen_res)):
        if screen_res[i] == ",":
            comma_index = i
    screen_x, screen_y = screen_res[:comma_index], screen_res[comma_index+1:]

    # Close file, as we are finished
    file.close()

    # Store the data in a dict
    return {
        "screen_res": (int(screen_x), int(screen_y))
    }


def write_settings(data: dict) -> None:
    settings_addr = USERDATA_ROOT + SETTINGS
    file = open(settings_addr, "w")
    file.write(str(data))
    file.close()


t_data = read_settings()
print(t_data["screen_res"])
