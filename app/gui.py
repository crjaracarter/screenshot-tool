import customtkinter as ctk
from tkinter import filedialog

class SettingsWindow:
    def __init__(self, config):
        self.config = config
        self.window = None
        self.hotkey_entries = {}

    def show(self):
        if self.window is not None:
            self.window.focus_force()
            return

        self.window = ctk.CTk()
        self.window.title("Screenshot Tool Settings")
        self.window.geometry("400x500")
        self.window.resizable(False, False)

        self.create_widgets()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def create_widgets(self):
        # Hotkeys frame
        hotkeys_frame = ctk.CTkFrame(self.window)
        hotkeys_frame.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(hotkeys_frame, text="Hotkeys", font=("", 16, "bold")).pack(pady=5)
        
        # Fullscreen hotkey
        full_screen_frame = ctk.CTkFrame(hotkeys_frame)
        full_screen_frame.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(full_screen_frame, text="Full screen:").pack(side="left", padx=5)
        self.hotkey_entries['full_screen'] = ctk.CTkEntry(full_screen_frame)
        self.hotkey_entries['full_screen'].insert(0, self.config.settings['hotkeys']['full_screen'])
        self.hotkey_entries['full_screen'].pack(side="right", padx=5)

        # Area selection hotkey
        area_frame = ctk.CTkFrame(hotkeys_frame)
        area_frame.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(area_frame, text="Area selection:").pack(side="left", padx=5)
        self.hotkey_entries['area_selection'] = ctk.CTkEntry(area_frame)
        self.hotkey_entries['area_selection'].insert(0, self.config.settings['hotkeys']['area_selection'])
        self.hotkey_entries['area_selection'].pack(side="right", padx=5)

        # Save options frame
        save_frame = ctk.CTkFrame(self.window)
        save_frame.pack(pady=10, padx=10, fill="x")
        ctk.CTkLabel(save_frame, text="Save Options", font=("", 16, "bold")).pack(pady=5)

        # Save directory
        dir_frame = ctk.CTkFrame(save_frame)
        dir_frame.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(dir_frame, text="Save directory:").pack(side="left", padx=5)
        self.dir_entry = ctk.CTkEntry(dir_frame)
        self.dir_entry.insert(0, self.config.settings['save_directory'])
        self.dir_entry.pack(side="left", padx=5, fill="x", expand=True)
        ctk.CTkButton(dir_frame, text="Browse", command=self.browse_directory).pack(side="right", padx=5)

        # Checkboxes
        self.clipboard_var = ctk.BooleanVar(value=self.config.settings['save_to_clipboard'])
        ctk.CTkCheckBox(save_frame, text="Save to clipboard", variable=self.clipboard_var).pack(padx=10, pady=5)

        self.file_var = ctk.BooleanVar(value=self.config.settings['save_to_file'])
        ctk.CTkCheckBox(save_frame, text="Save to file", variable=self.file_var).pack(padx=10, pady=5)

        # File format
        format_frame = ctk.CTkFrame(save_frame)
        format_frame.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(format_frame, text="File format:").pack(side="left", padx=5)
        self.format_var = ctk.StringVar(value=self.config.settings['file_format'])
        format_combo = ctk.CTkComboBox(format_frame, values=["png", "jpg"], variable=self.format_var)
        format_combo.pack(side="right", padx=5)

        # Save button
        ctk.CTkButton(self.window, text="Save Settings", command=self.save_settings).pack(pady=20)

    def browse_directory(self):
        directory = filedialog.askdirectory(initialdir=self.dir_entry.get())
        if directory:
            self.dir_entry.delete(0, 'end')
            self.dir_entry.insert(0, directory)

    def save_settings(self):
        self.config.settings['hotkeys']['full_screen'] = self.hotkey_entries['full_screen'].get()
        self.config.settings['hotkeys']['area_selection'] = self.hotkey_entries['area_selection'].get()
        self.config.settings['save_directory'] = self.dir_entry.get()
        self.config.settings['save_to_clipboard'] = self.clipboard_var.get()
        self.config.settings['save_to_file'] = self.file_var.get()
        self.config.settings['file_format'] = self.format_var.get()
        self.config.save_config()
        self.window.destroy()
        self.window = None

    def on_closing(self):
        self.window.destroy()
        self.window = None