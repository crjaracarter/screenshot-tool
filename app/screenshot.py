import pyautogui
import keyboard
from PIL import ImageGrab, Image
import win32clipboard
from io import BytesIO
import os
from datetime import datetime
import tkinter as tk

class ScreenshotTool:
    def __init__(self, config):
        self.config = config
        self.setup_hotkeys()
        self.selection_active = False

    def setup_hotkeys(self):
        keyboard.add_hotkey(
            self.config.settings['hotkeys']['full_screen'],
            self.capture_full_screen
        )
        keyboard.add_hotkey(
            self.config.settings['hotkeys']['area_selection'],
            self.start_area_selection
        )

    def capture_full_screen(self):
        screenshot = pyautogui.screenshot()
        self.process_screenshot(screenshot)

    def start_area_selection(self):
        if not self.selection_active:
            self.selection_active = True
            self.root = tk.Tk()
            self.root.attributes('-alpha', 0.3)
            self.root.attributes('-fullscreen', True)
            self.root.configure(background='grey')

            self.start_x = None
            self.start_y = None
            self.current_rect = None

            self.root.bind('<Button-1>', self.on_click)
            self.root.bind('<B1-Motion>', self.on_drag)
            self.root.bind('<ButtonRelease-1>', self.on_release)
            self.root.bind('<Escape>', lambda e: self.cancel_selection())

            self.canvas = tk.Canvas(self.root, highlightthickness=0)
            self.canvas.pack(fill='both', expand=True)
            self.canvas.configure(background='grey')

            self.root.mainloop()

    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        if self.current_rect:
            self.canvas.delete(self.current_rect)
        self.current_rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, event.x, event.y,
            outline='red', width=2
        )

    def on_release(self, event):
        if self.start_x is not None:
            x1 = min(self.start_x, event.x)
            y1 = min(self.start_y, event.y)
            x2 = max(self.start_x, event.x)
            y2 = max(self.start_y, event.y)
            
            self.root.withdraw()
            screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
            self.process_screenshot(screenshot)
        
        self.cancel_selection()

    def cancel_selection(self):
        self.selection_active = False
        if hasattr(self, 'root'):
            self.root.destroy()

    def process_screenshot(self, screenshot):
        if self.config.settings['save_to_clipboard']:
            self.save_to_clipboard(screenshot)
        
        if self.config.settings['save_to_file']:
            self.save_to_file(screenshot)

    def save_to_clipboard(self, image):
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()

    def save_to_file(self, image):
        os.makedirs(self.config.settings['save_directory'], exist_ok=True)
        filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{self.config.settings['file_format']}"
        filepath = os.path.join(self.config.settings['save_directory'], filename)
        image.save(filepath)