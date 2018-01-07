# -*- coding: utf-8 -*-
import os,sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from mywindow import MyWindow
import pygame


class Main(MyWindow):
    def __init__(self):
        super().__init__()
        self.play_list = QMediaPlaylist()
        self.player = QMediaPlayer()
        self.player.setPlaylist(self.play_list)
        self.initUI()

    def initUI(self):
        self.setGeometry(800, 300, 250, 150)
        btn = QPushButton("play", self)
        btn.clicked.connect(self.play)


        for root, dirs, files in os.walk("./music"):
            # print(root)
            # print(dirs)
            print(files)
            for file in files:
                print(os.path.join(file))
                media = QUrl("music/"+os.path.join(file))
                self.play_list.addMedia(QMediaContent(media))

        # self.play_list.addMedia(QMediaContent(QUrl("music/applause.mp3")))
        # self.play_list.addMedia(QMediaContent(QUrl("music/machine_fire.mp3")))
        # self.play_list.addMedia(QMediaContent(QUrl("music/wow.mp3")))



        self.show()

    def play(self):
        print("play")
        # self.play_list.setCurrentIndex(1)
        self.player.play()

        # pygame.mixer.init()
        # track = pygame.mixer.music.load("tankwar.mp3")
        # pygame.mixer.music.play()

        # self.player = QMediaPlayer()
        # media = QUrl("music/tankwar.mp3")
        # self.player.setMedia(QMediaContent(media))
        # self.player.play()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
