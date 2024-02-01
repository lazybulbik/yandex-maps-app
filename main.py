from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from YandexMapsAPI import YandexStaticApi


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Map_2')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            YMap.scale_up()
            YMap.get_image()
            self.PixMap = QPixmap('image.png')
            self.label.setPixmap(self.PixMap)
        elif event.key() == Qt.Key_PageDown:
            YMap.scale_down()
            YMap.get_image()
            self.PixMap = QPixmap('image.png')
            self.label.setPixmap(self.PixMap)
        elif event.key() == Qt.Key_Up:
            YMap.move_up()
            YMap.get_image()
            self.PixMap = QPixmap('image.png')
            self.label.setPixmap(self.PixMap)
        elif event.key() == Qt.Key_Down:
            YMap.move_down()
            YMap.get_image()
            self.PixMap = QPixmap('image.png')
            self.label.setPixmap(self.PixMap)
        elif event.key() == Qt.Key_Left:
            YMap.move_left()
            YMap.get_image()
            self.PixMap = QPixmap('image.png')
            self.label.setPixmap(self.PixMap)
        elif event.key() == Qt.Key_Right:
            YMap.move_right()
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
