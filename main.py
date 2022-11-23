import os, sys

from PIL import Image
im = Image.open("Untitled.jpg")

print("Untitled.png", im.format, f"{im.size} x {im.mode}")
