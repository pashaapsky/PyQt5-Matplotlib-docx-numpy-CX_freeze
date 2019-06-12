
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog_options(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog.resize(543, 353)
        dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        dialog.setModal(False)
        self.gridLayout_3 = QtWidgets.QGridLayout(dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalFrame_4 = QtWidgets.QFrame(dialog)
        self.verticalFrame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verticalFrame_4.setObjectName("verticalFrame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalFrame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.verticalFrame_4)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout.addWidget(self.doubleSpinBox_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalFrame_4)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.verticalFrame_4, 0, 1, 2, 1)
        self.verticalFrame_5 = QtWidgets.QFrame(dialog)
        self.verticalFrame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verticalFrame_5.setObjectName("verticalFrame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.verticalFrame_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.verticalFrame_5)
        self.label_6.setStatusTip("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.verticalFrame_5)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout_2.addWidget(self.doubleSpinBox_5, 2, 0, 1, 1)
        self.horizontalFrame = QtWidgets.QFrame(self.verticalFrame_5)
        self.horizontalFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.horizontalFrame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.gridLayout_2.addWidget(self.horizontalFrame, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.verticalFrame_5)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 4, 0, 1, 1)
        self.gridLayout_3.addWidget(self.verticalFrame_5, 2, 1, 2, 1)
        self.verticalFrame_2 = QtWidgets.QFrame(dialog)
        self.verticalFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalFrame_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.verticalFrame_2)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.verticalLayout_2.addWidget(self.doubleSpinBox_2)
        self.gridLayout_3.addWidget(self.verticalFrame_2, 1, 0, 2, 1)
        self.verticalFrame_3 = QtWidgets.QFrame(dialog)
        self.verticalFrame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verticalFrame_3.setObjectName("verticalFrame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalFrame_3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.verticalFrame_3)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.verticalLayout_3.addWidget(self.doubleSpinBox_3)
        self.gridLayout_3.addWidget(self.verticalFrame_3, 0, 0, 1, 1)
        self.verticalFrame = QtWidgets.QFrame(dialog)
        self.verticalFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.verticalFrame)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout.addWidget(self.doubleSpinBox)
        self.gridLayout_3.addWidget(self.verticalFrame, 3, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 4, 1, 1, 1)
        self.verticalFrame_4.raise_()
        self.verticalFrame_5.raise_()
        self.verticalFrame.raise_()
        self.verticalFrame_2.raise_()
        self.verticalFrame_3.raise_()
        self.buttonBox.raise_()

        self.retranslateUi(dialog)
        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Настройка переменных"))
        self.label_5.setText(_translate("dialog", "Уровень мощности сигнала \n"
"на выходе генератора ВЧ Pгвч АР-Р (f) \n"
"для стационарных, дБ(Вт)"))
        self.label_6.setText(_translate("dialog", "Уровень мощности сигнала \n"
"на выходе генератора ВЧ Pгвч АР-Р (f) \n"
"для портативно-возимых, дБ(Вт)"))
        self.label_4.setText(_translate("dialog", "Выбрать тип ВП"))
        self.comboBox.setItemText(0, _translate("dialog", "ВП с СЗУ"))
        self.comboBox.setItemText(1, _translate("dialog", "ВП без СЗУ"))
        self.pushButton.setText(_translate("dialog", "Вернуться к настройкам по умолчанию"))
        self.label_2.setText(_translate("dialog", "Дальность приема \n"
"приемной антенны Rprm, [м]"))
        self.label_3.setText(_translate("dialog", "Усилитель Gym, [дб] "))
        self.label.setText(_translate("dialog", "Дальность облучения \n"
"передающей антенны Rprd, [м]"))
