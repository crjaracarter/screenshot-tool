# Crear un script convert_icon.py
from PIL import Image
import os

# Abrir el PNG
img = Image.open('resources/icon.png')

# Convertir y guardar como ICO
img.save('resources/icon.ico', format='ICO')