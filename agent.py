# File: agent.py

import math
from PyQt4 import QtCore, QtGui


"""
	Paul v0.0:
	An agent
"""
class Agent():
	
	"""
		Paul v0.0:
	"""
	
	R = 5
	
	def __init__(self, i, j):
	
		self.statsWidget = RobotStatsWidget(self)
	
	
	def move(self):
		pass
	
	
	def draw(self, painter):
		pass
	
	

	def getStatsWidget(self):
		return self.statsWidget