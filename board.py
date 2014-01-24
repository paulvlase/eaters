# File: board.py

import math
from PyQt4 import QtCore, QtGui

from agent import Agent
from board_stats import BoardStats


"""
	Paul v0.0:
	Harta pe care se deplaseaza robotul
"""
class Board(QtGui.QFrame):
	
	msg2Statusbar = QtCore.pyqtSignal(str)
	
	Width = 650
	Height = 480
	Speed = 100
	
	
	def __init__(self, parent):
		super(Board, self).__init__(parent)
	
		self.parent = parent
	
		self.initUI()
		self.initAgents()
	
	def initUI(self):
		QtCore.qDebug('sim_map.Map.initMap')
		
		self.timer = QtCore.QBasicTimer()
		self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
		
		self.objects = []
		self.setFocusPolicy(QtCore.Qt.StrongFocus)
		self.setFixedSize(Board.Width, Board.Height)
		self.isStarted = False
		self.isPaused = False
		self.clearMap()

		self.boardStats = BoardStats(self)
	
	
	def initAgents(self):
		pass
	
	
	def start(self):
		QtCore.qDebug('sim_map.Map.start')
		
		if self.isPaused:
			return
		
		self.isStarted = True
		
		self.clearMap()
		
		self.msg2Statusbar.emit(str(0))
		
		self.timer.start(Map.Speed, self)
	
	
	def pause(self):
		QtCore.qDebug('sim_map.Map.pause')
		
		if not self.isStarted:
			return
		
		self.isPaused = not self.isPaused
		
		if self.isPaused:
			self.timer.stop()
			self.msg2Statusbar.emit("paused")
			
		else:
			self.timer.start(Map.Speed, self)
			self.msg2Statusbar.emit(str(0))
		
		self.update()
	
	
	def paintEvent(self, event):
		
		painter = QtGui.QPainter(self)
		rect = self.contentsRect()
		
		painter.setPen(QtGui.QColor(0xff0000))
		#TODO
		#QtCore.qDebug('[sim_map.Map.paintEvent] %d %d %d %d' % (rect.top(), rect.left(), rect.bottom(), rect.right())) 
		painter.fillRect(0, 0, rect.right(), rect.bottom(), QtGui.QColor(0xffffff))
		
		for obj in self.objects:
			obj.draw(painter)
	
	
	def keyPressEvent(self, event):
		
		key = event.key()
		
		if key == QtCore.Qt.Key_S:
			self.start()
			return
		
		if not self.isStarted:
			super(Map, self).keyPressEvent(event)
			return
		
		if key == QtCore.Qt.Key_P:
			self.pause()
			return
		
		if self.isPaused:
			return
		
		elif key == QtCore.Qt.Key_Q:
			self.robot.increaseLeftMotorSpeed(10)
		
		elif key == QtCore.Qt.Key_A:
			self.robot.increaseLeftMotorSpeed(-10)
		
		elif key == QtCore.Qt.Key_E:
			self.robot.increaseRightMotorSpeed(10)
		
		elif key == QtCore.Qt.Key_D:
			self.robot.increaseRightMotorSpeed(-10)
		
		else:
			super(Map, self).keyPressEvent(event)
	
	
	def timerEvent(self, event):
		
		if event.timerId() == self.timer.timerId():
			
			if self.robot is not None:
				self.robot.move()
				self.repaint()
		
		else:
			super(Map, self).timerEvent(event)
	
	
	def clearMap(self):
		self.objects = []

	
	def getStatsWidgets(self):
		
		widgets = []
		
		widgets.append(self.boardStats)
		
		#if self.robot is not None:
		#	widgets.append(self.robot.getStatsWidget())
	
		return widgets
	
	
	def setStatsWidget(self):
		
		widgets = self.getStatsWidgets()
		
		self.parent.setStatsWidgets(widgets)

