import os
import sys

# Asegurarse de que podemos encontrar los módulos
if getattr(sys, 'frozen', False):
    # Si estamos ejecutando como exe
    application_path = os.path.dirname(sys.executable)
else:
    # Si estamos ejecutando como script
    application_path = os.path.dirname(os.path.abspath(__file__))

# Agregar el directorio al path
sys.path.insert(0, application_path)

# Ahora importamos nuestros módulos
from app.config import Config
from app.screenshot import ScreenshotTool
from app.gui import SettingsWindow
from app.tray import SystemTray

def main():
    try:
        # Inicializar configuración
        config = Config()
        
        # Crear instancias de las clases principales
        settings_window = SettingsWindow(config)
        screenshot_tool = ScreenshotTool(config)
        system_tray = SystemTray(config, settings_window)
        
        # Ejecutar aplicación
        system_tray.run()
    except Exception as e:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", f"Error al iniciar la aplicación: {str(e)}")
        root.destroy()
        raise e

if __name__ == "__main__":
    main()