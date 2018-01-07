# -*- coding:utf-8 -*-
import cgitb

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ctypes.wintypes import *
cgitb.enable(format='text')

PADDING = 2
UP, DOWN, LEFT, RIGHT, LEFTTOP, LEFTBOTTOM, RIGHTTOP, RIGHTBOTTOM, UNDIRECT = range(9)
HTLEFT = 10
HTRIGHT = 11
HTTOP = 12
HTTOPLEFT = 13
HTTOPRIGHT = 14
HTBOTTOM = 15
HTBOTTOMLEFT = 16
HTBOTTOMRIGHT = 17
HTCAPTION = 2


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            # QApplication.postEvent(self, QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

# 如下方法会导致无法点击label，边框改变大小的箭头各种bug
    # def isInTitle(self, xPos, yPos):
    #     return yPos < 30
    #
    # def GET_X_LPARAM(self, param):
    #     return param & 0xffff
    #
    # def GET_Y_LPARAM(self, param):
    #     return param >> 16
    #
    # def nativeEvent(self, eventType, message):
    #     result = 0
    #     msg2 = ctypes.wintypes.MSG.from_address(message.__int__())
    #     minV,maxV = 18,22
    #     if msg2.message == 0x0084:
    #         xPos = self.GET_X_LPARAM(msg2.lParam) - self.frameGeometry().x()
    #         yPos = self.GET_Y_LPARAM(msg2.lParam) - self.frameGeometry().y()
    #
    #         if(minV < xPos < maxV):
    #             result = HTLEFT
    #         elif((self.width() - maxV) < xPos < (self.width() - minV)):
    #             result = HTRIGHT
    #         elif(minV < yPos < maxV):
    #             result = HTTOP
    #         elif((self.height() - maxV) < yPos < (self.height() - minV)):
    #             result = HTBOTTOM
    #         elif(minV < xPos < maxV and minV < yPos < maxV):
    #             result = HTTOPLEFT
    #         elif((self.width() - maxV) < xPos < (self.width() - minV) and minV < yPos < maxV):
    #             result = HTTOPRIGHT
    #         elif(minV < xPos < maxV and (self.height() - maxV) < yPos < (self.height() - minV)):
    #             result = HTBOTTOMLEFT
    #         elif((self.width() - maxV) < xPos < (self.width() - minV) and (self.height() - maxV) < yPos < (self.height() - minV)):
    #             result = HTBOTTOMRIGHT
    #         else:
    #             result = HTCAPTION
    #         return True, result
    #     ret = QMainWindow.nativeEvent(self, eventType, message)
    #     return ret

# if __name__ == '__main__':
#     app = QApplication([])
#     w = MyWindow()
#     w.show()
#     app.exec_()
