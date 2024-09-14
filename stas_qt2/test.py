import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Створи об'єкт медіа плеєра
        self.media = QMediaPlayer(self)
        # Налаштуй вивід зображення в QWidget
        self.media.setVideoOutput(self.ui.video)
        # Завантаж відео, що треба програвати
        vid = QMediaContent(QUrl.fromLocalFile("Video/3.mp4"))
        self.media.setMedia(vid)
        # Запусти відео
        self.media.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
