"""
FILE HANDLING MODULE: Holds functions to read and write to files
"""

# File location constants. NOTE: Files relative to main.py, not here
USERDATA_ROOT = "UserData/"
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
    data = []  # Stores each line in an array
    for i in range(lines):
        data.append(file.readline())
    file.close()

    # Store the data in a dict
