import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import os

class Widget(QMainWindow):
    def __init__(self):

        super().__init__()          # Ініціалізуємо вікно PyQt5. Вже створено
        self.ui = Ui_MainWindow()   
        self.ui.setupUi(self)

        self.configure()
        self.media = QMediaPlayer(self)           # Створює екземпляр медіа програвача
        self.media.setVideoOutput(self.ui.video)  # Вказує віджет, на якому буде знаходитись зображення
        self.get_date()

    def configure(self):                                          
        self.ui.start.clicked.connect(self.media_play)             # Прив’язуємо натискання на кнопку “Старт” до функції self.media_play
        self.ui.stop.clicked.connect(self.media_stop)              # Прив’язуємо натискання на кнопку “Стоп” до функції self.media_stop
        self.ui.calendar.selectionChanged.connect(self.get_date)   # Прив’язуємо подію зміни вибору дати (selectionChanged) до функції self.get_date

    def get_date(self):
        self.media_stop()                                  # Зупинити відео
        print(self.ui.calendar.selectedDate())             # Вивести номер обраного дня
        day = str(self.ui.calendar.selectedDate().day())   # Отримати номер обраного дня

        video_path = os.path.join("Video", f"{day}.mp4")     # Створити назву відео в форматі
        self.media.setMedia(QMediaContent(QUrl.fromLocalFile(video_path)))                     # Завантажити відео до програвача
        if self.ui.autostart.isChecked():                                                      # Якщо відмічено чекбокс “Автозапуск” - запустити відео, інакше - зупинити
            self.media_play()

    def media_play(self):
        self.media.play()  # Запуск відтворення відео

    def media_stop(self):
        self.media.stop() # Зупинка відтворення відео



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
