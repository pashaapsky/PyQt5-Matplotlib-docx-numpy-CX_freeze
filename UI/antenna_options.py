# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'antenna_options.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog_antenns(object):
    def setupUi(self, dialog_antenns):
        dialog_antenns.setObjectName("dialog_antenns")
        dialog_antenns.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog_antenns.resize(950, 402)
        dialog_antenns.setMinimumSize(QtCore.QSize(950, 402))
        dialog_antenns.setMaximumSize(QtCore.QSize(9999, 9999))
        self.gridLayout = QtWidgets.QGridLayout(dialog_antenns)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(dialog_antenns)
        self.scrollArea.setMinimumSize(QtCore.QSize(180, 290))
        self.scrollArea.setMaximumSize(QtCore.QSize(9999, 9999))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 219, 341))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setMinimumSize(QtCore.QSize(160, 210))
        self.listWidget.setMaximumSize(QtCore.QSize(9999, 9999))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.addWidget(self.scrollArea)
        self.scrollArea_2 = QtWidgets.QScrollArea(dialog_antenns)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(280, 0))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(9999, 9999))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 278, 341))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget.setMinimumSize(QtCore.QSize(240, 267))
        self.tableWidget.setMaximumSize(QtCore.QSize(9999, 9999))
        self.tableWidget.setAutoScrollMargin(10)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setMinimumSectionSize(5)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.addWidget(self.scrollArea_2)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame = QtWidgets.QFrame(dialog_antenns)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setLineWidth(1)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout_11.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(dialog_antenns)
        self.frame_3.setMinimumSize(QtCore.QSize(200, 110))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(dialog_antenns)
        self.frame_4.setMinimumSize(QtCore.QSize(200, 110))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_6.addWidget(self.comboBox_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(dialog_antenns)
        self.frame_5.setMinimumSize(QtCore.QSize(200, 110))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_8.addWidget(self.comboBox_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(dialog_antenns)
        self.frame_6.setMinimumSize(QtCore.QSize(200, 110))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_10.addWidget(self.label_4)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout_10.addWidget(self.comboBox_4)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog_antenns)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(dialog_antenns)
        self.buttonBox.accepted.connect(dialog_antenns.accept)
        self.buttonBox.rejected.connect(dialog_antenns.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_antenns)

    def retranslateUi(self, dialog_antenns):
        _translate = QtCore.QCoreApplication.translate
        dialog_antenns.setWindowTitle(_translate("dialog_antenns", "Настройка Антенн"))
        self.pushButton.setText(_translate("dialog_antenns", "Добавить антенну"))
        self.pushButton_2.setText(_translate("dialog_antenns", "Удалить антенну"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dialog_antenns", "F, МГц"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dialog_antenns", "Ka, дБ"))
        self.pushButton_3.setText(_translate("dialog_antenns", "Сохранить антенну"))
        self.label_5.setText(_translate("dialog_antenns", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; line-height:100%;margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Настройка приемных и передающих <br /> антенн </span></p>"))
        self.label.setText(_translate("dialog_antenns", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; line-height: 50%;\">Приемная антенна <br /> НЧ</span></p>"))
        self.label_2.setText(_translate("dialog_antenns", "<html><head/><body><p><span style=\" font-size:10pt;  line-height: 50%;\">Приемная антенна <br /> ВЧ</span></p>"))
        self.label_3.setText(_translate("dialog_antenns", "<html><head/><body><p><span style=\" font-size:10pt; line-height: 50%;\">Передающая антенна <br /> НЧ</span></p>"))
        self.label_4.setText(_translate("dialog_antenns", "<html><head/><body><p><span style=\" font-size:10pt; line-height: 50%;\">Передающая антенна <br /> ВЧ</span></p>"))

