import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import requests

x, y = map(int, input('ведите координаты:').split())
m1, m2 = map(int, input('введите масштаб:').split())
map_request = f'https://static-maps.yandex.ru/1.x/?ll={x},{y}&spn=2{m1},{m2}&l=sat'
map_response = requests.get(map_request)
with open('map.png', mode='wb') as file:
    file.write(map_response.content)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('maps.ui', self)

        self.pixmap = QPixmap('map.png')
        self.image = QLabel(self)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())