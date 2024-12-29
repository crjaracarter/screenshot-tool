import pystray
from PIL import Image
import os

class SystemTray:
    def __init__(self, config, settings_window):
        self.config = config
        self.settings_window = settings_window
        self.create_tray()

    def create_tray(self):
        icon_path = os.path.join(os.path.dirname(__file__), "../resources/icon.png")
        image = Image.open(icon_path)

        menu = (
            pystray.MenuItem("Settings", self.show_settings),
            pystray.MenuItem("Exit", self.quit_app)
        )

        self.icon = pystray.Icon(
            "Screenshot Tool",
            image,
            "Screenshot Tool",
            menu
        )

    def run(self):
        self.icon.run()

    def show_settings(self):
        self.settings_window.show()

    def quit_app(self):
        self.icon.stop()