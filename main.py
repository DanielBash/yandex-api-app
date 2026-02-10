import random
import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QApplication, QLabel
from PyQt6.uic.properties import QtWidgets

import yandexapi
from PIL import Image, ImageQt

x, y = 37.677751, 55.757718
z = 0

class YandexApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pyqt6 App api')
        self.setGeometry(300, 300, 500, 500)

        self.label = QLabel()

    def set_image(self, img: Image):
        img = ImageQt.toqimage(img)

        pixmap = QPixmap.fromImage(img).scaled(300, 300, QtWidgets.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)

    def load_image(self):
        self.set_image(x, y, z=z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YandexApp()
    window.show()
    sys.exit(app.exec())
