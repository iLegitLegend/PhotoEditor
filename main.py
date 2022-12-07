import PIL.Image
from PIL import Image, ImageOps, ImageEnhance
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
    f, e = os.path.splitext(chosen_image)
    image_type = str(input("What type would you like to convert to?\n"""))
    name = input(str("What would you like to name the image file?\n"))
    outfile = name + image_type
    picture.save(outfile)
    state = 1

if start == "2":
    while state == 0:
        chosen_edit = str(input("\nHow would you like to edit the image?\n"
                                "\n"
                                "[1] Rotate, flip(↕), or mirror(⇆) image\n"
                                "[2] Edit contrast\n"
                                "[3] Crop image\n"
                                "[4] Swap pixel colours / Change color palette\n"
                                "\n"
                                "Your selection: "))

        if chosen_edit == "1":
            rotate_flip_mirror = str(input("[1] Rotate\n"
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
            if rotate_flip_mirror == "2":
                picture_flip = ImageOps.flip(picture)
                picture = picture_flip
                picture.show()
            if rotate_flip_mirror == "3":
                picture_mirror = ImageOps.mirror(picture)
                picture = picture_mirror
                picture.show()
            _continue_ = str(input("\n[1] Keep editing\n[2] Save the edited image\n[3] Quit editing\nSelection: "))
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
                                         "x<1 = Decreased Contrast\n"
                                         "x>1 = Increased Contrast\n"
                                         "Factor: "))
            contrast = picture.point(lambda i: i * contrast_value)
            picture = contrast
            picture.show()
            _continue_ = str(input("\n[1] Keep editing\n[2] Save the edited image\n[3] Quit editing\nSelection: "))
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

        if chosen_edit == "3":
            print(picture.size)
            x, y = picture.size
            left = int(input(f"Left (0 < x < {x}): "))
            top = int(input(f"Top (0 < x < {y}): "))
            right = int(input(f"Right (0 < x < {x} | x > {left}): "))
            bottom = int(input(f"Bottom (0 < x < {y} | x > {top}): "))
            (left_, top_, right_, bottom_) = (left, top, right, bottom)
            picture_crop = picture.crop((left_, top_, right_, bottom_))
            picture_crop.show()
            picture = picture_crop
            _continue_ = str(input("\n[1] Keep editing\n[2] Save the edited image\n[3] Quit editing\nSelection:"))
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

        if chosen_edit == "4":
            colour_edit = input(str("[1] Greyscale\n"
                                    "[2] Colour palette\n"
                                    "[3] Change shades of white to colour\n"
                                    "[4] Enhance colour\n"
                                    "\nSelection:"))
            if colour_edit == "1":
                greyScale = picture.convert("L")
                picture = greyScale
                picture.show()
            if colour_edit == "2":
                colourDepth = int(input("Colour depth: "))
                palette = picture.convert("P", palette = Image.Palette.ADAPTIVE, colors = colourDepth)
                picture = palette
                picture.show()
            if colour_edit == "3":
                picture = picture.convert("RGB")
                Range = picture.getdata()
                newPicture = []
                r = int(input("R: "))
                g = int(input("G: "))
                b = int(input("B: "))
                for i in Range:
                    if i[0] in list(range(200, 256)):
                        newPicture.append((r, g, b))
                    else:
                        newPicture.append(i)
                picture.putdata(newPicture)
                picture.show()
            if colour_edit == "4":
                factor = int(input("Factor: "))
                colourEnhance = ImageEnhance.Color(picture).enhance(factor)
                picture = colourEnhance
                picture.show()
            if colour_edit == "5":
                pixel = picture.load()
                x = int(input("X coordinate: "))
                y = int(input("Y coordinate: "))
                r = int(input("R: "))
                g = int(input("G: "))
                b = int(input("B: "))
                pixel[x, y] = ((r, g, b))
                picture.show(pixel)
            _continue_ = str(input("\n[1] Keep editing\n[2] Save the edited image\n[3] Quit editing\nSelection:"))
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
