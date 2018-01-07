# -*- coding: utf-8 -*-
import os
import sys
import signal
import re
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from mywindow import MyWindow


class MyLabel(QLabel):
    def __init__(self, func, which, parent=None):
        super().__init__(parent)
        self.func = func
        self.which = which
        self.setCursor(Qt.PointingHandCursor)

    def mouseReleaseEvent(self, QMouseEvent):
        self.func()

    def enterEvent(self, *args, **kwargs):
        self.setPixmap(QPixmap("image/"+self.which+"_pressed.png"))

    def leaveEvent(self, *args, **kwargs):
        self.setPixmap(QPixmap("image/"+self.which + "_normal.png"))


class MyFrame(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.lines = []

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.draw_lines(qp)
        qp.end()

    # 遍历列表中的线并画出
    def draw_lines(self, qp):
        pen = QPen(QColor(224, 224, 225), 2, Qt.SolidLine)
        qp.setPen(pen)
        length = len(self.lines)
        for i in range(length):
            line = self.lines[i]
            qp.drawLine(line.x0, line.y0, line.x1, line.y1)

    # 添加一条线
    def draw_line(self, x0, y0, x1, y1):
        self.lines.append(MyLine(x0, y0, x1, y1))


class MyLine(object):
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1


class MyWidget(QWidget):
    def __init__(self, func, which, text):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.func = func
        self.which = which
        self.text = text
        self.pixmap_label = QLabel()
        self.pixmap_label.setPixmap(QPixmap("image/"+self.which + "_normal.png"))
        self.pixmap_label.setAlignment(Qt.AlignVCenter)
        self.text_label = QLabel("<font size=3 color=#646464>"+self.text+"</font>")
        self.text_label.setAlignment(Qt.AlignVCenter)
        hbox = QHBoxLayout()
        hbox.addWidget(self.pixmap_label)
        hbox.addWidget(self.text_label)
        hbox.addStretch(1)
        self.setLayout(hbox)
        self.setCursor(Qt.PointingHandCursor)

    def mouseReleaseEvent(self, QMouseEvent):
        self.func()
        main.list_name.setText("<font size=5 color=#646464>"+self.text+"</font>")

    def enterEvent(self, *args, **kwargs):
        self.pixmap_label.setPixmap(QPixmap("image/"+self.which+"_pressed.png"))
        self.text_label.setText("<font size=3 color=#444444>"+self.text+"</font>")

    def leaveEvent(self, *args, **kwargs):
        self.pixmap_label.setPixmap(QPixmap("image/"+self.which + "_normal.png"))
        self.text_label.setText("<font size=3 color=#646464>" + self.text + "</font>")


class MyScrollBar(QScrollBar):
    def __init__(self):
        super().__init__()
        # 滚动条样式表
        self.setStyleSheet("QScrollBar:vertical"
                           "{"
                                 "width:10px;"
                                 "background:rgb(244,244,246);"
                                 "margin:0px,0px,0px,0px;"
                                 "padding-top:0px;"
                                 "padding-bottom:0px;"
                           "}"
                           "QScrollBar::handle:vertical"
                           "{"
                                 "width:8px;"
                                 "background:rgb(224,224,225);"
                                 "border-radius:4px;"
                                 "min-height:20;"
                           "}"
                           "QScrollBar::handle:vertical:hover"
                           "{"
                                 "background:rgb(206,206,208);"
                                 "border-radius:4px;"
                                 "min-height:20;"
                           "}"
                           "QScrollBar::add-line:vertical"
                           "{"
                                 "height:0px;width:0px;"
                                 "background:rgb(244,244,246);"
                                 "subcontrol-position:bottom;"
                           "}"
                           "QScrollBar::sub-line:vertical"
                           "{"
                                 "height:0px;width:0px;"
                                 "background:rgb(244,244,246);"
                                 "subcontrol-position:top;"
                           "}"
                           "QScrollBar::add-line:vertical:hover"
                           "{"
                                 "height:0px;width:0px;"
                                 "background:rgb(244,244,246);"
                                 "subcontrol-position:bottom;"
                           "}"
                           "QScrollBar::sub-line:vertical:hover"
                           "{"
                                 "height:0px;width:0px;"
                                 "background:rgb(244,244,246);"
                                 "subcontrol-position:top;"
                           "}"
                           "QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical"
                           "{"
                                 "background:rgb(244,244,246);"
                                 "border-radius:4px;"
                           "}")


class MySlider1(QSlider):
    def __init__(self, orientation):
        super().__init__(orientation)
        self.setCursor(Qt.PointingHandCursor)
        # 滑动条样式表
        self.setStyleSheet("QSlider::add-page:Horizontal "
                           "{"
                           "background-color: rgb(87, 97, 106);"
                           "height:4px;"
                           "}"
                           "QSlider::sub-page:Horizontal"
                           "{"
                           "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231,80,229, 255), stop:1 rgba(7,208,255, 255));"
                           "height:4px;"
                           "}"
                           "QSlider::groove:Horizontal"
                           "{"
                           "background:transparent;"
                           "height:6px;"
                           "}"
                           "QSlider::handle:horizontal"
                           "{"
                           "background:white;"
                           "width:10px;border-radius:5px;"
                           "margin:-3px 0px -3px 0px;"
                           "}")


class MySlider2(QSlider):
    def __init__(self, orientation):
        super().__init__(orientation)
        self.setCursor(Qt.PointingHandCursor)
        # 滑动条样式表
        self.setStyleSheet("QSlider::groove:horizontal "
                           "{"
                                "border: 1px solid #4A708B;"
                                "background: #C0C0C0;"
                                "height: 5px;"
                                "border-radius: 1px;"
                                "padding-left:-1px;"
                                "padding-right:-1px;"
                           "}"
                           "QSlider::sub-page:horizontal"
                           "{"
                                "background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);"
                                "background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,stop: 0 #5DCCFF, stop: 1 #1874CD);"
                                "border: 1px solid #4A708B;"
                                "height: 10px;"
                                "border-radius: 2px;"
                           "}"
                           "QSlider::add-page:horizontal"
                           "{"
                                "background: #575757;"
                                "border: 0px solid #777;"
                                "height: 10px;"
                                "border-radius: 2px;"
                           "}"
                           "QSlider::handle:horizontal "
                           "{"
                                "background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 #45ADED, stop:0.778409 rgba(255, 255, 255, 255));"
                                "width: 11px;"
                                "margin-top: -3px;"
                                "margin-bottom: -3px;"
                                "border-radius: 5px;"
                           "}"
                           "QSlider::handle:horizontal:hover"
                           "{"
                                "background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 #2A8BDA, stop:0.778409 rgba(255, 255, 255, 255));"
                                "width: 11px;"
                                "margin-top: -3px;"
                                "margin-bottom: -3px;"
                                "border-radius: 5px;"
                           "}"
                           "QSlider::sub-page:horizontal:disabled"
                           "{"
                                "background: #00009C;"
                                "border-color: #999;"
                           "}"
                           "QSlider::add-page:horizontal:disabled"
                           "{"
                                "background: #eee;"
                                "border-color: #999;"
                           "}"
                           "QSlider::handle:horizontal:disabled"
                           "{"
                                "background: #eee;"
                                "border: 1px solid #aaa;"
                                "border-radius: 4px;"
                           "}")


class MyTableWidgetItem(QTableWidgetItem):
    def __init__(self, args):
        super().__init__(args)
        self.setTextAlignment(Qt.AlignCenter)
        self.setFont(QFont("SansSerif", 10))
        # self.setBackground(QColor(249, 249, 249))


class MySearchBox(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QLineEdit"
                           "{"
                               "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #64cbff, stop: 0 #a6e0fd, stop: 1 #80d4fe);"
                               "padding: 3px;border-style: solid;"
                               "border: 1px solid #80d4fe;"
                               "border-radius: 12;"
                           "}")

class Communicate(QObject):
    min = pyqtSignal()
    close = pyqtSignal()


class Main(MyWindow):
    def __init__(self):
        super().__init__()
        self.c = Communicate()
        self.c.min.connect(self.minWindow)
        self.c.close.connect(self.closeWindow)
        self.play_list = QMediaPlaylist()  # 播放列表
        self.player = QMediaPlayer()  # 播放器
        self.player.setPlaylist(self.play_list)
        self.play_list.currentMediaChanged.connect(self.media_changed)
        self.player.durationChanged.connect(self.duration_changed)
        self.player.positionChanged.connect(self.position_changed)
        self.initUI()
        self.initTitleBar()
        self.initMainFrame()
        self.initBottomBar()

    # 初始化MainWindow
    def initUI(self):
        self.setGeometry(360, 140, 1200, 800)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(self.width(), self.height())
        self.setStyleSheet("background-color:rgb(200,200,200)")
        self.show()

    # 初始化标题栏###########################################################################
    def initTitleBar(self):
        self.title_bar = MyFrame(self)
        self.title_bar.setGeometry(0, 0, 1200, 70)
        self.title_bar.setStyleSheet("background-color:rgb(0,120,230)")
        # 标题字
        title = QLabel()
        title.setPixmap(QPixmap("image/AwesomePlayer.png"))
        title.setAlignment(Qt.AlignVCenter)
        # title.setFixedSize(283, 62)
        # title.setMinimumSize(283, 62)
        # 搜索框
        self.search_box = MySearchBox()
        self.search_box.setPlaceholderText("搜索歌曲、歌手")
        search = MyLabel(self.search, "search")
        search.setPixmap(QPixmap("image/search_normal.png"))
        # search_layout = QHBoxLayout()
        # search_layout.addStretch(1)
        # search_layout.addWidget(search)
        # # search_layout.setSpacing(0)
        # search_layout.setContentsMargins(0, 0, 0, 0)
        # self.search_box.setLayout(search_layout)
        # 最小化关闭按钮
        min_btn = MyLabel(self.minWindow, "minbtn")  # 点击事件: 最小化
        min_btn.setPixmap(QPixmap("image/minbtn_normal.png"))
        min_btn.setToolTip("<font size=4 color=#646464>最小化</font>")
        close_btn = MyLabel(self.closeWindow, "closebtn")  # 点击事件: 关闭
        close_btn.setPixmap(QPixmap("image/closebtn_normal.png"))
        close_btn.setToolTip("<font size=4 color=#646464>关闭</font>")
        # min_btn.move(1100, 20)
        # close_btn.move(1150, 10)

        title_box = QHBoxLayout()
        title_box.addWidget(title)
        title_box.addStretch(1)
        title_box.addWidget(self.search_box, 3)
        title_box.addWidget(search)
        title_box.addStretch(6)
        title_box.addWidget(min_btn)
        title_box.addWidget(close_btn)
        self.title_bar.setLayout(title_box)

        self.title_bar.show()

    # 初始化主Frame
    def initMainFrame(self):
        self.main_frame = MyFrame(self)
        self.main_frame.setGeometry(0, 70, 1200, 660)
        self.main_frame.setStyleSheet("background-color:rgb(255,255,255)")
        self.initSongSheet()
        self.initSongList()
        self.main_frame.show()

    # 歌单###################################################################################
    def initSongSheet(self):
        self.song_sheet = MyFrame(self.main_frame)
        self.song_sheet.setGeometry(0, 0, 200, 660)
        self.song_sheet.setStyleSheet("background-color:rgb(244,244,246)")
        self.song_sheet.draw_line(199, 0, 199, 660)
        self.song_sheet.draw_line(0, 590, 200, 590)

        recommend = QVBoxLayout()
        recommend.addWidget(QLabel("<font size=4 color=#646464>推荐</font>"))
        recommend_list = []
        recommend_list.append(MyWidget(self.wait_to_handle, "find_music", "发现音乐"))
        recommend_list.append(MyWidget(self.wait_to_handle, "personal", "私人FM"))
        recommend_list.append(MyWidget(self.wait_to_handle, "mv", "MV"))
        recommend_list.append(MyWidget(self.wait_to_handle, "friend", "朋友"))
        for i in range(len(recommend_list)):
            recommend.addWidget(recommend_list[i])

        music = QVBoxLayout()
        music.addWidget(QLabel("<font size=4 color=#646464>我的音乐</font>"))
        music_list = []
        music_list.append(MyWidget(self.local_music, "local", "本地音乐"))
        music_list.append(MyWidget(self.wait_to_handle, "download", "下载管理"))
        music_list.append(MyWidget(self.wait_to_handle, "cloud", "我的音乐云盘"))
        music_list.append(MyWidget(self.wait_to_handle, "singer", "我的歌手"))
        for i in range(len(music_list)):
            music.addWidget(music_list[i])

        self.sheet = QVBoxLayout()
        my_sheet = QLabel("<font size=4 color=#646464>我的歌单</font>")
        add_music = MyLabel(self.add_music, "add_music")
        add_music.setPixmap(QPixmap("image/add_music_normal.png"))
        add_music_box = QHBoxLayout()
        add_music_box.addWidget(my_sheet)
        add_music_box.addStretch(1)
        add_music_box.addWidget(add_music)
        self.sheet.addLayout(add_music_box)
        self.sheet_list = []
        self.sheet_list.append(MyWidget(self.wait_to_handle, "like", "我喜欢的音乐"))
        self.sheet_list.append(MyWidget(self.wait_to_handle, "music", "歌单1"))
        self.sheet_list.append(MyWidget(self.wait_to_handle, "music", "歌单2"))
        for i in range(len(self.sheet_list)):
            self.sheet.addWidget(self.sheet_list[i])

        self.video = QVBoxLayout()
        my_movie = QLabel("<font size=4 color=#646464>我的视频</font>")
        add_movie = MyLabel(self.add_movie, "add_music")
        add_movie.setPixmap(QPixmap("image/add_music_normal.png"))
        add_movie_box = QHBoxLayout()
        add_movie_box.addWidget(my_movie)
        add_movie_box.addStretch(1)
        add_movie_box.addWidget(add_movie)
        self.video.addLayout(add_movie_box)
        self.video_list = []
        self.video_list.append(MyWidget(self.wait_to_handle, "mv", "视频列表1"))
        for i in range(len(self.video_list)):
            self.video.addWidget(self.video_list[i])

        box = QVBoxLayout()
        box.setAlignment(Qt.AlignTop)
        box.addLayout(recommend)
        box.addLayout(music)
        box.addLayout(self.sheet)
        box.addLayout(self.video)
        widget = QWidget()
        widget.setLayout(box)

        scroll_area = QScrollArea(self.song_sheet)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_area.setGeometry(0, 0, 198, 588)
        scroll_area.setWidget(widget)
        scroll_bar = MyScrollBar()
        scroll_area.setVerticalScrollBar(scroll_bar)

        self.song_picture = MyLabel(self.wait_to_handle, "playing", self.song_sheet)
        self.song_picture.setGeometry(0, 590, 70, 70)
        self.song_picture.setPixmap(QPixmap("image/playing_normal.png"))
        self.media_name = QLabel(self.song_sheet)
        self.media_name.move(75, 603)
        self.media_name.setText("<font size=4 color=#646464>media name</font>")
        self.singer_name = QLabel(self.song_sheet)
        self.singer_name.move(75, 627)
        self.singer_name.setText("<font size=4 color=#646464>singer name</font>")

        self.song_sheet.show()

    # 歌曲列表################################################################################
    def initSongList(self):
        self.song_list = MyFrame(self.main_frame)
        self.song_list.setGeometry(200, 0, 1000, 660)
        self.song_list.setStyleSheet("background-color:rgb(249,249,251)")

        scroll_area = QScrollArea(self.song_list)
        scroll_area.setWidgetResizable(False)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_area.setGeometry(0, 0, 1000, 660)
        scroll_bar = MyScrollBar()
        scroll_area.setVerticalScrollBar(scroll_bar)

        widget = QWidget()
        widget.setGeometry(0, 0, 1000, 660)
        scroll_area.setWidget(widget)

        self.top_widget = QWidget(widget)
        self.top_widget.setGeometry(0, 0, 1000, 150)
        self.top_widget.setStyleSheet("background-color:rgb(249,249,249)")
        date = MyLabel(self.wait_to_handle, "date", self.top_widget)
        date.setPixmap(QPixmap("image/date_normal.png"))
        date.setGeometry(50, 20, 99, 99)
        self.list_name = QLabel(self.top_widget)
        self.list_name.move(170, 50)
        self.list_name.setText("<font size=5 color=#646464>本地音乐</font>")

        self.current_path = QLabel("<font size=5 color=#646464></font>")
        choose_path = MyLabel(self.choose_path, "choose_path")
        choose_path.setPixmap(QPixmap("image/choose_path_normal.png"))
        clear = MyLabel(self.clear, "clear")
        clear.setPixmap(QPixmap("image/clear_normal.png"))
        hbox = QHBoxLayout(self.top_widget)
        hbox.setAlignment(Qt.AlignBottom|Qt.AlignRight)
        hbox.setContentsMargins(20, 20, 20, 20)
        hbox.addStretch(100)
        hbox.addWidget(self.current_path)
        hbox.addStretch(1)
        hbox.addWidget(choose_path)
        hbox.addStretch(1)
        hbox.addWidget(clear)
        hbox.addStretch(1)

        self.song_widget = QTableWidget(widget)
        self.song_widget.setGeometry(0, 150, 1000, 510)
        self.song_widget.setStyleSheet("background-color:rgb(249,249,249)")
        self.song_widget.setFrameShape(QFrame.NoFrame)
        self.song_widget.setSelectionBehavior(QTableWidget.SelectRows)  # 选择行
        self.song_widget.setSelectionMode(QTableWidget.SingleSelection)  # 选择单行
        self.song_widget.setEditTriggers(QTableWidget.NoEditTriggers)  # 不可编辑
        self.song_widget.verticalHeader().setVisible(False)  # 隐藏垂直表头
        self.song_widget.setAutoScroll(False)  # 去掉自动滚动
        self.song_widget.resizeRowsToContents()  # 行高与内容相匹配
        self.song_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 从不显示水平滚动条
        self.song_widget.setVerticalScrollBar(MyScrollBar())  # 设置滚动条
        self.song_widget.setAlternatingRowColors(True)

        self.song_widget.setColumnCount(5)
        self.song_widget.setColumnWidth(0, 50)
        self.song_widget.setColumnWidth(1, 340)
        self.song_widget.setColumnWidth(2, 240)
        self.song_widget.setColumnWidth(3, 270)
        self.song_widget.setColumnWidth(4, 100)

        # 设置水平表头
        header1 = MyTableWidgetItem("")
        header2 = MyTableWidgetItem("音乐标题")
        header3 = MyTableWidgetItem("歌手")
        header4 = MyTableWidgetItem("专辑")
        header5 = MyTableWidgetItem("时长")
        self.song_widget.setHorizontalHeaderItem(0, header1)
        self.song_widget.setHorizontalHeaderItem(1, header2)
        self.song_widget.setHorizontalHeaderItem(2, header3)
        self.song_widget.setHorizontalHeaderItem(3, header4)
        self.song_widget.setHorizontalHeaderItem(4, header5)

        # for root, dirs, files in os.walk("./music"):
        #     # print(files)
        #     # 遍历目录下音乐
        #     for i in range(len(files)):
        #         self.song_widget.setRowCount(len(files))
        #         # print(os.path.join(file))
        #         # 加入播放列表
        #         media = QUrl("music/"+os.path.join(files[i]))
        #         self.play_list.addMedia(QMediaContent(media))
        #         # 显示在表格上
        #         item1 = MyTableWidgetItem(str(i+1))
        #         item2 = MyTableWidgetItem(files[i])
        #
        #         self.song_widget.setItem(i, 0, MyTableWidgetItem(item1))
        #         self.song_widget.setItem(i, 1, MyTableWidgetItem(item2))

        self.song_list.show()

    # 初始化底部播放控制栏####################################################################
    def initBottomBar(self):
        self.bottom_bar = MyFrame(self)
        self.bottom_bar.setGeometry(0, 730, 1200, 70)
        self.bottom_bar.setStyleSheet("background-color:rgb(244,244,246)")
        self.bottom_bar.draw_line(0, 0, 1200, 0)

        prev_btn = MyLabel(self.prev, "prev")  # 上一首
        prev_btn.setPixmap(QPixmap("image/prev_normal.png"))
        prev_btn.setToolTip("<font size=4 color=#646464>上一首</font>")
        prev_btn.setAlignment(Qt.AlignVCenter)
        next_btn = MyLabel(self.next, "next")  # 下一首
        next_btn.setPixmap(QPixmap("image/next_normal.png"))
        next_btn.setToolTip("<font size=4 color=#646464>下一首</font>")
        next_btn.setAlignment(Qt.AlignVCenter)
        self.play_btn = MyLabel(self.play, "play")  # 播放
        self.play_btn.setPixmap(QPixmap("image/play_normal.png"))
        self.play_btn.setToolTip("<font size=4 color=#646464>播放</font>")
        self.play_btn.setAlignment(Qt.AlignVCenter)
        pause_btn = MyLabel(self.pause, "pause")  # 暂停
        pause_btn.setPixmap(QPixmap("image/pause_normal.png"))
        pause_btn.setAlignment(Qt.AlignVCenter)

        self.current_time = QLabel("<font size=3 color=#646464>00:00</font>")
        self.current_time.setAlignment(Qt.AlignVCenter)
        self.total_time = QLabel("<font size=3 color=#646464>00:00</font>")
        self.total_time.setAlignment(Qt.AlignVCenter)

        self.slider = MySlider1(Qt.Horizontal)
        self.slider.setFocusPolicy(Qt.NoFocus)
        self.slider.setSliderPosition(0)

        self.horn = MyLabel(self.mute, "horn2")
        self.horn.setPixmap(QPixmap("image/horn2_normal.png"))
        self.horn.setToolTip("<font size=4 color=#646464>静音</font>")
        self.horn.setAlignment(Qt.AlignVCenter)

        self.volume = MySlider2(Qt.Horizontal)
        self.volume.setFocusPolicy(Qt.NoFocus)
        self.volume.setMaximum(100)
        self.volume.setSliderPosition(100)
        self.volume.valueChanged.connect(self.volume_changed)
        self.volume.setToolTip("<font size=4 color=#646464>"+str(self.volume.value())+"</font>")

        self.mode = MyLabel(self.mode_changed, "mode1")
        self.mode.setPixmap(QPixmap("image/mode1_normal.png"))
        self.mode.setToolTip("<font size=4 color=#646464>顺序播放</font>")
        self.mode.setAlignment(Qt.AlignVCenter)

        lyric = MyLabel(self.show_lyric, "lyric")
        lyric.setPixmap(QPixmap("image/lyric_normal.png"))
        lyric.setAlignment(Qt.AlignVCenter)

        play_list = MyLabel(self.show_list, "play_list")
        play_list.setPixmap(QPixmap("image/play_list_normal.png"))
        play_list.setAlignment(Qt.AlignVCenter)

        bottom_box = QHBoxLayout()
        bottom_box.addStretch(2)
        bottom_box.addWidget(prev_btn)
        bottom_box.addStretch(1)
        bottom_box.addWidget(self.play_btn)
        bottom_box.addStretch(1)
        bottom_box.addWidget(next_btn)
        bottom_box.addStretch(3)
        bottom_box.addWidget(self.current_time)
        bottom_box.addStretch(1)
        bottom_box.addWidget(self.slider, 50)
        bottom_box.addStretch(1)
        bottom_box.addWidget(self.total_time)
        bottom_box.addStretch(3)
        bottom_box.addWidget(self.horn)
        bottom_box.addWidget(self.volume, 10)
        bottom_box.addStretch(1)
        bottom_box.addWidget(self.mode)
        bottom_box.addStretch(1)
        bottom_box.addWidget(lyric)
        bottom_box.addStretch(1)
        bottom_box.addWidget(play_list)

        self.bottom_bar.setLayout(bottom_box)
        self.bottom_bar.show()

    # 最小化点击事件
    def minWindow(self):
        self.showMinimized()

    # 关闭点击事件
    def closeWindow(self):
        self.close()

    def search(self):
        return

    def add_music(self):
        text, ok = QInputDialog.getText(self, "新建歌单", "请输入你的歌单名", QLineEdit.Normal, "新建歌单")
        if ok:
            self.sheet_list.append(MyWidget(self.wait_to_handle, "music", text))
            self.sheet.addWidget(self.sheet_list[len(self.sheet_list)-1])

    def add_movie(self):
        text, ok = QInputDialog.getText(self, "新建视频列表", "请输入你的列表名", QLineEdit.Normal, "新建视频列表")
        if ok:
            self.video_list.append(MyWidget(self.wait_to_handle, "movie", text))
            self.video.addWidget(self.video_list[len(self.video_list) - 1])

    def change_list(self):
        return

    # 上一首
    def prev(self):
        self.play_list.previous()

    # 下一首
    def next(self):
        self.play_list.next()

    # 播放
    def play(self):
        self.player.play()
        self.play_btn.func = self.pause
        self.play_btn.which = "pause"
        self.play_btn.setPixmap(QPixmap("image/pause_normal.png"))
        self.play_btn.setToolTip("<font size=4 color=#646464>播放</font>")

    # 暂停
    def pause(self):
        self.player.pause()
        self.play_btn.func = self.play
        self.play_btn.which = "play"
        self.play_btn.setPixmap(QPixmap("image/play_normal.png"))
        self.play_btn.setToolTip("<font size=4 color=#646464>暂停</font>")

    # 改变进度条
    def progress_changed(self):
        self.player.setPosition(self.slider.pos())

    def position_changed(self):
        self.slider.setSliderPosition(self.player.position())

    def duration_changed(self):
        self.media_name.setText("<font size=4 color=#646464>" + str(self.player.media()) + "</font>")
        print(self.player.duration())
        # self.slider.setSliderPosition(0)  # 置为0

        duration = int(self.player.duration()/1000)
        self.slider.setMaximum(duration)
        total_time = QTime(duration/3600, duration % 3600/60, duration & 60)
        time_format = "mm:ss"
        if duration > 3600:
            time_format = "hh:mm:ss"
        self.total_time.setText("<font size=3 color=#646464>"+total_time.toString(time_format)+"</font>")

    # 改变播放媒体
    def media_changed(self):
        return
        # self.media_name.setText("<font size=4 color=#646464>" + str(self.player.media()) + "</font>")
        # print(self.player.duration())
        # self.slider.setSliderPosition(0)  # 置为0
        # self.slider.setMaximum(self.player.duration()/1000)
        # self.total_time.setText("<font size=3 color=#646464>"+str(self.player.duration())+"</font>")

    # 静音
    def mute(self):
        if self.horn.which == "horn2":
            self.horn.which = "horn0"
            self.horn.setPixmap(QPixmap("image/horn0_normal"))
            self.horn.setToolTip("<font size=4 color=#646464>恢复音量</font>")
            self.volume.setValue(0)
        elif self.horn.which == "horn0":
            self.horn.which = "horn2"
            self.horn.setPixmap(QPixmap("image/horn2_normal"))
            self.horn.setToolTip("<font size=4 color=#646464>静音</font>")
            self.volume.setValue(100)

    # 改变音量
    def volume_changed(self):
        self.volume.setToolTip("<font size=4 color=#646464>" + str(self.volume.value()) + "</font>")
        self.player.setVolume(self.volume.value())  # 改变播放音量
        if self.volume.value() >= 50:
            self.horn.which = "horn2"
            self.horn.setPixmap(QPixmap("image/horn2_normal"))
            self.horn.setToolTip("<font size=4 color=#646464>静音</font>")
        elif self.volume.value() == 0:
            self.horn.which = "horn0"
            self.horn.setPixmap(QPixmap("image/horn0_normal"))
            self.horn.setToolTip("<font size=4 color=#646464>恢复音量</font>")
        elif 0 < self.volume.value() < 50:
            self.horn.which = "horn1"
            self.horn.setPixmap(QPixmap("image/horn1_normal"))
            self.horn.setToolTip("<font size=4 color=#646464>静音</font>")


    # 点击切换播放模式，更改mode.which属性，更改图片
    # mode1 顺序播放
    # mode2 循环播放
    # mode3 单曲循环
    # mode4 随机播放
    def mode_changed(self):
        def mode1():
            self.play_list.setPlaybackMode(QMediaPlaylist.Loop)
            self.mode.which = "mode2"
            self.mode.setPixmap(QPixmap("image/mode2_norma2.png"))
            self.mode.setToolTip("<font size=4 color=#646464>循环播放</font>")

        def mode2():
            self.play_list.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
            self.mode.which = "mode3"
            self.mode.setPixmap(QPixmap("image/mode3_norma3.png"))
            self.mode.setToolTip("<font size=4 color=#646464>单曲循环</font>")

        def mode3():
            self.play_list.setPlaybackMode(QMediaPlaylist.Random)
            self.mode.which = "mode4"
            self.mode.setPixmap(QPixmap("image/mode4_norma4.png"))
            self.mode.setToolTip("<font size=4 color=#646464>随机播放</font>")

        def mode4():
            self.play_list.setPlaybackMode(QMediaPlaylist.Sequential)
            self.mode.which = "mode1"
            self.mode.setPixmap(QPixmap("image/mode1_norma1.png"))
            self.mode.setToolTip("<font size=4 color=#646464>顺序播放</font>")
        # 字典映射实现switch-case
        switch = {
            "mode1": mode1,
            "mode2": mode2,
            "mode3": mode3,
            "mode4": mode4,
        }
        switch.get(self.mode.which)()

    def show_lyric(self):
        return

    def show_list(self):
        return

    def local_music(self):
        # self.song_list = MyFrame(self.main_frame)
        # self.song_list.setGeometry(200, 0, 1000, 660)
        # self.song_list.setStyleSheet("background-color:rgb(249,249,251)")
        # self.listvbox = QVBoxLayout()
        # self.song_list.setLayout(self.listvbox)
        # self.song_list.show()
        return

    def choose_path(self):
        dir = QFileDialog.getExistingDirectory(self, "选取文件夹", "D:/PythonWorkSpace/AwesomePlayer/")
        self.current_path.setText("<font size=4 color=#646464>"+dir+"</font>")
        self.song_widget.clearContents()  # 清空表格，不包括标题头
        self.play_list.clear()  # 清空播放列表
        for root, dirs, files in os.walk(dir):
            # print(files)
            # 遍历目录下音乐
            for i in range(len(files)):
                self.song_widget.setRowCount(len(files))
                # print(dir+"/"+os.path.join(files[i]))
                # 加入播放列表
                media = QUrl(dir+"/"+os.path.join(files[i]))
                self.play_list.addMedia(QMediaContent(media))
                # 显示在表格上
                item1 = MyTableWidgetItem(str(i+1))
                item2 = MyTableWidgetItem(files[i])
                item3 = MyTableWidgetItem(files[i])
                item4 = MyTableWidgetItem(files[i])
                item5 = MyTableWidgetItem(files[i])

                self.song_widget.setItem(i, 0, MyTableWidgetItem(item1))
                self.song_widget.setItem(i, 1, MyTableWidgetItem(item2))
                # self.song_widget.setItem(i, 2, MyTableWidgetItem(item3))
                # self.song_widget.setItem(i, 3, MyTableWidgetItem(item4))
                # self.song_widget.setItem(i, 4, MyTableWidgetItem(item5))

    def clear(self):
        self.current_path.setText("<font size=4 color=#646464></font>")
        self.song_widget.clearContents()  # 清空表格，不包括标题头
        self.play_list.clear()  # 清空播放列表

    def wait_to_handle(self):
        pass

    def keyPressEvent(self, e):
        print(e.key)
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Enter or e.key() == Qt.Key_Return:
            # Enter为小键盘回车 Return为大键盘的回车
            return  # To be filled
        if e.key() == Qt.Key_F1:
            return  # To be filled


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
