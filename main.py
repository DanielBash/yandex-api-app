import random
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QApplication, QLabel
from PyQt6.uic.properties import QtWidgets

import yandexapi
from PIL import Image, ImageQt

x, y = 37.677751, 55.757718
z = 0

z_step, x_step, y_step = 1, 1, 1
theme = 'light'


class YandexApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pyqt6 App api')
        self.setGeometry(300, 300, 500, 500)

        self.label = QLabel(self)
        self.label.setFixedSize(500, 500)

        self.load_image()

    def set_image(self, img: Image):
        img = ImageQt.toqimage(img)

        pixmap = QPixmap.fromImage(img).scaled(500, 500)
        self.label.setPixmap(pixmap)

    def load_image(self):
        self.set_image(yandexapi.get_static(x=x, y=y, z=z, theme=theme))

    def keyPressEvent(self, event):
        global x, y, z, theme

        if event.key() == Qt.Key.Key_PageUp:
            z += z_step
        if event.key() == Qt.Key.Key_PageDown:
            z += z_step

        if event.key() == Qt.Key.Key_Up:
            y += y_step / z
        if event.key() == Qt.Key.Key_Down:
            y -= y_step / z
        if event.key() == Qt.Key.Key_Right:
            x += x_step / z
        if event.key() == Qt.Key.Key_Left:
            x -= x_step / z

        if event.key() == Qt.Key.Key_Space:
            if theme == 'dark':
                theme = 'light'
            elif theme == 'light':
                theme = 'dark'

        x = min(180, max(-180, x))
        y = min(180, max(-180, y))

        self.load_image()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YandexApp()
    window.show()
    sys.exit(app.exec())
