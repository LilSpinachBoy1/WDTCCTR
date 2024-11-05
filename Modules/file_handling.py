"""
FILE HANDLING MODULE: Holds functions to read and write to files
"""
import json

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
def read_settings() -> dict:
    # Get all the data from settings
    settings_addr = USERDATA_ROOT + SETTINGS
    file = open(settings_addr, "r")
    data = json.loads(file.read())
    file.close()
    return data


def write_settings(data: dict) -> None:
    settings_addr = USERDATA_ROOT + SETTINGS
    file = open(settings_addr, "w")
    data = json.dumps(data)
    file.write(data)
    file.close()
