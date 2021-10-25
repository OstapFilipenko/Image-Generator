import glob
from PIL import Image

old_color = 255, 112, 171, 255
new_color = 66, 135, 245, 255

for path in glob.glob("assets/FK-Square.png"):
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
            if pix[x,y] == old_color:
                im.putpixel((x, y), new_color)

    im.save(path+"__out.png")