
# File: board.py

import math
import random
from PyQt4 import QtCore, QtGui

from board_stats import BoardStats
from food import BonusFood, NormalFood
from global_config import GlobalConfig
from move_north_agent import MoveNorthAgent
from soar import Soar
from wall import Wall



"""
	Paul v0.0:
	Harta pe care se deplaseaza robotul
"""
class Board(QtGui.QFrame):

	msg2Statusbar = QtCore.pyqtSignal(str)

	Width = 17
	Height = 17
	Speed = 100


	def __init__(self, parent):
		super(Board, self).__init__(parent)

		self.parent = parent

		self.initBoard()
		self.initAgents()

		self.initUI()

		self.timer.start(Board.Speed, self)


	def initBoard(self):
		self.blocks = []

		for i in range(Board.Height):
			for j in range(Board.Width):
				self.blocks.append(None)

		for j in range(Board.Width):
			self.setBlockAt(0, j, Wall(0, j))
			self.setBlockAt(Board.Width - 1, j, Wall(Board.Width - 1, j))

		for i in range(1, Board.Height - 1):
			self.setBlockAt(i, 0, Wall(i, 0))
			self.setBlockAt(i, Board.Height - 1, Wall(i, Board.Height - 1))

		n = random.randint(0, math.floor(Board.Width * Board.Height / 2))

		for k in range(n):

			i = random.randint(1, Board.Width - 1)
			j = random.randint(1, Board.Height - 1)

			if self.getBlockAt(i, j) is None and\
					self.getBlockAt(i - 1, j - 1) is None and\
					self.getBlockAt(i - 1, j + 1) is None and\
					self.getBlockAt(i + 1, j - 1) is None and\
					self.getBlockAt(i + 1, j + 1) is None:
				self.setBlockAt(i, j, Wall(i, j))


		for j in range(1, Board.Width - 1):

			if j % 3 == 2:
				for i in range(1, Board.Height - 1):

					if self.getBlockAt(i, j) is None:
						self.setBlockAt(i, j, BonusFood(i, j))

			else:
				for i in range(1, Board.Height - 1):

					if self.getBlockAt(i, j) is None:
						self.setBlockAt(i, j, NormalFood(i, j))


	def initAgents(self):
		self.agents = []

		i = random.randint(1, Board.Width - 2)
		j = random.randint(1, Board.Height - 2)

		agent = MoveNorthAgent(i, j)
		self.agents.append(agent)
		self.setBlockAt(i, j, agent)

		self.soar = Soar(self.blocks, self.agents)


	def initUI(self):
		QtCore.qDebug('sim_map.Map.initMap')

		self.timer = QtCore.QBasicTimer()
		self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)

		self.setFocusPolicy(QtCore.Qt.StrongFocus)
		self.setFixedSize(Board.Width * GlobalConfig.BlockDim + 1, Board.Height * GlobalConfig.BlockDim + 1)
		self.isStarted = False
		self.isPaused = False

		self.boardStats = BoardStats(self)


	def start(self):
		QtCore.qDebug('sim_map.Map.start')

		if self.isPaused:
			return

		self.isStarted = True

		self.clearMap()

		self.msg2Statusbar.emit(str(0))


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
		painter.fillRect(0, 0, rect.right(), rect.bottom(), QtGui.QColor(0xffffff))

		#TODO
		#QtCore.qDebug('[sim_map.Map.paintEvent] %d %d %d %d' % (rect.top(), rect.left(), rect.bottom(), rect.right()))

		for block in self.blocks:
			if block is not None:
				block.draw(painter)


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

		else:
			super(Map, self).keyPressEvent(event)


	def timerEvent(self, event):

		if event.timerId() == self.timer.timerId():
			self.soar.step()
			self.repaint()

		else:
			super(Map, self).timerEvent(event)


	def getStatsWidgets(self):

		widgets = []

		widgets.append(self.boardStats)

		#if self.robot is not None:
		#	widgets.append(self.robot.getStatsWidget())

		return widgets


	def setStatsWidget(self):

		widgets = self.getStatsWidgets()

		self.parent.setStatsWidgets(widgets)


	def getBlockAt(self, i, j):
		return self.blocks[i * Board.Width + j]


	def setBlockAt(self, i, j, block):
		self.blocks[i * Board.Width + j] = block
