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

randCol = parse_line_to_color(random_file_line())
randColVal = int(randCol.red), int(randCol.green), int(randCol.blue), 255

randCol_2 = parse_line_to_color(random_file_line())
randColVal_2 = int(randCol_2.red), int(randCol_2.green), int(randCol_2.blue), 255
combine_images(change_color("assets/Components/Layer-1/Background.png", old_color, randColVal), change_color("assets/Components/Layer-2/Circle.png", old_color, randColVal_2)).save("kik.png")
