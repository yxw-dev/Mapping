import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from untitled import *
import Mapping
import My_Label

class MyMainWindow(QMainWindow, Ui_MainWindow):
    Finish_Draw = pyqtSignal()
    dict_c = {"吡咯烷酮类似物":[0,0.002] , "6-羟基环氧吡咯噁嗪类似物":[0,0.002] , "7-羟基环氧吡咯噁嗪类似物":[0,0.002] ,
              "杂质H":[0,0.0002] , "环氧四氢呋喃类似物":[0,0.001] , "杂质D与环氧四氢呋喃类似物的和":[0,0.001] , "其他杂质":[0,0.0015],
              "总杂质":[0,0.01]}
    dict_r = {"吡咯烷酮类似物":0.0002 , "6-羟基环氧吡咯噁嗪类似物":0.0003 , "7-羟基环氧吡咯噁嗪类似物":0.0003 , "杂质H":0.0006,
              "环氧四氢呋喃类似物":0.0001 , "杂质D与环氧四氢呋喃类似物的和":0.0002 , "其他单一杂质":0.0005 ,"总杂质":0.004}
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.frush_Chart(self.dict_c , 0)
        self.frush_Chart(self.dict_r , 1)

    def Frush_ui(self, region):
        # self.update()
        if self.sender() == self.label_1:
            img = self.label_1.imgs[0]
            print("检验单图片")
        else:
            for i in self.labs:
                if self.sender() == i:
                    img = i.imgs[0]
                    print("报告图片")
        print(img)

        #写表格
        self.Insert_Chart("11" , 9,1)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.showMaximized()
    sys.exit(app.exec_())