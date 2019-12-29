import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
# TODO: replace ImageOps
from PIL import Image, ImageDraw, ImageOps
from PyQt5.QtWidgets import QFileDialog, QWidget
from matrix_ui import Ui_Form
from matrix_morph_ui import Morph_Ui
from coder_ui import Ui_Coder
from functools import wraps
from time import time


class imgActs(object):

    def __setattr__(self, *args, **kwargs):
        """Проверка на workon или crOutput"""
        tmp = args[1]
        if args[0] == 'workon':
            if tmp.width < 200:
                self.iLabel.setPixmap(tmp.toqpixmap().scaledToWidth(200))
            else:
                self.iLabel.setPixmap(tmp.toqpixmap())
            self.ihst = self.getHist(tmp)
            self.drwHist(self.ihst, 0)
        if args[0] == 'crOutput':
            if tmp.width < 200:
                self.oLabel.setPixmap(tmp.toqpixmap().scaledToWidth(200))
            else:
                self.oLabel.setPixmap(tmp.toqpixmap())
            self.ohst = self.getHist(tmp)
            self.drwHist(self.ohst, 1)
        object.__setattr__(self, *args, **kwargs)

    ####################################################################################################################
    ###########################################  Inner   ###############################################################
    ####################################################################################################################

    def open(self):
        # TODO: обработать отмену выбора файла
        filename, _ = QFileDialog.getOpenFileName(self.MainWindow,
                                                  "Open File",
                                                  "images/")
        self.workon = Image.open(filename)

    def _printIn(self):
        """Вывод исходного изображения"""
        pass

    def _printOut(self):
        """Вывод обработанного изображения"""
        self.oLabel.setPixmap(self.crOutput.toqpixmap())
        self.oLabel.adjustSize()
        self.drwHist(self.getHist(self.crOutput), 1)
        # pass

    def _reuse(self):
        """Передача выходного изображения на вход"""
        self.workon = self.crOutput

    def _save(self):
        pass

    def _clear(self):
        # QLabels
        self.iLabel.clear()
        self.oLabel.clear()
        # Axes
        self.axIn.clear()
        self.axOut.clear()
        # Figures
        self.iFig.draw()
        self.oFig.draw()

    def _prepare(self):
        """Исключить, for_each_px"""
        # TODO: исключить
        self.oLabel.clear()
        self.crOutput = Image.new(self.workon.mode,
                                  self.workon.size)
        draw = ImageDraw.Draw(self.crOutput)
        pix = self.workon.load()
        return draw, pix

    def for_each_px(function):
        @wraps(function)
        def wrapper(self, *args, **kwargs):
            self.oLabel.clear()
            out = Image.new(self.workon.mode,
                            self.workon.size)
            draw = ImageDraw.Draw(out)
            pix = self.workon.load()
            for i in range(self.workon.width):
                for j in range(self.workon.height):
                    rs = function(self, pix[i, j])
                    draw.point((i, j), (rs, rs, rs))
            self.crOutput = out
        return wrapper

    def filling_mtr(function):
        @wraps(function)
        def wrapper(self, *args, **kwargs):
            """Создание структурирующего элемента"""
            self.mtr = list()
            obj = self.window.ui
            m, n = obj.mtx.rowCount(), obj.mtx.columnCount()
            for i in range(m):
                for j in range(n):
                    self.mtr.append(float(obj.mtx.item(i, j).text()))
            self.crtMatrix(m, n)
            self.window.close()
            # function(self, *args, **kwargs)
        return wrapper

    def timer(function):
        @wraps(function)
        def wrapper(self, *args, **kwargs):
            start_time = time()
            function(self, *args, **kwargs)
            print("--- %s: %s seconds ---" % (function.__name__, round((time() - start_time), 3)))
        return wrapper

    ####################################################################################################################
    #######################################  Histogram   ###############################################################
    ####################################################################################################################

    @timer
    def _drwFigs(self):
        # TODO: сделать вывод гистограммы
        figIn, figOut = Figure(), Figure()
        figIn.set_tight_layout({'pad': 0,})
        figOut.set_tight_layout({'pad': 0,})
        self.axIn = figIn.add_subplot(111)
        self.axOut = figOut.add_subplot(111)
        self.iFig, self.oFig = FigureCanvasQTAgg(figIn), FigureCanvasQTAgg(figOut)
        self.gridLayout.addWidget(self.iFig, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.oFig, 3, 2, 1, 1)

    def drwHist(self, hst, p):
        # TODO: не менять
        ax = self.axIn if p == 0 else self.axOut
        hist = self.iFig if p == 0 else self.oFig
        ax.clear()
        ax.hist(range(256), bins=256, weights=hst, density=1, color='gray')
        ax.set_xmargin(0.01)
        hist.draw()

    def getHist(self, img: 'Image') -> 'histogram':
        """Calculate histogram from image"""
        px = img.load()
        w, h = img.size
        hst = [0] * 256

        for i in range(w):
            for j in range(h):
                if type(px[i, j]) != int:
                    r, g, b = px[i, j]
                    res = (r + g + b) // 3
                else:
                    res = px[i, j]
                hst[res] += 1

        return hst

    def getCumHist(self, img):
        hist = self.getHist(img)
        s = self.workon.width * self.workon.height
        hist = [i / s for i in hist]
        cumhist = [0] * 256
        summ = 0
        for i, j in enumerate(hist):
            summ += j
            cumhist[i] = round(summ * 256)
        return cumhist

    ####################################################################################################################
    #########################################  Filters   ###############################################################
    ####################################################################################################################

    @timer
    @for_each_px
    def pfAveraging(self, colors):
        return sum(colors) // 3

    @timer
    @for_each_px
    def pfHumanEye(self, colors):
        return round(.3 * colors[0] + .59 * colors[1] + .11 * colors[2])

    @timer
    @for_each_px
    def pfDesaturation(self, colors):
        return (max(colors) + min(colors)) // 2

    @timer
    @for_each_px
    def pfMax(self, colors):
        return max(colors)

    @timer
    @for_each_px
    def pfMin(self, colors):
        return min(colors)

    ####################################################################################################################
    ##########################################  Create   ###############################################################
    ####################################################################################################################

    def crtWindow(self, ui_class):
        # TODO: изменить создание окна
        self.window = QWidget()
        ui = ui_class()
        ui.setupUi(self.window)
        self.window.ui = ui

    def crtMask(self):
        """Окно для создания маски фильтра"""
        self.crtWindow(Ui_Form)

        # buttons
        self.window.ui.confirm.clicked.connect(self.pfFilter)
        self.window.ui.lnHor.editingFinished.connect(self.cfHor)
        self.window.ui.lnVer.editingFinished.connect(self.cfVer)
        # self.window.ui.gaussBtn.clicked.connect(self.pfGauss)
        self.window.show()

    def crtCoder(self):
        """Окно для кодирования"""
        self.crtWindow(Ui_Coder)

        # buttons
        self.window.ui.coderBtn.clicked.connect(self.pfCoder)
        self.window.ui.decoderBtn.clicked.connect(self.pfDecoder)
        self.window.show()

    # TODO: another name
    # TODO: difference between pfFilter and crtMorphology
    def crtMorphology(self):
        """Окно для задания структурирующего элемента"""
        self.crtWindow(Morph_Ui)

        # buttons
        # self.window.ui.confirm.clicked.connect(partial
        self.window.ui.confirm.clicked.connect(self.pfZero)
        self.window.ui.lnHor.editingFinished.connect(self.cfHor)
        self.window.ui.lnVer.editingFinished.connect(self.cfVer)
        self.window.show()

    def crtMatrix(self, m, n):
        """Преобразование в матрицу"""
        tmp = []
        for i in range(m):
            tmp.append([])
            for j in range(n):
                tmp[-1].append(self.mtr[j + n * i])
        # преобразовывает правильно
        self.mtr = tmp

    ####################################################################################################################
    #########################################  Perform   ###############################################################
    ####################################################################################################################

    def pfEqualization(self):
        cumhist = self.getCumHist(self.workon)
        draw, pix = self._prepare()

        for i in range(self.workon.width):
            for j in range(self.workon.height):
                if type(pix[i, j]) != int:
                    num = sum(pix[i, j]) // 3
                    c = cumhist[num]
                    draw.point((i, j), (c, c, c))
                else:
                    num = pix[i, j]
                    c = cumhist[num]
                    draw.point((i, j), c)
        self._printOut()

    @filling_mtr
    def pfFilter(self, *args, **kwargs):
        """Проход по пикселам внутри рамки"""
        m, n = len(self.mtr), len(self.mtr[0])
        dx, dy = (n - 1) // 2, (m - 1) // 2
        tmp = Image.new(self.workon.mode,
                              (self.workon.width + (2 * dx),
                               self.workon.height + (2 * dy)))
        tmp.paste(self.workon, (dx, dy))

        px = tmp.load()

        out = Image.new(self.workon.mode,
                        self.workon.size)
        draw = ImageDraw.Draw(out)

        h = tmp.height - dy
        w = tmp.width - dx
        for y in range(dy, h):
            for x in range(dx, w):
                self.filter(x, y, px, draw)
        self.crOutput = out

    # TODO: совместить с pfFilter
    # TODO: refactoring
    @timer
    def pfMorphology(self, cs):
        m, n = len(self.mtr), len(self.mtr[0])
        dx, dy = (n - 1) // 2, (m - 1) // 2

        # изображение в рамке
        tmp = Image.new(self.workon.mode,
                        (self.workon.width + (2 * dx),
                         self.workon.height + (2 * dy)))
        tmp.paste(self.workon, (dx, dy))

        # попикселный доступ
        px = tmp.load()

        # выходное изображение
        out = Image.new('1', self.workon.size)

        # поверхность для рисования на выходном изображении
        draw = ImageDraw.Draw(out)

        # сдвиги для правильного прохода
        h = tmp.height - dy
        w = tmp.width - dx
        if cs == 0:
            for y in range(dy, h):
                for x in range(dx, w):
                        self.erode(x, y, px, draw)
            out = out.crop((dx, dy, w, h))  # TODO: WTF
        elif cs == 1:
            out = Image.new('1', tmp.size)
            draw = ImageDraw.Draw(out)
            for y in range(dy, h):  # range(tmp.height):
                for x in range(dx, w):  # range(tmp.width):
                    self.dilate(x, y, px, draw, out)
            out = out.crop((dx, dy, w, h))
        elif cs == 2:
            for y in range(dy, h):  # range(tmp.height):
                for x in range(dx, w):  # range(tmp.width):
                    self.intensity(x, y, 3, .2, px, draw)
        self.crOutput = out

    def pfDilation(self):
        self.pfMorphology(1)

    def pfErosion(self):
        self.pfMorphology(0)

    def pfOpening(self):
        try:
            self.pfErosion()
            self._reuse()
            self.pfDilation()
        except Exception as e:
            print(e)

    def pfClosing(self):
        self.pfDilation()
        self._reuse()
        self.pfErosion()

    # it was Gauss
    @filling_mtr
    def pfZero(self):
        """Пустая функция"""
        pass

    def pfCoder(self):
        """Арифметическое кодирование"""

        # TODO: не перезаписывать словарь, если фраза не изменилась
        # Подготовка
        obj = self.window.ui
        self.dct = dict()
        letters = obj.lnDict.text()
        phrase = obj.lnPhrase.text()
        self.trm = obj.lnTerm.text()
        probability = 1 / (len(letters) + 1)
        l = 0.

        # Собираем словарь символов
        for chr in letters:
            r = l + probability
            self.dct[chr] = cdSmb(l, r)
            l = r

        # Добавляем терминальный символ
        self.dct[self.trm] = cdSmb(l, 1.)

        # Кодирование и вывод
        obj.lnResCode.setText(self.ariphmeticCoding(phrase).__repr__())

    def pfDecoder(self):
        """Арифметическое декодирование"""

        # Подготовка
        obj = self.window.ui
        code = float(obj.lnCode.text())

        # Декодирование и вывод результата
        obj.lnResDecoder.setText(self.ariphmeticDecoding(code))

    def pfSimpleBinarization(self, threshold=128):
        px = ImageOps.grayscale(self.workon).load()
        out = Image.new('1', self.workon.size)
        draw = ImageDraw.Draw(out)

        for i in range(self.workon.width):
            for j in range(self.workon.height):
                # TODO: задавать порог
                if px[i, j] > threshold:
                    draw.point((i, j), 1)
        self.crOutput = out

    def pfNiblack(self):
        self.mtr = [[0 for i in range(3)] for i in range(3)]
        self.pfMorphology(2)

    def pfOtsu(self):
        """Вычисление порога по гистограмме"""
        # нормализация гистограммы
        N = sum(self.ihst)
        hst = [i / N for i in self.ihst]
        # инициализация
        w1 = hst[0]
        w2 = 1 - w1
        mu1 = 0
        mu2 = sum([i * hst[i] for i in range(1, len(hst))])
        var_b, t = 0, 1
        for i in range(1, len(hst)):
            w1 += hst[i]
            w2 -= hst[i]
            mu1 += i * hst[i]
            mu2 -= i * hst[i]
            if w1 != 0 and w2 != 0:
                var_tmp = w1 * w2 * (((mu1 / w1) - (mu2 / w2)) ** 2)
                if var_tmp > var_b:
                    var_b = var_tmp
                    t = i
        self.pfSimpleBinarization(t)

    ####################################################################################################################
    #########################################  Confirm   ###############################################################
    ####################################################################################################################

    def cfHor(self):
        """Ширина матрицы"""
        txt = self.window.ui.lnHor.text()
        if txt != '':
            n = int(txt)
            if n % 2 != 0:
                self.window.ui.mtx.setColumnCount(n)
            else:
                pass

    def cfVer(self):
        """Высота матрицы"""
        txt = self.window.ui.lnVer.text()
        if txt != '':
            m = int(txt)
            if m % 2 != 0:
                self.window.ui.mtx.setRowCount(m)
            else:
                pass

    ####################################################################################################################
    #########################################  Actions   ###############################################################
    ####################################################################################################################

    def filter(self, x, y, px, draw):
        """Фильтр"""
        sr, sg, sb = 0, 0, 0
        m, n = len(self.mtr), len(self.mtr[0])
        dx, dy = (n - 1) // 2, (m - 1) // 2
        # по всему фильтру
        for i in range(m):
            for j in range(n):
                r, g, b = px[x - dx + j, y - dy + i]
                sr += self.mtr[i][j] * r
                sg += self.mtr[i][j] * g
                sb += self.mtr[i][j] * b
        draw.point((x - 1, y - 1), (round(sr), round(sg), round(sb)))

    def dilate(self, x, y, px, draw, out):
        """Дилатация"""
        m, n = len(self.mtr), len(self.mtr[0])
        dx, dy = (n - 1) // 2, (m - 1) // 2
        # TODO: добавить любой символ
        cx, cy = n // 2, m // 2
        if self.mtr[cx][cy] == px[x, y]:
            # rows - y
            for i in range(m):
                # columns - x
                for j in range(n):
                    try:
                        draw.point((x - dx + j, y - dy + i),
                                   int(out.getpixel((x - dx + j, y - dy + i)) or
                                       self.mtr[j][i] or
                                       px[x - dx + j, y - dy + i]))
                    except Exception as err:
                        pass
                        # print(err)
                        # print(x-dx+j, y-dy+i)

    def erode(self, x, y, px, draw):
        """"Эрозия"""
        m, n = len(self.mtr), len(self.mtr[0])  # TODO: remove calculation
        dx, dy = (n - 1) // 2, (m - 1) // 2  # TODO: remove calculation
        # TODO: добавить любой символ
        cx, cy = n // 2, m // 2  # TODO: remove calculation
        flag = True
        # rows - y
        for i in range(m):
            # columns - x
            for j in range(n):
                # condition
                if (self.mtr[i][j] == 1) and (px[x - dx + j, y - dy + i] != self.mtr[i][j]):
                    flag = False
                    break
        if flag: draw.point((x, y), int(self.mtr[cy][cx]))

    def intensity(self, x, y, n, k, px, draw):
        """расчет интенсивности для Ниблэка в точке"""
        dx = (n - 1) // 2
        dy = dx
        ls = []
        for i in range(n):
            for j in range(n):
                ls.append(px[x - dx + j, y - dy + i][0])
        mean = sum(ls) / len(ls)
        std = (sum((xi - mean) ** 2 for xi in ls) / len(ls)) ** (1 / 2)
        I = mean - k * std
        if px[x, y][0] > I:
            draw.point((x, y), 1)

    def ariphmeticCoding(self, msg: str) -> 'cdSmb':
        res = cdSmb(0, 1)
        for i in msg:
            h = res.l + (res.h - res.l) * self.dct[i].h
            l = res.l + (res.h - res.l) * self.dct[i].l
            res.l, res.h = l, h
        return res

    def ariphmeticDecoding(self, code: float) -> str:
        res = ''
        while len(res) == 0 or res[-1] != '!':
            for i in self.dct:
                if self.dct[i].isIn(code):
                    res += i
                    print(i, self.dct[i].l, self.dct[i].h, code)
                    code = (code - self.dct[i].l) / (self.dct[i].h - self.dct[i].l)
        return res


class cdSmb:
    """Интервал для символа на отрезке [0, 1)"""
    def __init__(self, l, h):
        """Инициализация"""
        self.l = l
        self.h = h

    def __repr__(self):
        """Вывод в терминал"""
        return '({0}; {1})'.format(self.l, self.h)

    def isIn(self, cd):
        """Проверка вхождения"""
        if (cd < self.h) and (cd >= self.l):
            return True
        else:
            return False
