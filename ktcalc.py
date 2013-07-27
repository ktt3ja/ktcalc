import sys
from decimal import Decimal
from PySide.QtGui import QMainWindow, QApplication
from ui_ktcalc import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.initStartState()
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
		self.clearEntryButton.clicked.connect(lambda: self.lineEdit.setText('0'))

	def doPendingBinOp(self):
		num = Decimal(self.lineEdit.text())
		if not self._binOperator:
			self._storedOperand = Decimal(self.lineEdit.text())
		elif self._binOperator == '+':
			self._storedOperand += num
		elif self._binOperator == '-':
			self._storedOperand -= num
		elif self._binOperator == '*':
			self._storedOperand *= num
		elif self._binOperator == '/':
			self._storedOperand /= num
		return self._storedOperand

	def enterBinOp(self, operator):
		if self._state != 'compute':
			try:
				result = self.doPendingBinOp()
				self.lineEdit.setText(unicode(result))
				self._state = 'compute'
			except:
				self.lineEdit.setText('Error')
				self._state = 'error'
		self._binOperator = operator

	def enterDigit(self, digit):
		if self._state == 'start' or self._state == 'compute':
			if digit != '0':
				self.lineEdit.clear()
				self.lineEdit.setText(self.lineEdit.text() + unicode(digit))
				self._state = 'accum'
			if digit == '.':
				self._state = 'point'
		elif self._state == 'accum':
			self.lineEdit.setText(self.lineEdit.text() + unicode(digit))
			if digit == '.':
				self._state = 'point'
		elif self._state == 'point':
			if digit != '.':
				self.lineEdit.setText(self.lineEdit.text() + unicode(digit))

	def enterEqual(self):
		if self._state == 'accum' or self._state == 'point':
			try:
				result = self.doPendingBinOp()
				self.lineEdit.setText(unicode(result))
				self._state = 'start'
			except:
				self.lineEdit.setText('Error')
				self._state = 'error'
			self._binOperator = None

	def initStartState(self):
		self.lineEdit.setText('0')
		self._state = 'start'
		self._storedOperand = Decimal(0)
		self._binOperator = None

if __name__== '__main__':
	app = QApplication(sys.argv)
	frame = MainWindow()
	frame.show()
	app.exec_()