# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Data\pythonstudy\pyqt5\matplotlib\plt.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(870, 796)
        self.pbtn_static = QtWidgets.QPushButton(Form)
        self.pbtn_static.setGeometry(QtCore.QRect(710, 160, 75, 23))
        self.pbtn_static.setObjectName("pbtn_static")
        self.pbtn_dynamic = QtWidgets.QPushButton(Form)
        self.pbtn_dynamic.setGeometry(QtCore.QRect(710, 660, 75, 23))
        self.pbtn_dynamic.setObjectName("pbtn_dynamic")
        self.widget = MatplotlibWidget(Form)
        self.widget.setGeometry(QtCore.QRect(90, 80, 491, 291))
        self.widget.setObjectName("widget")
        self.widget_2 = MatplotlibWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(50, 470, 471, 291))
        self.widget_2.setObjectName("widget_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pbtn_static.setText(_translate("Form", "static"))
        self.pbtn_dynamic.setText(_translate("Form", "dynamic"))

from MatplotlibWidget import MatplotlibWidget
