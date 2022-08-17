from PySide2.QtGui import QColor, QPalette
from PySide2.QtWidgets import QWidget


def validColorValue(value: int):
    if value < 0:
        return 0
    elif value > 255:
        return 255
    else:
        return value


def rgb2Color(rgbText:str) -> QColor:
    rgb = rgbText.split(',')
    if rgb:
        if len(rgb) == 3:
            r = int(rgb[0])
            g = int(rgb[1])
            b = int(rgb[2])
            r = validColorValue(r)
            g = validColorValue(g)
            b = validColorValue(b)
            print(r, g, b)
            return QColor(r, g, b)


def hex2Color(hexText: str) -> QColor:
    if hexText.startswith('#') and len(hexText) == 7:
        r = int(hexText[1:3], 16)
        g = int(hexText[3:5], 16)
        b = int(hexText[5:7], 16)
        r = validColorValue(r)
        g = validColorValue(g)
        b = validColorValue(b)
        print(r, g, b)
        return QColor(r, g, b)


def color2hex(color : QColor) -> str:
    r = color.red()
    g = color.green()
    b = color.blue()
    return "#{0}{1}{2}".format(hex(r)[2:4], hex(g)[2:4], hex(b)[2:4])


def color2rgb(color : QColor) -> str:
    r = color.red()
    g = color.green()
    b = color.blue()
    return "{0},{1},{2}".format(r, g, b)


class ColorBlock(QWidget):
    def __init__(self, color):
        super(ColorBlock, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

    def setColor(self, newColor: QColor):
        p = self.palette()
        p.setColor(QPalette.Window, newColor)
        self.setPalette(p)