#继承重写QLabel，备用方案
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyLabel(QLabel):
    sendmsg = pyqtSignal(QPixmap)
    def __init__(self, Parent=None):
        super(QLabel, self).__init__(Parent)
        self.img_path = str()
        self.regions = list()
        self.imgs = list()
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.flag = False
        self.Enable = True


    def set_path(self , path:str):
        self.img_path = path
    def mousePressEvent(self, ev:QMouseEvent):
        if(self.Enable):
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
        if(self.Enable):
            if event.button() == Qt.LeftButton:
                temp_x1 = min(self.x1, self.x2)
                temp_y1 = min(self.y1, self.y2)
                temp_x2 = max(self.x1, self.x2)
                temp_y2 = max(self.y1, self.y2)
                self.x1 = temp_x1
                self.y1 = temp_y1
                self.x2 = temp_x2
                self.y2 = temp_y2
                if abs(self.x2 - self.x1) < 10 or abs(self.y2 - self.y1) < 10:
                    print(abs(self.x2 - self.x1))
                    print(abs(self.y2 - self.y1))
                else:
                    this_region = [self.x1, self.y1, abs(self.x2 - self.x1), abs(self.y2 - self.y1)]
                    if self.img_path == "":
                        res = self.pixmap().copy(
                            QRect(self.x1, self.y1, abs(self.x2 - self.x1), abs(self.y2 - self.y1)))
                    else:
                        image = QPixmap(self.img_path)
                        rat_w = image.width() / self.width()
                        rat_h = image.height() / self.height()
                        img_region = [self.x1 * rat_w, self.y1 * rat_h, abs(self.x2 - self.x1) * rat_w,
                                      abs(self.y2 - self.y1) * rat_h]
                        res = image.copy(QRect(self.x1 * rat_w, self.y1 * rat_h, abs(self.x2 - self.x1) * rat_w,
                                               abs(self.y2 - self.y1) * rat_h))
                    self.regions.append(this_region)
                    self.imgs.append(res)
                    self.sendmsg.emit(res)
                self.Enable = False




    def mouseMoveEvent(self, ev:QMouseEvent):
        if self.flag :
            self.x2 = ev.x()
            self.y2 = ev.y()

    def paintEvent(self, ev:QPaintEvent):
        super(MyLabel , self).paintEvent(ev)
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QPen(Qt.red , 5 , Qt.SolidLine))
        painter.drawRect(min(self.x1 ,self.x2),min(self.y1 , self.y2) , abs(self.x2 - self.x1), abs(self.y2 - self.y1))
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
    def Remove_last(self):
        self.regions.pop()
        self.imgs.pop()
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.update()