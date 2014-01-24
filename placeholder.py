
from PyQt4 import QtCore, QtGui

from board import Board


class Placeholder(QtGui.QWidget):

	RightWidgetWidth = 175

	def __init__(self, parent):
		super(Placeholder, self).__init__(parent)
		
		self.initPlaceholder()
	
	
	def initPlaceholder(self):
		
		self.board = Board(self)
		
		self.hbox = QtGui.QHBoxLayout()
		
		self.vbox = QtGui.QVBoxLayout()
		
		self.hbox.addWidget(self.board)
		
		widgets = self.board.getStatsWidgets()
		
		for widget in widgets:
			self.vbox.addWidget(widget)
		
		self.vbox.addStretch(1)
		
		self.hbox.addLayout(self.vbox)
		
		self.setLayout(self.hbox)

	
	def setStatsWidgets(self, widgets):
		print('placeholder.Placeholder.setStatsWidgets')
		pass
