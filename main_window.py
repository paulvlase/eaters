
from PyQt4 import QtCore, QtGui

class MainWindow(QtGui.QFrame):

	def __init__(self, parent):
		super(MainWindow, self).__init__(parent)
	
		self.parent = parent
		
		self.initWindow()
	
	
	def initWindow(self):
		
		self.lbl1 = QtGui.QLabel('Eaters')
		
		self.bt1 = QtGui.QPushButton('Run')
		self.bt1.clicked.connect(self.parent.runEaters)
		
		
		self.bt2 = QtGui.QPushButton('Exit')
		self.bt2.clicked.connect(self.parent.exitEaters)
		
		vbox = QtGui.QVBoxLayout()
		self.setLayout(vbox)
		vbox.addWidget(self.lbl1)
		vbox.addWidget(self.bt1)
		vbox.addWidget(self.bt2)
