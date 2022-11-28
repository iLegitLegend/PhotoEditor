import os, sys

from PIL import Image
im = Image.open("Untitled.png")
im.show("Untitled.png")
box = (100, 100, 400, 400)
region = im.crop(box)

