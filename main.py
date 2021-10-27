import glob
from PIL import Image

old_color = 255, 112, 171, 255
new_color = 66, 135, 245, 255

def change_color(file_path, o_color, n_color):
    for path in glob.glob(file_path):
        if "__out" in path:
            print("skipping on: " + path)
            continue

        print ("working on: " + path)

        im = Image.open(path)
        im = im.convert("RGBA")
        width, height = im.size
        colortuples = im.getcolors()

        pix = im.load()
        for x in range(0, width):
            for y in range(0, height):
                if pix[x,y] == o_color:
                    im.putpixel((x, y), n_color)

        return im

def combine_images(background_image, foreground_image):
    return Image.alpha_composite(background_image, foreground_image)

change_color("assets/FK-Square.png", old_color, new_color).save("lol.png")
