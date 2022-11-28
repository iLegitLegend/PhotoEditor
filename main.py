import os, sys

from PIL import Image
im = Image.open("Triforce.png")
print(im.format, im.size, im.mode)

def roll(im, delta):
    xsize, ysize, = im.size

    delta = delta % xsize
    if delta == 0:
        return im

    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta))



