from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
# TODO: replace ImageOps
from PIL import Image, ImageDraw, ImageOps
from PyQt5.QtWidgets import QFileDialog, QWidget
from matrix_ui import Ui_Form
from coder_ui import Ui_Coder
from functools import wraps


class imgActs(object):

    def open(self):
        # TODO: обработать отмену выбора файла
        filename, _ = QFileDialog.getOpenFileName(self.MainWindow,
                                                  "Open File",
                                                  'images/')
        self.workon = Image.open(filename)
        self.iLabel.setPixmap(self.workon.toqpixmap())
        self.iLabel.adjustSize()

        self.drawHist(self.getHist(self.workon), 0)

    def _print(self):
        self.oLabel.setPixmap(self.crOutput.toqpixmap())
        self.drawHist(self.getHist(self.crOutput), 1)

    def for_each_px(function):
        @wraps(function)
        def wrapper(self, *args, **kwargs):
            self.oLabel.clear()
            self.crOutput = Image.new(self.workon.mode,
                                      self.workon.size)
            draw = ImageDraw.Draw(self.crOutput)
            pix = self.workon.load()
            for i in range(self.workon.width):
                for j in range(self.workon.height):
                    rs = function(self, pix[i, j])
                    draw.point((i, j), (rs, rs, rs))
            self._print()
        return wrapper

    def ddrawHist(self):
        # TODO: сделать вывод гистограммы
        figIn, figOut = Figure(), Figure()
        figIn.set_tight_layout({'pad': 0,})
        figOut.set_tight_layout({'pad': 0,})
        self.axIn = figIn.add_subplot(111)
        self.axOut = figOut.add_subplot(111)
        self.iHist, self.oHist = FigureCanvasQTAgg(figIn), FigureCanvasQTAgg(figOut)
        self.gridLayout.addWidget(self.iHist, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.oHist, 3, 2, 1, 1)

    def drawHist(self, hst, p):
        # TODO: не менять
        ax = self.axIn if p == 0 else self.axOut
        hist = self.iHist if p == 0 else self.oHist
        ax.clear()
        ax.hist(range(256), bins=256, weights=hst, density=1, color='gray')
        ax.set_xmargin(0.01)
        hist.draw()

    def getHist(self, img):
        pix = img.load()
        w, h = img.size
        hist = [0] * 256

        for i in range(w):
            for j in range(h):
                if type(pix[i, j]) != int:
                    r, g, b = pix[i, j]
                    res = (r + g + b) // 3
                else:
                    res = pix[i, j]
                hist[res] += 1
        return hist

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

    def save(self):
        pass

    def _clear(self):
        self.iLabel.clear()
        self.oLabel.clear()
        self.axIn.clear()
        self.iHist.draw()
        self.axOut.clear()
        self.oHist.draw()

    @for_each_px
    def pfAveraging(self, colors):
        return sum(colors) // 3

    @for_each_px
    def pfHumanEye(self, colors):
        return round(.3 * colors[0] + .59 * colors[1] + .11 * colors[2])

    @for_each_px
    def pfDesaturation(self, colors):
        return (max(colors) + min(colors)) // 2

    @for_each_px
    def pfMax(self, colors):
        return max(colors)

    @for_each_px
    def pfMin(self, colors):
        return min(colors)

    def pfEqualization(self):
        cumhist = self.getCumHist(self.workon)
        draw, pix = self.prepare()

        for i in range(self.workon.width):
            for j in range(self.workon.height):
                if type(pix[i, j]) != int:
                    num = sum(pix[i, j]) // 3
                    c = cumhist[num]
                    draw.point((i, j), (c, c, c))
                else:
                    num = 256 - pix[i, j]
                    c = cumhist[num]
                    draw.point((i, j), c)

        self._print()

    def filter(self, x, y, px, draw):
        """Применение фильтра"""
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

    def pfFilter(self):
        """Проход по пикселам внутри рамки"""
        m, n = len(self.mtr), len(self.mtr[0])
        dx, dy = (n - 1) // 2, (m - 1) // 2
        ext_image = Image.new(self.workon.mode,
                              (self.workon.width + (2 * dx),
                               self.workon.height + (2 * dy)))
        ext_image.paste(self.workon, (dx, dy))

        px = ext_image.load()

        self.crOutput = Image.new(self.workon.mode,
                                  self.workon.size)
        draw = ImageDraw.Draw(self.crOutput)

        h = ext_image.height - dy
        w = ext_image.width - dx
        for y in range(dy, h):
            for x in range(dx, w):
                self.filter(x, y, px, draw)

        self._print()

    def pfGauss(self):
        """Фильтр Гаусса"""
        # TODO: задать фильтр для границ
        # TODO: вывести фильтр в таблицу
        pass

    def crtWindow(self):
        # TODO: изменить создание окна
        self.window = QWidget()
        ui = Ui_Form()
        ui.setupUi(self.window)
        self.window.ui = ui

        # TODO: привязать кнопки
        self.window.ui.confirm.clicked.connect(self.cfMatrix)
        self.window.ui.lnHor.editingFinished.connect(self.cfHor)
        self.window.ui.lnVer.editingFinished.connect(self.cfVer)
        self.window.ui.gaussBtn.clicked.connect(self.pfGauss)
        self.window.show()

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

    def crtCoder(self):
        """Окно для кодирования"""
        # TODO: изменить создание окна
        self.window = QWidget()
        ui = Ui_Coder()
        ui.setupUi(self.window)
        self.window.ui = ui


        # TODO: привязать кнопки
        self.window.ui.coderBtn.clicked.connect(self.pfCoder)
        self.window.ui.decoderBtn.clicked.connect(self.pfDecoder)
        self.window.show()

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
            r = round(l + probability, 3)
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

    def cfMatrix(self):
        self.mtr = list()
        obj = self.window.ui
        m, n = obj.mtx.rowCount(), obj.mtx.columnCount()
        for i in range(m):
            for j in range(n):
                self.mtr.append(float(obj.mtx.item(i, j).text()))
        self.crtMatrix(m, n)
        self.window.close()
        self.pfFilter()

    def crtMatrix(self, m, n):
        """Преобразование в матрицу"""
        tmp = []
        for i in range(m):
            tmp.append([])
            for j in range(n):
                tmp[-1].append(self.mtr[j + n * i])
        # преобразовывает правильно
        self.mtr = tmp

    def pfBinarization(self):
        px = ImageOps.grayscale(self.workon).load()
        self.crOutput = Image.new('1', self.workon.size)
        draw = ImageDraw.Draw(self.crOutput)

        for i in range(self.workon.width):
            for j in range(self.workon.height):
                # TODO: задавать порог
                if px[i, j] > 128:
                    draw.point((i, j), 1)
        self._print()

    # TODO: another name
    # TODO: difference between pfFilter and crtMorphology
    def crtMorphology(self):
        pass

    def prepare(self):
        """Исключить, for_each_px"""
        # TODO: исключить
        self.oLabel.clear()
        self.crOutput = Image.new(self.workon.mode,
                                  self.workon.size)
        draw = ImageDraw.Draw(self.crOutput)
        pix = self.workon.load()
        return draw, pix


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
