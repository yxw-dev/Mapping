#继承重写QLabel，备用方案
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyLabel(QLabel):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    _width = 0
    _height = 0
    flag = False
    sendmsg = pyqtSignal(QPixmap)

    def __init__(self, Parent=None):
        super(QLabel, self).__init__(Parent)
        self.regions = list()
        self.imgs = list()

    def mousePressEvent(self, ev:QMouseEvent):
        if ev.button() == Qt.LeftButton:
            self.flag = True
            self.x1 = ev.x()
            self.y1 = ev.y()
            self.x2 = ev.x()
            self.y2 = ev.y()
        if ev.button() == Qt.RightButton:
            self.x1 = 0
            self.x2 = 0
            self.y1 = 0
            self.y2 = 0
            self.regions.clear()
            self.imgs.clear()
            self.update()

    def mouseReleaseEvent(self, event:QMouseEvent):
        self.flag = False
        res = self.pixmap().copy(QRect(self.x1 ,self.y1 , abs(self.x2 - self.x1), abs(self.y2 - self.y1)))
        this_region = [self.x1 ,self.y1 , abs(self.x2 - self.x1), abs(self.y2 - self.y1)]
        self.regions.append(this_region)
        self.imgs.append(res)
        self.sendmsg.emit(res)

    def mouseMoveEvent(self, ev:QMouseEvent):
        if self.flag :
            self.x2 = ev.x()
            self.y2 = ev.y()

    def paintEvent(self, ev:QPaintEvent):
        super(MyLabel , self).paintEvent(ev)
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QPen(Qt.red , 5 , Qt.SolidLine))
        painter.drawRect(self.x1 ,self.y1 , abs(self.x2 - self.x1), abs(self.y2 - self.y1))
        for region in self.regions:
            painter.drawRect(region[0], region[1], region[2], region[3])
        font = QFont()
        font.setPointSize(8)
        painter.setFont(font)
        self.update()

    # def Draw_rect(self , x1,y1,x2,y2):
    #     draw = QPainter(self.pixmap())
    #     pen = QPen()
    #     draw.setPen(QPen(Qt.black, 1, Qt.DashLine))
    #     draw.drawRect(x1,y1,abs(x2-x1),abs(y2-y1))
    #     draw.end()
