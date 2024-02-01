from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from YandexMapsAPI import YandexStaticApi


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Map_2')
        self.map_type = 'map'  # Изначально установим тип карты как "схема"

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            YMap.scale_up()
        elif event.key() == Qt.Key_PageDown:
            YMap.scale_down()
        elif event.key() == Qt.Key_Up:
            YMap.move_up()
        elif event.key() == Qt.Key_Down:
            YMap.move_down()
        elif event.key() == Qt.Key_Left:
            YMap.move_left()
        elif event.key() == Qt.Key_Right:
            YMap.move_right()
        elif event.key() == Qt.Key_M:  # Пример использования клавиши M для переключения слоев карты
            self.change_map_layer()

        YMap.get_image()
        self.PixMap = QPixmap('image.png')
        self.label.setPixmap(self.PixMap)

    def change_map_layer(self):
        if self.map_type == 'map':
            self.map_type = 'sat'  # Переключаем на спутниковый вид
        elif self.map_type == 'sat':
            self.map_type = 'map'  # Переключаем на схему

        YMap.change_map_type(self.map_type)

        YMap.get_image()
        self.PixMap = QPixmap('image.png')
        self.label.setPixmap(self.PixMap)

    def load_image(self, file_name):
        pixmap = QPixmap(file_name)
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())
        self.resize(pixmap.width(), pixmap.height())


if __name__ == '__main__':
    import sys

    YMap = YandexStaticApi(53.1738929, 56.8724243)
    app = QApplication(sys.argv)
    YMap.get_image()  # координаты X, Y
    ex = App()
    ex.load_image('image.png')
    ex.show()

    sys.exit(app.exec_())
