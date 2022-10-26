from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class mapping():
    # #选取坐标范围0:左上角坐标x；1左上角坐标y；2：选框宽度；3：选框高度
    Region=[]
    mouse_pos = [0,0]
    Watch_Mouse_Pos = QtCore.QTimer()
    def __init__(self , Control:QLabel , Signal:pyqtSignal):
        self.control = Control
        self.signal = Signal
        self.Img_Source = self.control.pixmap()
        self.Watch_Mouse_Pos.timeout.connect(self.Draw)

    def start_Draw(self):
        self.Watch_Mouse_Pos.start(50)
    def stop_Draw(self):
        self.Watch_Mouse_Pos.stop()

    def Get_Region_Info(self):
        return self.Region
    def Get_Region_Img(self):
        return self.Img_Select

    def Draw(self):
        draw = QPainter()
        pen = QPen()
        draw.begin(self.control)

        draw.setPen(QPen(Qt.black , 2 ,Qt.DashLine))
        draw.drawLine(80 ,10 , 80 , 160)
        draw.end()

    def test_Draw(self):
        draw = QPainter(self.control.pixmap())
        pen = QPen()

        draw.setPen(QPen(Qt.black, 10, Qt.DashLine))
        draw.drawRect(80, 10, 180, 160)
        draw.end()
        self.signal.emit()



