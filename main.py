import sys

from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QPalette, QColor, QKeyEvent
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, \
    QLineEdit, QGridLayout, QLabel, QPushButton

from color_widget import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Color panel")

        # self.setFixedSize(QSize(400, 300))

        initColor = QColor('grey')
        colorWidget = ColorBlock(initColor)
        colorWidget.setMinimumHeight(50)

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

        vLayout = QGridLayout()
        vLayout.setAlignment(Qt.AlignCenter | Qt.AlignTop)
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
