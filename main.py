import PIL.Image
from PIL import Image
import os, sys

chosen_image = str(input("Which image would you like to edit? : "))
pic = Image.open(chosen_image)

state = 0
while state == 0:
    chosen_edit = str(input("\nHow would you like to edit the image?\n"
                            "\n"
                            "[1] Convert image type\n"
                            "[2] Rotate image\n"
                            "[3] Edit contrast\n"
                            "[4] Merge images\n"
                            "[5] Swap pixel colours\n"
                            "\n"
                            "Your selection: "))
    if chosen_edit == "1":
        image_type = str(input("What type would you like to convert to?\n"""))
        f, e = os.path.splitext(chosen_image)
        outfile = f + image_type
        pic.show(outfile)
        _continue_ = str(input("Would you like to [1] Keep editing, or [2] Save the edited image?\n"))
        if _continue_ == "1":
            state = 0
        if _continue_ == "2":
            pic.save(outfile)
            state = 1

    if chosen_edit == "2":
        rotate_or_flip = str(input("What would you like to do to the image?\n"
                                   "[1] Rotate\n"
                                   "[2] Flip\n"
                                   "Selection: "))
        if rotate_or_flip == "1":
            rotate = str(input("By what degree do you want to rotate the image?\n"))
            image_rotate = PIL.Image.TRANSPOSE(rotate)
            pic.show(image_rotate) https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Transpose.ROTATE_180
    if state == 1:
        break




