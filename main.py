import glob
from PIL import Image
import random
import linecache

from Models.color import Color

old_color = 0, 0, 0, 255
new_color = 66, 135, 245, 255
color_path = "assets/colors.txt"

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

def random_file_line():
    num_lines = sum(1 for line in open(color_path))
    random_line = random.randint(0,num_lines)
    return linecache.getline(color_path, random_line)

def parse_line_to_color(line):
    spilited_line = line.split(":")
    rgba_values = spilited_line[1].split(",")
    return Color(spilited_line[0], rgba_values[0],rgba_values[1], rgba_values[2], rgba_values[3])

#print(parse_line_to_color(random_file_line()))
##change_color("assets/FK-Square.png", old_color, new_color).save("lol.png")

combine_images(change_color("assets/Components/Background.png", old_color, new_color), Image.open("assets/Components/Circle-b9-774x774.png")).save("kik.png")
