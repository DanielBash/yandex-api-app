import random
import sys
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QApplication, QLabel
import yandexapi


class YandexApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pyqt6 App api')
        self.setGeometry(300, 300, 500, 500)

        self.label = QLabel()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YandexApp()
    window.show()
    sys.exit(app.exec())
