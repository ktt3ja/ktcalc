import sys
from decimal import Decimal
from PySide.QtGui import QMainWindow, QApplication
from ui_ktcalc import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self._MAXTEXTLEN = 23 
		self.setupUi(self)
		self.initStartState(initMemory=True)
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