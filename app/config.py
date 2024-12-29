import json
import os

class Config:
    DEFAULT_CONFIG = {
        "hotkeys": {
            "full_screen": "ctrl+shift+c",
            "area_selection": "ctrl+shift+a",
        },
        "save_directory": os.path.expanduser("~/Pictures/Screenshots"),
        "save_to_clipboard": True,
        "save_to_file": True,
        "file_format": "png"
    }

    def __init__(self):
        self.config_file = os.path.expanduser("~/.screenshot_app_config.json")
        self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                self.settings = json.load(f)
        except FileNotFoundError:
            self.settings = self.DEFAULT_CONFIG
            self.save_config()

    def save_config(self):
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        with open(self.config_file, 'w') as f:
            json.dump(self.settings, f, indent=4)