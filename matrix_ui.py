# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matrix_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(535, 480)
        Form.setMinimumSize(QtCore.QSize(535, 480))
        Form.setMaximumSize(QtCore.QSize(535, 480))
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(2, 0, 531, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 2, 1, 1)
        self.lnHor = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lnHor.setObjectName("lnHor")
        self.gridLayout.addWidget(self.lnHor, 1, 2, 1, 1)
        self.label2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 2, 2, 1, 1)
        self.confirm = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.confirm.setObjectName("confirm")
        self.gridLayout.addWidget(self.confirm, 6, 2, 1, 1)
        self.fltr2Btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.fltr2Btn.setObjectName("fltr2Btn")
        self.gridLayout.addWidget(self.fltr2Btn, 6, 1, 1, 1)
        self.lnVer = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lnVer.setObjectName("lnVer")
        self.gridLayout.addWidget(self.lnVer, 3, 2, 1, 1)
        self.gaussBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.gaussBtn.setObjectName("gaussBtn")
        self.gridLayout.addWidget(self.gaussBtn, 6, 0, 1, 1)
        self.fltr4Btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.fltr4Btn.setObjectName("fltr4Btn")
        self.gridLayout.addWidget(self.fltr4Btn, 7, 1, 1, 1)
        self.fltr3Btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.fltr3Btn.setObjectName("fltr3Btn")
        self.gridLayout.addWidget(self.fltr3Btn, 7, 0, 1, 1)
        self.label3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 5, 0, 1, 2)
        spacerItem = (QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding))
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        self.mtx = QtWidgets.QTableWidget(self.gridLayoutWidget)
        (self.mtx.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents))
        self.mtx.setRowCount(3)
        self.mtx.setColumnCount(3)
        self.mtx.setObjectName("mtx")
        self.mtx.horizontalHeader().setVisible(False)
        self.mtx.horizontalHeader().setDefaultSectionSize(80)
        self.mtx.horizontalHeader().setHighlightSections(False)
        self.mtx.horizontalHeader().setMinimumSectionSize(30)
        self.mtx.verticalHeader().setVisible(False)
        self.mtx.verticalHeader().setDefaultSectionSize(60)
        self.mtx.verticalHeader().setHighlightSections(False)
        self.gridLayout.addWidget(self.mtx, 0, 0, 5, 2)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 15)
        self.gridLayout.setRowStretch(5, 1)
        self.gridLayout.setRowStretch(6, 2)
        self.gridLayout.setRowStretch(7, 2)

        # self.confirm.clicked.connect(self.cfMatrix)
        # self.lnHor.editingFinished.connect(self.cfHor)
        # self.lnVer.editingFinished.connect(self.cfVer)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Настройка маски"))
        self.label1.setText(_translate("Form", "По горизонтали:"))
        self.label2.setText(_translate("Form", "По вертикали:"))
        self.confirm.setText(_translate("Form", "Применить"))
        self.fltr2Btn.setText(_translate("Form", "Фильтр2"))
        self.gaussBtn.setText(_translate("Form", "Гаусс"))
        self.fltr4Btn.setText(_translate("Form", "Фильтр4"))
        self.fltr3Btn.setText(_translate("Form", "Фильтр3"))
        self.label3.setText(_translate("Form", "Готовые:"))

    def cfMatrix(self):
        """Создание матрицы"""
        ls = []
        for i in range(self.mtx.rowCount()):
            for j in range(self.mtx.columnCount()):
                ls.append(self.mtx.item(i, j).text())
        print(ls)

    def cfHor(self):
        """Ширина матрицы"""
        txt = self.lnHor.text()
        if txt != '':
            self.n = int(txt)
            if self.n % 2 != 0:
                self.mtx.setColumnCount(self.n)
            else:
                pass

    def cfVer(self):
        """Высота матрицы"""
        txt = self.lnVer.text()
        if txt != '':
            self.m = int(txt)
            if self.m % 2 != 0:
                self.mtx.setRowCount(self.m)
            else:
                pass

    def resize_table(self):
        """Перестраивает матрицу"""
        pass


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
