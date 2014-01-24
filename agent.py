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
	
	
	
	def __init__(self, i, j, color):
		super(Agent, self).__init__(i, j)
	
		self.color = color
		self.direction = Direction.NORTH
		self.animationStep = 0
		self.animationDirStep = 1
		
		self.statsWidget = AgentStats(self)
	
	
	def step(self):
		
		self.inputPhase()
		self.proposePhase()
		self.decisionPhase()
		self.applyPhase()
		self.outputPhase()
	
	
	def inputPhase(self):
		pass
	
	
	def self.proposePhase(self):
		pass
	
	
	def self.decisionPhase(self):
		pass
	
	
	def self.applyPhase(self):
		pass
	
	
	def self.outputPhase(self):
		pass
	
	
	def draw(self, painter):
		d = GlobalConfig.BlockDim
		
		painter.setPen(QtGui.QColor(0x000000))
		painter.setBrush(QtGui.QColor(color))
		
		rect = QtCore.QRect(round(self.j * d + d * 0.1), round(self.i * d + d * 0.1), round(d * 0.8),round( d * 0.8))
		
		# Default for Direction.WEST
		
		startAngle = self.animationStep * 15

		self.animationStep = self.animationStep + self.animationDirStep
		if self.animationStep < 0:
			self.animationStep = 1
			self.animationDirStep = 1
		elif self.animationStep > 4:
			self.animationStep = 3
			self.animationDirStep = -1

		spanAngle = 360 - 2 * startAngle
		
		angle = 0
		if self.direction == Direction.NORTH:
			angle = 90
		elif self.direction == Direction.WEST:
			angle = 180
		elif self.direction == Direction.SOUTH:
			angle = 270
		
		startAngle = startAngle + angle
		
		painter.drawPie(rect, startAngle * 16, spanAngle * 16)
	
	
	def getStatsWidget(self):
		return self.statsWidget


class Direction(object):
	
	EAST = 0
	NORTH = 1
	WEST = 2
	SOUTH = 3