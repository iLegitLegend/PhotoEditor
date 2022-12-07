import PIL.Image
from PIL import Image, ImageOps
import os, sys

chosen_image = str(input("Which image would you like to edit?\n"))
picture = Image.open(chosen_image)

state = 0

start = str(input("What would you like to do to the image?\n"
                  "\n"
                  "[1] Convert image file type\n"
                  "[2] Edit image\n"
                  "[3] Quit\n"
                  "\n"
                  "Your selection: "))

if start == "3":
    state = 2

if start == "1":
    image_type = str(input("What type would you like to convert to?\n"""))
    f, e = os.path.splitext(chosen_image)
    outfile = f + image_type
    name = input(str("What would you like to name the image file?\n"))
    picture.save(fr"C:\Users\Josh VanderLaan\PycharmProjects\pythonProject1\{name}{image_type}")

if start == "2":
    while state == 0:
        chosen_edit = str(input("\nHow would you like to edit the image?\n"
                                "\n"
                                "[1] Rotate, flip(↕), or mirror(⇆) image\n"
                                "[2] Edit contrast\n"
                                "[3] Merge images\n"
                                "[4] Swap pixel colours\n"
                                "\n"
                                "Your selection: "))

        if chosen_edit == "1":
            rotate_flip_mirror = str(input("What would you like to do to the image?\n"
                                            "[1] Rotate\n"
                                            "[2] Flip (↕)\n"
                                            "[3] Mirror (⇆)\n"
                                            "Selection: "))
            if rotate_flip_mirror == "1":
                rotate = str(input("By what degree do you want to rotate the image?\n"))
                cut = str(input("Would you like the original image cut, or to remain fully displayed?\n"
                                "[1] Cut\n"
                                "[2] Full\n"
                                "\n"
                                "Your selection: "))
                if cut == "1":
                    degree = picture.rotate(int(rotate), expand=False)
                    picture = degree
                    picture.show()
                if cut == "2":
                    degree = picture.rotate(int(rotate), expand=True)
                    picture = degree
                    picture.show()
                degree = picture
                _continue_ = str(input("Would you like to [1] Keep editing, [2] Save the edited image, "
                                       "or [3] Quit editing?\n"))
                if _continue_ == "1":
                    state = 0
                if _continue_ == "2":
                    picture = degree
                    name = input(str("What would you like to name the image file?\n"))
                    f, e = os.path.splitext(chosen_image)
                    outfile = name + e
                    picture.save(outfile)
                    state = 1
                if _continue_ == "3":
                    break
            if rotate_flip_mirror == "2":
                picture_flip = ImageOps.flip(picture)
                picture = picture_flip
                picture.show()
                _continue_ = str(input("Would you like to [1] Keep editing, [2] Save the edited image, "
                                       "or [3] Quit editing?\n"))
                if _continue_ == "1":
                    state = 0
                if _continue_ == "2":
                    name = input(str("What would you like to name the image file?\n"))
                    f, e = os.path.splitext(chosen_image)
                    outfile = name + e
                    picture.save(outfile)
                    state = 1
                if _continue_ == "3":
                    break
            if rotate_flip_mirror == "3":
                picture_mirror = ImageOps.mirror(picture)
                picture = picture_mirror
                picture.show()
                _continue_ = str(input("Would you like to [1] Keep editing, [2] Save the edited image, "
                                       "or [3] Quit editing?\n"))
                if _continue_ == "1":
                    state = 0
                if _continue_ == "2":
                    name = input(str("What would you like to name the image file?\n"))
                    f, e = os.path.splitext(chosen_image)
                    outfile = name + e
                    picture.save(outfile)
                    state = 1
                if _continue_ == "3":
                    break

        if chosen_edit == "2":
            contrast_value = float(input("1 = Original Image\n"
                                         "x<1 = Decreased Contras\n"
                                         "x>1 = Increased Contrast\n"
                                         "Factor: "))
            contrast = picture.point(lambda i: i * contrast_value)
            picture = contrast
            picture.show()
            _continue_ = str(input("Would you like to [1] Keep editing, [2] Save the edited image, "
                                   "or [3] Quit editing?\n"))
            if _continue_ == "1":
                state = 0
            if _continue_ == "2":
                name = input(str("What would you like to name the image file?\n"))
                f, e = os.path.splitext(chosen_image)
                outfile = name + e
                picture.save(outfile)
                state = 1
            if _continue_ == "3":
                break

        if state == 1:
            print("Image file has been saved.")
            break
        if state == 2:
            break





