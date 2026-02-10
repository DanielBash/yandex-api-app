import random
import sys
import traceback

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QApplication, QLabel
from PyQt6.uic.properties import QtWidgets
import yandexapi
from PIL import Image, ImageQt

sys._excepthook = sys.excepthook


def pyqt_exception_hook(exctype, value, tb):
    traceback.print_exception(exctype, value, tb)
    sys._excepthook(exctype, value, tb)
    sys.exit(1)


sys.excepthook = pyqt_exception_hook

x, y = 37.677751, 55.757718
z = 0

z_step, x_step, y_step = 1, 1, 1
theme = 'light'
pt = ''

search_txt = 'Тут будет адрес объекта'
display_mail = True
current_adress = ()


class YandexApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pyqt6 App api')
        self.setGeometry(300, 300, 500, 500)

        self.label = QLabel(self)
        self.label.setFixedSize(500, 500)
        self.led = QLineEdit(self)
        self.led_btn = QPushButton(self)

        self.led_btn.setText('Поиск')
        self.led_btn.move(120, 0)
        self.led_btn.clicked.connect(self.search_obj)

        self.theme_btn = QPushButton(self)
        self.theme_btn.setText('Сменить тему')
        self.theme_btn.move(190, 0)
        self.theme_btn.clicked.connect(self.theme_change)

        self.clear_search_btn = QPushButton(self)
        self.clear_search_btn.setText('Очистить поиск')
        self.clear_search_btn.move(290, 0)
        self.clear_search_btn.clicked.connect(self.clear_search)

        self.search_obj_label = QLabel(self)
        self.search_obj_label.setFixedSize(500, 30)
        self.search_obj_label.move(0, 470)
        self.search_obj_label.setText(search_txt)

        self.display_mail_btn = QPushButton(self)
        self.display_mail_btn.setText('Отображать почтовый индекс')
        self.display_mail_btn.move(290, 0)
        self.display_mail_btn.clicked.connect(self.toggle_mail)

        self.load_image()

    def set_image(self, img: Image):
        img = ImageQt.toqimage(img)

        pixmap = QPixmap.fromImage(img).scaled(500, 500)
        self.label.setPixmap(pixmap)

    def load_image(self):
        self.set_image(yandexapi.get_static(x=x, y=y, z=z, theme=theme, pt=pt))

    def keyPressEvent(self, event):
        global x, y, z, theme, pt

        if event.key() == Qt.Key.Key_PageUp:
            z += z_step
        if event.key() == Qt.Key.Key_PageDown:
            z -= z_step

        if event.key() == Qt.Key.Key_Up:
            y += y_step / z
        if event.key() == Qt.Key.Key_Down:
            y -= y_step / z
        if event.key() == Qt.Key.Key_Right:
            x += x_step / z
        if event.key() == Qt.Key.Key_Left:
            x -= x_step / z

        if event.key() == Qt.Key.Key_Space:
            self.theme_change()

        x = min(180, max(-180, x))
        y = min(180, max(-180, y))

        self.load_image()

    def search_obj(self):
        global x, y, z, pt, current_adress
        try:
            dat = yandexapi.get_geocoder(self.led.text()).json()
            long, lat, delta = yandexapi.get_location(dat)
            x = float(long)
            y = float(lat)
            pt = f'{x},{y}'
            z = 5
            self.led.setText('')
            current_adress = (
                dat["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
                    "GeocoderMetaData"]["text"], '12')
            self.toggle_mail()
        except:
            self.led.setText('')
            current_adress = ()

        self.load_image()

    def theme_change(self):
        global theme

        if theme == 'dark':
            theme = 'light'
        elif theme == 'light':
            theme = 'dark'

        self.load_image()

    def clear_search(self):
        global pt

        pt = ''
        self.search_obj_label.setText(search_txt)
        self.load_image()

    def update_mail(self):
        ret = search_txt

        if len(current_adress) > 0:
            if display_mail:
                ret = f'{current_adress[0]} {current_adress[1]}'

        self.search_obj_label.setText(ret)

    def toggle_mail(self):
        global display_mail

        display_mail = not display_mail

        self.toggle_mail()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YandexApp()
    window.show()
    sys.exit(app.exec())
