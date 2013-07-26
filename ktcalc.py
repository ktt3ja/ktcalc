import sys
from PySide.QtGui import QMainWindow, QApplication
from ui_ktcalc import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.lineEdit.setText('0')
		self.zeroButton.clicked.connect(lambda: self.append(0))
		self.oneButton.clicked.connect(lambda: self.append(1))
		self.twoButton.clicked.connect(lambda: self.append(2))
		self.threeButton.clicked.connect(lambda: self.append(3))
		self.fourButton.clicked.connect(lambda: self.append(4))
		self.fiveButton.clicked.connect(lambda: self.append(5))
		self.sixButton.clicked.connect(lambda: self.append(6))
		self.sevenButton.clicked.connect(lambda: self.append(7))
		self.eightButton.clicked.connect(lambda: self.append(8))
		self.nineButton.clicked.connect(lambda: self.append(9))

	def append(self, number):
		self.lineEdit.setText(self.lineEdit.text().lstrip('0') + unicode(number))

if __name__== '__main__':
	app = QApplication(sys.argv)
	frame = MainWindow()
	frame.show()
	app.exec_()