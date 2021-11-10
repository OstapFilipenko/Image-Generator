import re
from PIL.Image import new
from reportlab.graphics.shapes import Drawing
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
import codecs
import random
import linecache
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.renderSVG import SVGCanvas, draw

import gui

gui.start_gui()

old_colour = '#FF0000'
color_path = "assets/hexColors.txt"
backgroundCol = ''

background = None
layer2 = None


def random_color():
    num_lines = sum(1 for line in open(color_path))
    random_line = random.randint(1, num_lines)
    return linecache.getline(color_path, random_line)


def get_content(filePath, newCol):
    f = codecs.open(filePath, encoding='utf-8', errors='ignore')
    content = f.read()
    f.close
    w = content.replace(old_colour, newCol)
    return w


def combine_svg(background, foreground):
    d = Drawing(1024, 1024)
    d.add(background)
    d.add(foreground)
    c = SVGCanvas((d.width, d.height))
    draw(d, c, 0, 0)
    return c


def change_color(filePath, content):
    f = open(filePath, 'w', encoding='utf-8', errors='ignore')
    f.write(content)
    f.close


def build_background():
    newColBackground = random_color()
    backgroundCol = get_content(
        'assets/Components/Layer-1/background.svg', newColBackground)
    change_color('layer1.svg', backgroundCol)
    background = svg2rlg('layer1.svg')
    return background


def choose_layer2():
    percent = random.randint(1, 100)
    if percent <= 30:
        return 'assets/Components/Layer-2/circle.svg'
    elif (percent > 30) and (percent <= 50):
        return 'assets/Components/Layer-2/square.svg'
    elif (percent > 50) and (percent <= 65):
        return 'assets/Components/Layer-2/octagon.svg'
    else:
        return 'assets/Components/nothing.svg'


def build_layer2():
    chosenlayer2 = choose_layer2()

    while True:
        newColForeground = random_color()
        if newColForeground != backgroundCol:
            break
    layer2Col = get_content(chosenlayer2, newColForeground)
    change_color('layer2.svg', layer2Col)
    layer2 = svg2rlg('layer2.svg')
    return layer2


def choose_layer3():
    percent = random.randint(1, 100)
    if percent <= 20:
        return 'assets/Components/Layer-3/smallcircle.svg'
    elif (percent > 20) and (percent <= 45):
        return 'assets/Components/Layer-3/smallsquare.svg'
    elif (percent > 45) and (percent <= 55):
        return 'assets/Components/Layer-3/smallhexagon.svg'
    else:
        return 'assets/Components/nothing.svg'


def build_layer3():
    chosenlayer3 = choose_layer3()
    layer3 = svg2rlg(chosenlayer3)
    return layer3


def choose_layer4():
    percent = random.randint(1, 100)
    if percent <= 20:
        return 'assets/Components/Layer-4/circle.svg'
    elif (percent > 20) and (percent <= 45):
        return 'assets/Components/Layer-4/square.svg'
    elif (percent > 45) and (percent <= 55):
        return 'assets/Components/Layer-4/hexagon.svg'
    elif (percent > 55) and (percent <= 60):
        return 'assets/Components/Layer-4/rotatedsquare.svg'
    else:
        return 'assets/Components/nothing.svg'


def build_layer4():
    chosenlayer4 = choose_layer4()
    layer4 = svg2rlg(chosenlayer4)
    return layer4


def choose_layer5():
    percent = random.randint(1, 100)
    if percent <= 20:
        return 'assets/Components/Layer-5/bigcircle.svg'
    elif (percent > 20) and (percent <= 45):
        return 'assets/Components/Layer-5/bigsquare.svg'
    elif (percent > 45) and (percent <= 55):
        return 'assets/Components/Layer-5/bighexagon.svg'
    else:
        return 'assets/Components/nothing.svg'


def build_layer5():
    chosenlayer5 = choose_layer5()
    layer5 = svg2rlg(chosenlayer5)
    return layer5

def create_image(name_ending):
    background = build_background()
    layer2 = build_layer2()
    layer3 = build_layer3()
    layer4 = build_layer4()
    layer5 = build_layer5()

    firstcombined = combine_svg(background, layer2)
    firstcombined.save("NFT.svg")

    a = svg2rlg("NFT.svg")

    secondcombined = combine_svg(a, layer3)
    secondcombined.save("NFT.svg")

    a = svg2rlg("NFT.svg")

    thirdcombined = combine_svg(a, layer4)
    thirdcombined.save("NFT.svg")

    a = svg2rlg("NFT.svg")

    combined = combine_svg(a, layer5)
    combined.save("NFT.svg")

    a = svg2rlg("NFT.svg")

    renderPM.drawToFile(a, gui.folder_name + "/NFT_" + str(name_ending) + ".png", fmt="PNG")

for i in range (0, int(gui.image_number)):
    create_image(i+1)

