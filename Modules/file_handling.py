"""
FILE HANDLING MODULE: Holds functions to read and write to files
"""
import json

# File location constants. NOTE: Files relative to main.py, not here
SETTINGS = "settings.txt"


class Manager:
    def __init__(self, root: str = "UserData/"):
        """
        Create a file manager class that stores all the data needed to access, rather than passing it in every use
        :param root: The file path to the "UserData" folder
        """
        self.file_addr = root + SETTINGS

    # Read settings
    def read_settings(self) -> dict:
        # Get all the data from settings
        file = open(self.file_addr, "r")
        data = json.loads(file.read())
        file.close()
        return data

    def write_settings(self, data: dict) -> None:
        file = open(self.file_addr, "w")
        data = json.dumps(data)
        file.write(data)
        file.close()
