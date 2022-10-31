# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QWidget, QFileDialog
import My_Label
import Ini_operate
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2560, 1440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_ini = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_ini.setObjectName("pushButton_ini")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_3.addWidget(self.pushButton_ini)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.widget_3)
        self.horizontalLayout_5.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_2)
        self.tabWidget.setMinimumSize(QtCore.QSize(919, 1040))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 1400))
        self.tabWidget.setObjectName("tabWidget")
        #self.tab = QtWidgets.QWidget()
        #self.tab.setObjectName("tab")
        #self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.widget_2)
        self.tabWidget_2.setMinimumSize(QtCore.QSize(919, 1040))
        self.tabWidget_2.setMaximumSize(QtCore.QSize(16777215, 1400))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_1 = My_Label.MyLabel(self.tab_2)
        self.label_1.resize(919, 1380)
        self.label_1.setObjectName("label_1")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget_2)
        self.horizontalLayout_5.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2560, 34))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #全局变量：报告文件路径Path(list)、检验报告单文件path（str）、检验报告单结果(dict)、报告文件结果（dict）
        self.report_path = []
        self.check_report = ""
        self.check_report_result = dict()
        self.report_result = dict()

        #表格插入表头
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["检验标准" ,"报告数据","检验结果","核对结果"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #绑定信号槽
        self.pushButton.clicked.connect(self.Get_Report_path)
        self.pushButton_ini.clicked.connect(self.save_ini)
        self.pushButton_2.clicked.connect(self.Get_Check_Report_path)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "导入报告"))
        self.pushButton_ini.setText(_translate("MainWindow", "保存位置信息"))
        self.pushButton_2.setText(_translate("MainWindow", "导入校验报告单"))
        self.label.setText(_translate("MainWindow", "核对结果："))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "检验报告单"))
        self.menu.setTitle(_translate("MainWindow", "导入"))
        self.action.setText(_translate("MainWindow", "人员报告"))
        self.action_2.setText(_translate("MainWindow", "实验报告"))

    def Add_img(self, path: list):
        num = 0
        self.labs = list()
        for i in path:
            tab = QWidget()
            lab1 = My_Label.MyLabel(tab)
            lab1.resize(919, 1380)
            self.tabWidget.addTab(tab, str(num))
            temp_pic = QPixmap(i).scaled(919, 1380)
            lab1.set_path(i)
            lab1.setPixmap(temp_pic)
            self.labs.append(lab1)
            self.labs[-1].sendmsg.connect(self.Frush_ui)
            num = num + 1
        print(self.labs)

    def Get_Report_path(self):
        self.report_path.clear()
        path = QFileDialog.getExistingDirectory()
        if len(path) == 0:
            return
        for file_name in os.listdir(path):
            str1 = file_name.split(".")[-1]
            if str1 == "png" or str1 == "jpg" or str1 == "bmp":
                self.report_path.append(file_name)
                print(file_name)
        self.Add_img(self.report_path)

    def Get_Check_Report_path(self):
        path = QFileDialog.getOpenFileName()
        str1 = path[0].split(".")[-1]
        if str1 == "png" or str1 == "jpg" or str1 == "bmp":
            self.check_report = path[0]
        tab = QWidget()

        tem_pic = QPixmap(self.check_report).scaled(919, 1380)
        self.label_1.setPixmap(tem_pic)
        self.label_1.set_path(self.check_report)
        self.label_1.sendmsg.connect(self.Frush_ui)

    def save_ini(self):
        region_info = Ini_operate.ini_operate()
        c , r , img_1 , img2 = region_info.get_region()
        print(c)
        print(r)
        print(img_1)
        print(img2)
        # region_info.save_region(self.label_1.regions , self.labs[0].regions , [self.label_1.width() , self.label_1.height()] , [self.labs[0].width() , self.labs[0].height()])
    #type为0,添加字典数据至第一第二列，为1添加字典数据至第三第四列
    def frush_Chart(self , dat:dict , type:int):
        num = len(dat)
        self.tableWidget.setRowCount(num + 1)
        str1 = list(dat.keys())
        str2 = list(dat.values())
        if type == 0:
            for i in range(num):
                item1 = QTableWidgetItem(str1[i])
                item2 = QTableWidgetItem(str(str2[i]))
                self.tableWidget.setItem(i , 0 , item1)
                self.tableWidget.setItem(i, 1, item2)
        if type == 1:
            for i in range(num):
                item3 = QTableWidgetItem(str(str2[i]))
                self.tableWidget.setItem(i , 2 , item3)
                #判断程序
                item4 = QTableWidgetItem("合格")
                self.tableWidget.setItem(i, 4, item4)

    def Insert_Chart(self , value , row , col):
        if col > 5:
            return
        if row > (self.tableWidget.rowCount()-1):
            self.tableWidget.setRowCount(row + 1)
        item1 = QTableWidgetItem(str(value))
        self.tableWidget.setItem(int(row), int(col), item1)

    def Frush_table(self , c:dict , r:dict):
        self.tableWidget.setRowCount(c.keys().__len__())
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["检测名目", "检验结果", "报告数据",  "核对结果"])
        index = 0
        for i in c.keys():
            item1 = QTableWidgetItem(str(i))
            item2 = QTableWidgetItem(str(c[i]))
            self.tableWidget.setItem(index, int(0), item1)
            self.tableWidget.setItem(index, int(1), item2)
            index = index + 1
        try:
            for i in range(0 , len(r)):
                item1 = QTableWidgetItem(list(r.values())[i])
                print(list(r.keys())[i])
                if list(r.keys())[i] in list(c.keys()):
                    ind = list(c.keys()).index(list(r.keys())[i] )
                    if list(c.values())[ind] == list(r.values())[i]:
                        str1 = "√"
                    else:
                        str1 = "×"
                    item2 = QTableWidgetItem(str1)
                    self.tableWidget.setItem(ind, int(2), item1)
                    self.tableWidget.setItem(ind, int(3), item2)
        except:
            My_Label.QMessageBox.show("error")


