# File: agent.py

import math
from PyQt4 import QtCore, QtGui

from agent_stats import AgentStats
from block import Block
from datamap import Node
from global_config import GlobalConfig


"""
	Paul v0.0:
	An agent
"""
class Agent(Block):

	"""
		Paul v0.0:
	"""

	def __init__(self, x, y):
		super(Agent, self).__init__(x, y)

		self.name = 'grey'
		self.direction = None
		self.score = 0

		self.initDatamap()
		self.initUI()

	def initDatamap(self):

		self.wm = Node('.')

		_s = self.wm.add('^state')
		_s.add('^type state')
		_s.add('^superstate nil')

		_io = _s.add('^io')
		_io.add('^input-link')
		_io.add('^output-link')


	def initUI(self):

		self.color = 0xAAAAAA
		self.animationStep = 0
		self.animationDirStep = 1

		self.statsWidget = AgentStats(self)


	def step(self):

		self.inputPhase()
		self.proposePhase()
		self.decisionPhase()
		self.applyPhase()
		self.outputPhase()


	def inputPhase(self, board):

		print('agent.Agent.inputPhase')

		(_a1, _s) = self.wm.get('^state')[0]
		augms = _s.get('^io')

		if len(augms) > 1:
			print 'Error multiple ^io augmentations'
			return -1

		(_a2, _io) = _s.get('^io')[0]
		(_a3, _il) = _io.get('^input-link')[0]
		_eater = _il.add('^eater')

		if self.direction != None:
			_direction = _eater.add('^direction ' + self.direction)

		_eater.add('^name ' + self.name)
		_eater.add('^score ' + str(self.score))
		_eater.add('^x ' + str(self.x))
		_eater.add('^y ' + str(self.y))


	def proposePhase(self):
		pass


	def decisionPhase(self):
		pass


	def applyPhase(self):
		pass


	def outputPhase(self, board):

		print('agent.Agent.outputPhase')

		(a, _s) = self.wm.get('^state')[0]
		augms = _s.get('^io')

		if len(augms) > 1:
			print 'Error multiple ^io augmentations'
			return -1

		(a, _io) = augms[0]

		(a, _ol) = _io.get('^output-link')[0]

		action_done = False

		for (a, _action) in _ol.get():
			if actionDone == False and len(_action[1].get('^status complete')) == 0:
				if _action[0] == '^move':

					_direction = _action[1].get('^direction')

					x = self.x
					y = self.y

					if _direction[1] == 'north':
						y = y - 1
					elif _direction[1] == 'west':
						x = x - 1
					elif _direction[1] == 'south':
						y = y + 1
					elif _direction[1] == 'east':
						x = x + 1

					block = self.board.getBlockAt(x, y)
					move = False
					score = 0
					if block is None:
						move = True
					elif instanceof(block, Food):
						move = True
						score = Food.getScore()

					if move == True:
						self.board.setBlockAt(self.x, self.y, None)
						self.board.setBlockAt(x, y, self)
						self.x = x
						self.y = y

					_action.add('^status complete')
					actionDone = True
				elif _action[1] == '^jump':
					pass
					_action.add('^status complete')
					actionDone = True


	def draw(self, painter):
		d = GlobalConfig.BlockDim

		painter.setPen(QtGui.QColor(0x000000))
		painter.setBrush(QtGui.QColor(self.color))

		rect = QtCore.QRect(round(self.x * d + d * 0.1), round(self.y * d + d * 0.1), round(d * 0.8),round( d * 0.8))

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


	def dumpDatamap(self, node = None, visited = None):

		if node is None:
			node = self.wm
			visited = {}

		for (l, a) in node.get():
			print('%s %s %s' % (node, l, a))

		visited[node] = node
		for (l, a) in node.get():
			if a not in visited:
				self.dumpDatamap(a, visited)


class Direction(object):

	EAST = 0
	NORTH = 1
	WEST = 2
	SOUTH = 3
