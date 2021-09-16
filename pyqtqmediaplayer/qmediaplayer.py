from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
import sys

class VideoPlayer:

    def __init__(self):
        self.video = QVideoWidget()
        self.video.resize(300, 300)
        self.video.move(0, 0)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video)
        url1=r"example1.avi"
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(url1)))
        self.player.setPosition(0) # to start at the beginning of the video every time
        self.video.show()
        self.player.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    v = VideoPlayer()
    sys.exit(app.exec_())

