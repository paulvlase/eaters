# File: agent.py

import math
from PyQt4 import QtCore, QtGui

from agent_stats import AgentStats
from block import Block
from global_config import GlobalConfig


"""
	Paul v0.0:
	An agent
"""
class Agent(Block):
	
	"""
		Paul v0.0:
	"""
	
	
	
	def __init__(self, i, j):
		super(Agent, self).__init__(i, j)
	
		self.direction = 0
		self.statsWidget = AgentStats(self)
	
	
	def move(self):
		pass
	
	
	def draw(self, painter):
		d = GlobalConfig.BlockDim
		
		painter.setPen(QtGui.QColor(0x000000))
		painter.setBrush(QtGui.QColor(0x00ff00))
		
		rect = QtCore.QRect(round(self.j * d + d * 0.1), round(self.i * d + d * 0.1), round(d * 0.8),round( d * 0.8))
		startAngle = 135 * 16
		spanAngle = (360 - 90) * 16
		
		painter.drawPie(rect, startAngle, spanAngle)
	
	
	def getStatsWidget(self):
		return self.statsWidget


class Direction(object):
	
	EAST = 0
	NORTH = 1
	WEST = 2
	SOUTH = 3