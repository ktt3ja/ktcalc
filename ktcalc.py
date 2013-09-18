import sys
from decimal import Decimal
from PySide.QtGui import QMainWindow, QApplication, QShortcut, QAction, QMessageBox
from ui_ktcalc import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self._MAXTEXTLEN = 23 
        self.setupUi(self)
        self.initStartState(initMemory=True)
        self.zeroShortcut = QShortcut('0', self.centralwidget)
        self.oneShortcut = QShortcut('1', self.centralwidget)
        self.twoShortcut = QShortcut('2', self.centralwidget)
        self.threeShortcut = QShortcut('3', self.centralwidget)
        self.fourShortcut = QShortcut('4', self.centralwidget)
        self.fiveShortcut = QShortcut('5', self.centralwidget)
        self.sixShortcut = QShortcut('6', self.centralwidget)
        self.sevenShortcut = QShortcut('7', self.centralwidget)
        self.eightShortcut = QShortcut('8', self.centralwidget)
        self.nineShortcut = QShortcut('9', self.centralwidget)
        self.dotShortcut = QShortcut('.', self.centralwidget)
        self.addShortcut = QShortcut('+', self.centralwidget)
        self.minusShortcut = QShortcut('-', self.centralwidget)
        self.multiplyShortcut = QShortcut('*', self.centralwidget)
        self.divideShortcut = QShortcut('/', self.centralwidget)
        self.equalShortcut1 = QShortcut('Enter', self.centralwidget)
        self.equalShortcut2 = QShortcut('Return', self.centralwidget)
        self.clearShortcut = QShortcut('Alt+C', self.centralwidget)
        self.clearEntryShortcut = QShortcut('C', self.centralwidget)
        self.signShortcut = QShortcut('~', self.centralwidget)
        self.inverseShortcut = QShortcut('I', self.centralwidget)
        self.sqrtShortcut = QShortcut('S', self.centralwidget)
        self.mrShortcut = QShortcut('Ctrl+R', self.centralwidget)
        self.mcShortcut = QShortcut('Ctrl+C', self.centralwidget)
        self.mpShortcut = QShortcut('Ctrl++', self.centralwidget)
        self.mmShortcut = QShortcut('Ctrl+-', self.centralwidget)
        self.zeroShortcut.activated.connect(lambda:self.enterDigit('0'))
        self.oneShortcut.activated.connect(lambda: self.enterDigit('1'))
        self.twoShortcut.activated.connect(lambda: self.enterDigit('2'))
        self.threeShortcut.activated.connect(lambda: self.enterDigit('3'))
        self.fourShortcut.activated.connect(lambda: self.enterDigit('4'))
        self.fiveShortcut.activated.connect(lambda: self.enterDigit('5'))
        self.sixShortcut.activated.connect(lambda: self.enterDigit('6'))
        self.sevenShortcut.activated.connect(lambda: self.enterDigit('7'))
        self.eightShortcut.activated.connect(lambda: self.enterDigit('8'))
        self.nineShortcut.activated.connect(lambda: self.enterDigit('9'))
        self.dotShortcut.activated.connect(lambda: self.enterDigit('.'))
        self.addShortcut.activated.connect(lambda: self.enterBinOp(operator='+'))
        self.minusShortcut.activated.connect(lambda: self.enterBinOp(operator='-'))
        self.multiplyShortcut.activated.connect(lambda: self.enterBinOp(operator='*'))
        self.divideShortcut.activated.connect(lambda: self.enterBinOp(operator='/'))
        self.equalShortcut1.activated.connect(self.enterEqual)
        self.equalShortcut2.activated.connect(self.enterEqual)
        self.clearShortcut.activated.connect(self.initStartState)
        self.clearEntryShortcut.activated.connect(self.enterClearEntry)
        self.signShortcut.activated.connect(self.enterSigned)
        self.inverseShortcut.activated.connect(self.enterInverse)
        self.sqrtShortcut.activated.connect(self.enterSqrt)
        self.mrShortcut.activated.connect(self.enterMR)
        self.mcShortcut.activated.connect(self.enterMC)
        self.mpShortcut.activated.connect(self.enterMP)
        self.mmShortcut.activated.connect(lambda: self.enterMP(plus=False))
        self.zeroButton.clicked.connect(lambda: self.enterDigit('0'))
        self.oneButton.clicked.connect(lambda: self.enterDigit('1'))
        self.twoButton.clicked.connect(lambda: self.enterDigit('2'))
        self.threeButton.clicked.connect(lambda: self.enterDigit('3'))
        self.fourButton.clicked.connect(lambda: self.enterDigit('4'))
        self.fiveButton.clicked.connect(lambda: self.enterDigit('5'))
        self.sixButton.clicked.connect(lambda: self.enterDigit('6'))
        self.sevenButton.clicked.connect(lambda: self.enterDigit('7'))
        self.eightButton.clicked.connect(lambda: self.enterDigit('8'))
        self.nineButton.clicked.connect(lambda: self.enterDigit('9'))
        self.dotButton.clicked.connect(lambda: self.enterDigit('.'))
        self.addButton.clicked.connect(lambda: self.enterBinOp(operator='+'))
        self.minusButton.clicked.connect(lambda: self.enterBinOp(operator='-'))
        self.multiplyButton.clicked.connect(lambda: self.enterBinOp(operator='*'))
        self.divideButton.clicked.connect(lambda: self.enterBinOp(operator='/'))
        self.equalButton.clicked.connect(self.enterEqual)
        self.clearButton.clicked.connect(self.initStartState)
        self.clearEntryButton.clicked.connect(self.enterClearEntry)
        self.signButton.clicked.connect(self.enterSigned)
        self.inverseButton.clicked.connect(self.enterInverse)
        self.sqrtButton.clicked.connect(self.enterSqrt)
        self.mrButton.clicked.connect(self.enterMR)
        self.mcButton.clicked.connect(self.enterMC)
        self.mpButton.clicked.connect(self.enterMP)
        self.mmButton.clicked.connect(lambda: self.enterMP(plus=False))
        self.fileMenu.addAction(QAction("About", self, triggered=self.about))

    def about(self):
        QMessageBox.about(self, "Calculator", "It's a calculator")

    def displayText(self, text):
        self.lineEdit.setText(unicode(text)[:23])

    def doBinOp(self, operator, num1, num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2

    def doPendingBinOp(self):
        num = Decimal(self.lineEdit.text())
        if not self._binOperator:
            self._storedOperand = num
        else:
            self._storedOperand = self.doBinOp(self._binOperator, self._storedOperand, num)
        return self._storedOperand

    def setLastOp(self):
        num = Decimal(self.lineEdit.text())
        operator = self._binOperator
        self._lastOp = lambda x: self.doBinOp(operator, x, num)

    def doLastOp(self):
        if self._lastOp:
            num = Decimal(self.lineEdit.text())
            self._storedOperand = self._lastOp(num)
            self.displayText(self._storedOperand)

    def handleError(self):
        self.displayText('Error')
        self._state = 'error'

    def enterBinOp(self, operator):
        if self._state != 'compute':
            try:
                result = self.doPendingBinOp()
            except:
                self.handleError()
            else:
                self.displayText(result)
                self._state = 'compute'
        self._binOperator = operator

    def enterDigit(self, digit):
        if self._state == 'start' or self._state == 'compute' or self._state == 'memory':
            if digit != '0':
                self.lineEdit.clear()
                if digit == '.':
                    self._state = 'point'
                    self.displayText('0.')
                else:
                    self._state = 'accum'
                    self.displayText(digit)
        elif self._state == 'accum':
            self.displayText(self.lineEdit.text() + unicode(digit))
            if digit == '.':
                self._state = 'point'
        elif self._state == 'point':
            if digit != '.':
                self.displayText(self.lineEdit.text() + unicode(digit))

    def enterEqual(self):
        if self._state == 'accum' or self._state == 'point' or self._state == 'memory':
            try:
                result = self.doPendingBinOp()
            except:
                self.handleError()
            else:
                self.setLastOp()
                self.displayText(result)
                self._state = 'start'
                self._binOperator = None
        elif self._state == 'start':
            try:
                self.doLastOp()
            except:
                self.handleError()

    def initStartState(self, initMemory=False):
        self.lineEdit.setText('0')
        self._state = 'start'
        self._storedOperand = Decimal(0)
        self._binOperator = None
        self._lastOp = None
        if initMemory:
            self._memory = Decimal(0)

    def enterClearEntry(self):
        if self._state != 'error':
            self.lineEdit.setText('0')
            self._state = 'start'

    def enterSigned(self):
        num = Decimal(self.lineEdit.text())
        num = num if num == 0 else num * -1
        self.displayText(num)

    def enterInverse(self):
        num = Decimal(self.lineEdit.text())
        try:
            num = 1 / num
        except:
            self.handleError()
        else:
            self.displayText(num)

    def enterSqrt(self):
        num = Decimal(self.lineEdit.text()).sqrt()
        self.displayText(num)

    def enterMR(self):
        self.displayText(self._memory)
        self._state = 'memory'

    def enterMC(self):
        self._memory = Decimal(0)

    def enterMP(self, plus=True):
        try:
            num = Decimal(self.lineEdit.text())
        except:
            self.handleError()
        else:
            self._state = 'memory'
            self._memory = self._memory + num if plus else self._memory - num

if __name__== '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()