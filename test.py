import os, sys

from PIL import Image
im = Image.open("Unnamed.jpg")
print(im.format, im.size, im.mode)

josh_png = Image.open("Josh.png")
def merge(im1, im2):
    w = max(im1.size[0], im2.size[0])
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2)

    return im

im = merge(im, josh_png)

im.show(im)