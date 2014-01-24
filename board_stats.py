

from PyQt4 import QtCore, QtGui

from global_config import GlobalConfig


class BoardStats(QtGui.QFrame):
	
	def __init__(self, parent):
		super(BoardStats, self).__init__(parent)
		
		self.initUI()
	
	
	def initUI(self):
		
		self.setFixedWidth(GlobalConfig.StatsWidgetWidth)
		
		self.vbox = QtGui.QVBoxLayout()
		
		self.setLayout(self.vbox)
