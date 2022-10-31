import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from untitled import *
from OCR_Widget import *
import Mapping
import My_Label
import easyocr
import numpy as np

class MyMainWindow(QMainWindow, Ui_MainWindow):
    Finish_Draw = pyqtSignal()
    # dict_c = {"吡咯烷酮类似物":[0,0.002] , "6-羟基环氧吡咯噁嗪类似物":[0,0.002] , "7-羟基环氧吡咯噁嗪类似物":[0,0.002] ,
    #           "杂质H":[0,0.0002] , "环氧四氢呋喃类似物":[0,0.001] , "杂质D与环氧四氢呋喃类似物的和":[0,0.001] , "其他杂质":[0,0.0015],
    #           "总杂质":[0,0.01]}
    # dict_r = {"吡咯烷酮类似物":0.0002 , "6-羟基环氧吡咯噁嗪类似物":0.0003 , "7-羟基环氧吡咯噁嗪类似物":0.0003 , "杂质H":0.0006,
    #           "环氧四氢呋喃类似物":0.0001 , "杂质D与环氧四氢呋喃类似物的和":0.0002 , "其他单一杂质":0.0005 ,"总杂质":0.004}
    dict_c = dict()
    dict_r = dict()

    def __init__(self , ocr:Ui_Dialog):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
        self.ww = QtWidgets.QDialog()
        self.ocr_result = ocr
        self.ocr_result.setupUi(self.ww)
        self.ocr_result.pushButton_Yes.clicked.connect(self.Yes_btn)
        self.ocr_result.pushButton_No.clicked.connect(self.No_btn)
        self.frush_Chart(self.dict_c , 0)
        self.frush_Chart(self.dict_r , 1)

    def Yes_btn(self):
        self.foucs_lab.Enable = True
        if (self.label_1 == self.foucs_lab):
            self.dict_c[self.ocr_result.lineEdit.text()] = self.ocr_result.lineEdit_2.text()
        else:
            self.dict_r[self.ocr_result.lineEdit.text()] = self.ocr_result.lineEdit_2.text()
        self.Frush_table(self.dict_c , self.dict_r)
        self.ww.close()
    def No_btn(self):
        self.foucs_lab.Enable = True
        self.foucs_lab.Remove_last()
        self.ww.close()

    def Frush_ui(self, region):
        if self.sender() == self.label_1:
            image = self.label_1.imgs[-1].toImage()
            size = image.size()
            s = image.bits().asstring(size.width() * size.height() * image.depth() // 8)
            arr = np.fromstring(s, dtype=np.uint8).reshape((size.height(), size.width(), image.depth() // 8))
            result = self.reader.readtext(arr, detail=0)
            if len(result) < 2:
                QMessageBox.show("未找到数据对")
            else:
                self.ocr_result.set_text(result)
            print("检验单图片")
            self.ocr_result.show_picture(self.label_1.imgs[-1])
            self.foucs_lab = self.label_1
        else:
            for i in self.labs:
                if self.sender() == i:
                    img = i.imgs[-1].toImage()
                    size = img.size()
                    s = img.bits().asstring(size.width() * size.height() * img.depth() // 8)
                    arr = np.fromstring(s, dtype=np.uint8).reshape((size.height(), size.width(), img.depth() // 8))
                    result = self.reader.readtext(arr, detail=0)
                    if len(result) < 2:
                        QMessageBox.show("未找到数据对")
                    else:
                        self.ocr_result.set_text(result)
                    print("报告图片")
                    self.ocr_result.show_picture(img)
                    self.foucs_lab = i
        self.ww.show()

        #ocr识别，提取数值，根据表格来源填写
        #写表格
        # self.Insert_Chart("11" , 9,1) #第九行第一列写入‘11’
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ocr_win = Ui_Dialog()
    win = MyMainWindow(ocr_win)
    win.showMaximized()
    sys.exit(app.exec_())