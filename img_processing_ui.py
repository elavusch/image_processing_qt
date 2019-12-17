# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from img_actions import imgActs


class Ui_imgProcUI(imgActs, object):
    def setupUi(self, imgProcUI):
        self.MainWindow = imgProcUI  # Для QFileDialog
        imgProcUI.setObjectName("imgProcUI")
        imgProcUI.resize(1500, 852)

        # imgProcUI size
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        (sizePolicy.setHeightForWidth(
            imgProcUI.sizePolicy().hasHeightForWidth()))

        imgProcUI.setSizePolicy(sizePolicy)
        imgProcUI.setMinimumSize(QtCore.QSize(1500, 852))
        # imgProcUI.setMaximumSize(QtCore.QSize(1500, 852))
        self.centralwidget = QtWidgets.QWidget(imgProcUI)

        # centralwidget size: was .Maximum
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        (sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()))

        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        # TODO: попробовать поставить переменные
        self.gridLayoutWidget.setGeometry(QtCore.QRect(7, 7, 1490, 792))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 16)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 16)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollAreaIn = QtWidgets.QScrollArea(self.gridLayoutWidget)
        self.scrollAreaIn.setWidgetResizable(True)
        self.scrollAreaIn.setObjectName("scrollAreaIn")

        self.iLabel = QtWidgets.QLabel()
        self.iLabel.setGeometry(QtCore.QRect(0, 0, 391, 731))

        # iLabel size
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                           QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        (sizePolicy.setHeightForWidth(
            self.iLabel.sizePolicy().hasHeightForWidth()))

        self.iLabel.setSizePolicy(sizePolicy)
        self.iLabel.setAutoFillBackground(True)
        self.iLabel.setText("")
        self.iLabel.setAlignment(QtCore.Qt.AlignLeading |
                                 QtCore.Qt.AlignLeft |
                                 QtCore.Qt.AlignTop)
        self.iLabel.setObjectName("iLabel")
        self.scrollAreaIn.setWidget(self.iLabel)

        self.gridLayout.addWidget(self.scrollAreaIn, 1, 0, 3, 1)
        self.label3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 0, 2, 1, 1)
        self.label2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 0, 1, 1, 1)
        self.label1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)
        self.clBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clBtn.setObjectName("clBtn")
        self.clBtn.clicked.connect(self._clear)
        self.gridLayout.addWidget(self.clBtn, 4, 2, 1, 1)
        self.useBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.useBtn.setObjectName("useBtn")
        # TODO: connect button
        # self.useBtn.clicked.connect(self._clear)
        self.gridLayout.addWidget(self.useBtn, 4, 1, 1, 1)
        self.label4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label4.setObjectName("label4")
        self.gridLayout.addWidget(self.label4, 2, 2, 1, 1)
        self.scrollAreaOut = QtWidgets.QScrollArea(self.gridLayoutWidget)
        self.scrollAreaOut.setWidgetResizable(True)
        self.scrollAreaOut.setObjectName("scrollAreaOut")

        self.oLabel = QtWidgets.QLabel()
        self.oLabel.setGeometry(QtCore.QRect(0, 0, 391, 731))

        # oLabel size
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                           QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        (sizePolicy.setHeightForWidth(
            self.oLabel.sizePolicy().hasHeightForWidth()))

        self.oLabel.setSizePolicy(sizePolicy)
        self.oLabel.setAutoFillBackground(True)
        self.oLabel.setText("")
        self.oLabel.setAlignment(QtCore.Qt.AlignLeading |
                                 QtCore.Qt.AlignLeft |
                                 QtCore.Qt.AlignTop)
        self.oLabel.setObjectName("oLabel")
        self.scrollAreaOut.setWidget(self.oLabel)

        self.gridLayout.addWidget(self.scrollAreaOut, 1, 1, 3, 1)
        imgProcUI.setCentralWidget(self.centralwidget)

        # Создание меню
        self.menubar = QtWidgets.QMenuBar(imgProcUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1222, 26))
        self.menubar.setObjectName("menubar")
        self.mnFile = QtWidgets.QMenu(self.menubar)
        self.mnFile.setObjectName("mnFile")
        self.mnBW = QtWidgets.QMenu(self.menubar)
        self.mnBW.setObjectName("mnBW")
        self.mnHist = QtWidgets.QMenu(self.menubar)
        self.mnHist.setObjectName("mnHist")
        self.mnFilter = QtWidgets.QMenu(self.menubar)
        self.mnFilter.setObjectName("mnFilter")
        self.mnCoder = QtWidgets.QMenu(self.menubar)
        self.mnCoder.setObjectName("mnCoder")
        self.mnBinarization = QtWidgets.QMenu(self.menubar)
        self.mnBinarization.setObjectName("mnBinarization")
        self.mnMorphology = QtWidgets.QMenu(self.menubar)
        self.mnMorphology.setObjectName("mnMorphology")
        imgProcUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(imgProcUI)
        self.statusbar.setObjectName("statusbar")
        imgProcUI.setStatusBar(self.statusbar)

        self.actOpen = QtWidgets.QAction(imgProcUI,
                                         triggered=self.open)
        self.actOpen.setObjectName("actOpen")
        self.actSave = QtWidgets.QAction(imgProcUI,
                                         triggered=self._save)
        self.actSave.setObjectName("actSave")
        self.actAveraging = QtWidgets.QAction(imgProcUI,
                                              triggered=self.pfAveraging)
        self.actAveraging.setObjectName("actAveraging")
        self.actHumanEye = QtWidgets.QAction(imgProcUI,
                                             triggered=self.pfHumanEye)
        self.actHumanEye.setObjectName("actHumanEye")
        self.actDesaturation = QtWidgets.QAction(imgProcUI,
                                                 triggered=self.pfDesaturation)
        self.actDesaturation.setObjectName("actDesaturation")
        self.actMax = QtWidgets.QAction(imgProcUI,
                                        triggered=self.pfMax)
        self.actMax.setObjectName("actMax")
        self.actMin = QtWidgets.QAction(imgProcUI,
                                        triggered=self.pfMin)
        self.actMin.setObjectName("actMin")
        self.actEqualization = QtWidgets.QAction(imgProcUI,
                                                 triggered=self.pfEqualization)
        self.actEqualization.setObjectName("actEqualization")
        self.actCrFilter = QtWidgets.QAction(imgProcUI,
                                             triggered=self.crtWindow)
        self.actCrFilter.setObjectName("actCrFilter")
        self.actCoder = QtWidgets.QAction(imgProcUI,
                                          triggered=self.crtCoder)
        self.actCoder.setObjectName("actCoder")
        # New
        self.actBinarization = QtWidgets.QAction(imgProcUI,
                                                 triggered=self.pfBinarization)
        self.actBinarization.setObjectName("actBinarization")
        self.actMorphology = QtWidgets.QAction(imgProcUI,
                                               triggered=self.crtMorphology)  # TODO: another name
        self.actMorphology.setObjectName("actMorphology")
        self.mnFile.addAction(self.actOpen)
        self.mnFile.addAction(self.actSave)
        self.mnBW.addAction(self.actAveraging)
        self.mnBW.addAction(self.actHumanEye)
        self.mnBW.addAction(self.actDesaturation)
        self.mnBW.addAction(self.actMax)
        self.mnBW.addAction(self.actMin)
        self.mnHist.addAction(self.actEqualization)
        self.mnFilter.addAction(self.actCrFilter)
        self.mnCoder.addAction(self.actCoder)
        self.mnBinarization.addAction(self.actBinarization)
        self.mnMorphology.addAction(self.actMorphology)
        self.menubar.addAction(self.mnFile.menuAction())
        self.menubar.addAction(self.mnBW.menuAction())
        self.menubar.addAction(self.mnHist.menuAction())
        self.menubar.addAction(self.mnFilter.menuAction())
        self.menubar.addAction(self.mnCoder.menuAction())
        self.menubar.addAction(self.mnBinarization.menuAction())
        self.menubar.addAction(self.mnMorphology.menuAction())

        self.retranslateUi(imgProcUI)
        QtCore.QMetaObject.connectSlotsByName(imgProcUI)

        # TODO: убрать позорище
        self.count = 0
        self.ddrawHist()
        self.MainWindow.resizeEvent = self.resizeEvent

    def retranslateUi(self, imgProcUI):
        _translate = QtCore.QCoreApplication.translate
        imgProcUI.setWindowTitle(_translate("imgProcUI",
                                            "Обработка изображений"))
        self.label3.setText(_translate("imgProcUI",
                                       "Гистограмма исходного изображения:"))
        self.label2.setText(_translate("imgProcUI", "Обработанное:"))
        self.label1.setText(_translate("imgProcUI", "Исходное:"))
        self.clBtn.setText(_translate("imgProcUI", "Очистить"))
        self.useBtn.setText(_translate("imgProcUI", "Использовать обработанное изображение"))
        (self.label4.setText(_translate(
            "imgProcUI", "Гистограмма обработанного изображения:")))
        self.mnFile.setTitle(_translate("imgProcUI", "Файл"))
        self.mnBW.setTitle(_translate("imgProcUI", "Ч/Б"))
        self.mnHist.setTitle(_translate("imgProcUI", "Гистограмма"))
        self.mnFilter.setTitle(_translate("imgProcUI", "Фильтры"))
        self.mnCoder.setTitle(_translate("imgProcUI", "Кодирование"))
        self.mnBinarization.setTitle(_translate("imgProcUI", "Бинаризация"))
        self.mnMorphology.setTitle(_translate("imgProcUI", "Морфология"))

        self.actOpen.setText(_translate("imgProcUI", "Открыть"))
        self.actOpen.setShortcut(_translate("imgProcUI", "Ctrl+O"))
        self.actSave.setText(_translate("imgProcUI", "Сохранить"))
        self.actSave.setShortcut(_translate("imgProcUI", "Ctrl+S"))
        self.actAveraging.setText(_translate("imgProcUI", "Усреднение"))
        self.actHumanEye.setText(_translate("imgProcUI",
                                            "Коррекция под чел. глаз"))
        self.actDesaturation.setText(_translate("imgProcUI", "Десатурация"))
        self.actMax.setText(_translate("imgProcUI", "Градация по максимуму"))
        self.actMin.setText(_translate("imgProcUI", "Градация по минимуму"))
        self.actEqualization.setText(_translate("imgProcUI", "Эквализация"))
        self.actCrFilter.setText(_translate("imgProcUI", "Задать фильтр"))
        self.actCoder.setText(_translate("imgProcUI", "Арифметическое кодирование"))
        self.actBinarization.setText(_translate("imgProcUI", "Пороговая"))
        self.actMorphology.setText(_translate("imgProcUI", "Задать стр. элемент"))

    def resizeEvent(self, *args, **kwargs):
        s = self.MainWindow.size()
        self.gridLayoutWidget.setGeometry(QtCore.QRect(7, 7, s.width() - 10, s.height() - 60))
        QtWidgets.QWidget.resizeEvent(self.MainWindow, *args, **kwargs)


def test_image_out(window):
    img = QtGui.QImage('images/lenna.png')
    window.iLabel.setPixmap(QtGui.QPixmap.fromImage(img))
    window.iLabel.adjustSize()


def test_2images_out(window):
    img = QtGui.QImage('images/lenna.png')
    window.oLabel.setPixmap(QtGui.QPixmap.fromImage(img))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_imgProcUI()
    ui.setupUi(window)

    # Тесты:
    # test_image_out(ui)
    # test_2images_out(ui)
    ########

    window.show()
    sys.exit(app.exec_())
