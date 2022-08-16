import sys

from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QPalette, QColor, QKeyEvent
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, \
    QLineEdit, QGridLayout, QLabel, QPushButton


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

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
        self.setFixedSize(200, 200)

    def setColor(self, newColor: QColor):
        p = self.palette()
        p.setColor(QPalette.Window, newColor)
        self.setPalette(p)

# class ColorLineEdit(QLineEdit):
#     def __init__(self, fn):
#         super(ColorLineEdit, self).__init__()
#         self.fn = fn
#
#     def keyPressEvent(self, evt:QKeyEvent) -> None:
#         super(ColorLineEdit, self).keyPressEvent(evt)
#         if evt.key() == Qt.Key.Key_Enter:
#             self.fn()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Color panel")

        # self.setFixedSize(QSize(400, 300))

        initColor = QColor('grey')
        colorWidget = Color(initColor)
        rgbLabel = QLabel('RGB: ')
        rgbEdit = QLineEdit()
        setRgbBtn = QPushButton('rgb ok')
        hexLabel = QLabel('HEX: ')
        hexEdit = QLineEdit()
        setHexBtn = QPushButton('hex ok')
        setRgbBtn.clicked.connect(self.setRgbColor)
        setHexBtn.clicked.connect(self.setHexColor)
        rgbEdit.returnPressed.connect(self.setRgbColor)
        hexEdit.returnPressed.connect(self.setHexColor)

        gridLayout = QGridLayout()
        gridLayout.addWidget(rgbLabel, 0, 0)
        gridLayout.addWidget(rgbEdit, 0, 1)
        gridLayout.addWidget(setRgbBtn, 0, 2)
        gridLayout.addWidget(hexLabel, 1, 0)
        gridLayout.addWidget(hexEdit, 1, 1)
        gridLayout.addWidget(setHexBtn, 1, 2)

        gridWidget = QWidget()
        gridWidget.setLayout(gridLayout)

        vLayout = QVBoxLayout()
        vLayout.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        vLayout.addWidget(colorWidget)
        vLayout.addWidget(gridWidget)

        mainWidget = QWidget()
        mainWidget.setLayout(vLayout)
        self.setCentralWidget(mainWidget)
        self.colorWidget = colorWidget
        self.rgbEdit = rgbEdit
        self.hexEdit = hexEdit
        self.updateText(initColor)

    def setRgbColor(self):
        print('rgb')
        rgbText = self.rgbEdit.text()
        color = rgb2Color(rgbText)
        if color:
            self.colorWidget.setColor(color)
            self.updateText(color)

    def setHexColor(self):
        print('hex')
        hexText = self.hexEdit.text()
        color = hex2Color(hexText)
        if color:
            self.colorWidget.setColor(color)
            self.updateText(color)

    def updateText(self, color):
        self.rgbEdit.setText(color2rgb(color))
        self.hexEdit.setText(color2hex(color))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
