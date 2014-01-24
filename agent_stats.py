
import math
from PyQt4 import QtCore, QtGui


class AgentStats(QtGui.QWidget):

	def __init__(self, robot):
		super(RobotStatsWidget, self).__init__(None)
		
		self.robot = robot
		
		self.initStatsWidget()
	
	
	def initUI(self):
		
		self.setFixedWidth(GlobalConfig.StatsWidgetWidth)
		
		self.lbl1Text = QtGui.QLabel('score: ', self)
		self.lbl1Value = QtGui.QLabel('0', self)
		self.lbl1Value.setFixedWidth(50)
		self.lbl1Value.setAlignment(QtCore.Qt.AlignRight)
		
		hbox1 = QtGui.QHBoxLayout()
		hbox1.addWidget(self.lbl1Text)
		hbox1.addStretch(1)
		hbox1.addWidget(self.lbl1Value)
		
		vbox = QtGui.QVBoxLayout()
		vbox.addLayout(hbox1)
		
		self.setLayout(vbox)