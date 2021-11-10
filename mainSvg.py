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

from Models.color import Color


old_colour = '#FF0000'
color_path = "assets/hexColors.txt"
backgroundCol = ''

background = None
layer2 = None


def randomColor():
    num_lines = sum(1 for line in open(color_path))
    random_line = random.randint(1, num_lines)
    return linecache.getline(color_path, random_line)


def getContent(filePath, newCol):
    f = codecs.open(filePath, encoding='utf-8', errors='ignore')
    content = f.read()
    f.close
    w = content.replace(old_colour, newCol)
    return w


def combineSvg(background, foreground):
    d = Drawing(1024, 1024)
    d.add(background)
    d.add(foreground)
    c = SVGCanvas((d.width, d.height))
    draw(d, c, 0, 0)
    return c


def changeColor(filePath, content):
    f = open(filePath, 'w', encoding='utf-8', errors='ignore')
    f.write(content)
    f.close


def buildBackground():
    newColBackground = randomColor()
    backgroundCol = getContent(
        'assets/Components/Layer-1/background.svg', newColBackground)
    changeColor('layer1.svg', backgroundCol)
    background = svg2rlg('layer1.svg')
    return background


def chooseLayer2():
    percent = random.randint(1, 100)
    if percent <= 30:
        return 'assets/Components/Layer-2/circle.svg'
    elif (percent > 30) and (percent <= 50):
        return 'assets/Components/Layer-2/square.svg'
    elif (percent > 50) and (percent <= 65):
        return 'assets/Components/Layer-2/octagon.svg'
    else:
        return 'assets/Components/nothing.svg'


def buildLayer2():
    chosenlayer2 = chooseLayer2()

    while True:
        newColForeground = randomColor()
        if newColForeground != backgroundCol:
            break
    layer2Col = getContent(chosenlayer2, newColForeground)
    changeColor('layer2.svg', layer2Col)
    layer2 = svg2rlg('layer2.svg')
    return layer2


def chooseLayer3():
    percent = random.randint(1, 100)
    if percent <= 20:
        return 'assets/Components/Layer-3/smallcircle.svg'
    elif (percent > 20) and (percent <= 45):
        return 'assets/Components/Layer-3/smallsquare.svg'
    elif (percent > 45) and (percent <= 55):
        return 'assets/Components/Layer-3/smallhexagon.svg'
    else:
        return 'assets/Components/nothing.svg'


def buildLayer3():
    chosenlayer3 = chooseLayer3()
    layer3 = svg2rlg(chosenlayer3)
    return layer3


def chooseLayer4():
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


def buildLayer4():
    chosenlayer4 = chooseLayer4()
    layer4 = svg2rlg(chosenlayer4)
    return layer4


def chooseLayer5():
    percent = random.randint(1, 100)
    if percent <= 20:
        return 'assets/Components/Layer-5/bigcircle.svg'
    elif (percent > 20) and (percent <= 45):
        return 'assets/Components/Layer-5/bigsquare.svg'
    elif (percent > 45) and (percent <= 55):
        return 'assets/Components/Layer-5/bighexagon.svg'
    else:
        return 'assets/Components/nothing.svg'


def buildLayer5():
    chosenlayer5 = chooseLayer5()
    layer5 = svg2rlg(chosenlayer5)
    return layer5


background = buildBackground()
layer2 = buildLayer2()
layer3 = buildLayer3()
layer4 = buildLayer4()
layer5 = buildLayer5()

firstcombined = combineSvg(background, layer2)
firstcombined.save("NFT.svg")

a = svg2rlg("NFT.svg")

secondcombined = combineSvg(a, layer3)
secondcombined.save("NFT.svg")

a = svg2rlg("NFT.svg")

thirdcombined = combineSvg(a, layer4)
thirdcombined.save("NFT.svg")

a = svg2rlg("NFT.svg")

combined = combineSvg(a, layer5)
combined.save("NFT.svg")

a = svg2rlg("NFT.svg")

renderPM.drawToFile(a, "NFT.png", fmt="PNG")
