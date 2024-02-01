from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from YandexMapsAPI import YandexStaticApi


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Map_1')

    def load_image(self, file_name):
        pixmap = QPixmap(file_name)

        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())

        self.resize(pixmap.width(), pixmap.height())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    YandexStaticApi().get_image(53.1738929, 56.8724243, 1)  # координаты X, Y и масштаб
    ex = App()
    ex.load_image('image.png')
    ex.show()

    sys.exit(app.exec_())
