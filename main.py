import PIL.Image
from PIL import Image
import os, sys

chosen_image = str(input("Which image would you like to edit?\n"))
picture = Image.open(chosen_image)

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
        picture.show(outfile)
        _continue_ = str(input("Would you like to [1] Keep editing, or [2] Save the edited image?\n"))
        if _continue_ == "1":
            state = 0
        if _continue_ == "2":
            name = input(str("What would you like to name the image file?\n"))
            picture.save(fr"C:\Temp\{name}{image_type}")
            state = 1

    if chosen_edit == "2":
        rotate_or_flip = str(input("What would you like to do to the image?\n"
                                   "[1] Rotate\n"
                                   "[2] Flip\n"
                                   "Selection: "))
        if rotate_or_flip == "1":
            rotate = str(input("By what degree do you want to rotate the image?\n"))
            degree = picture.rotate(int(rotate), expand=True)
            picture = degree
            picture.show()
            _continue_ = str(input("Would you like to [1] Keep editing, or [2] Save the edited image?\n"))
            if _continue_ == "1":
                state = 0
            if _continue_ == "2":
                picture = degree
                picture.save(fr"C:\Temp\Untitled.png")
                state = 1

    if state == 1:
        print("Image file has been saved to C:\Temp")
        break




