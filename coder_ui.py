# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coder_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Coder(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(702, 402)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 701, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label1.setObjectName("label1")
        self.verticalLayout.addWidget(self.label1)
        self.lnDict = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lnDict.setObjectName("lnDict")
        self.verticalLayout.addWidget(self.lnDict)
        self.label2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label2.setObjectName("label2")
        self.verticalLayout.addWidget(self.label2)
        self.lnTerm = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lnTerm.setObjectName("lnTerm")
        self.verticalLayout.addWidget(self.lnTerm)
        self.label3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label3.setObjectName("label3")
        self.verticalLayout.addWidget(self.label3)
        self.lnPhrase = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lnPhrase.setObjectName("lnPhrase")
        self.verticalLayout.addWidget(self.lnPhrase)
        self.label4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label4.setObjectName("label4")
        self.verticalLayout.addWidget(self.label4)
        self.lnResCode = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lnResCode.setObjectName("lnResCode")
        self.verticalLayout.addWidget(self.lnResCode)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label5.setObjectName("label5")
        self.verticalLayout.addWidget(self.label5)
        self.lnCode = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lnCode.setObjectName("lnCode")
        self.verticalLayout.addWidget(self.lnCode)
        self.label6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label6.setObjectName("label6")
        self.verticalLayout.addWidget(self.label6)
        self.lnResDecoder = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lnResDecoder.setObjectName("lnResDecoder")
        self.verticalLayout.addWidget(self.lnResDecoder)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.coderBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.coderBtn.setObjectName("coderBtn")
        self.horizontalLayout.addWidget(self.coderBtn)
        self.decoderBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.coderBtn.setObjectName("coderBtn")
        self.decoderBtn.setObjectName("decoderBtn")
        self.horizontalLayout.addWidget(self.decoderBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Арифметическое кодирование"))
        self.label1.setText(_translate("Form", "Словарь символов:"))
        self.label2.setText(_translate("Form", "Терминирующий символ:"))
        self.label3.setText(_translate("Form", "Фраза для кодирования:"))
        self.label4.setText(_translate("Form", "Результат кодировки:"))
        self.label5.setText(_translate("Form", "Последовательность для декодирования:"))
        self.label6.setText(_translate("Form", "Результат декодирования:"))
        self.coderBtn.setText(_translate("Form", "Закодировать"))
        self.decoderBtn.setText(_translate("Form", "Декодировать"))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_Coder()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())