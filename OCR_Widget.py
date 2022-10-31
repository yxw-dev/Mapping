# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OCR_Widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setMinimumSize(QtCore.QSize(0, 120))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 700, 320))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 120))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(0, 40))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 120))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 120))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(102, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Yes = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_Yes.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton_Yes.setObjectName("pushButton_Yes")
        self.horizontalLayout.addWidget(self.pushButton_Yes)
        spacerItem1 = QtWidgets.QSpacerItem(103, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_No = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_No.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton_No.setObjectName("pushButton_No")
        self.horizontalLayout.addWidget(self.pushButton_No)
        spacerItem2 = QtWidgets.QSpacerItem(102, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.widget_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", ":"))
        self.pushButton_Yes.setText(_translate("Dialog", "保存"))
        self.pushButton_No.setText(_translate("Dialog", "取消"))

    def show_picture(self , img:QPixmap):
        temp_pic = QPixmap(img).scaled(700, 320)
        self.label.setPixmap(temp_pic)
        i = temp_pic.toImage()
        i.size()

    def set_text(self , str:list):
        try:
            self.lineEdit.setText(str[0])
            self.lineEdit_2.setText(str[1])
        except:
            QMessageBox.show("未匹配到相对应数据")