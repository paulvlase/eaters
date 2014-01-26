
from PyQt4 import QtCore, QtGui

from block import Block
from global_config import GlobalConfig

class Food(Block):

	def __init__(self, x, y):
		super(Food, self).__init__(x, y)

		self.score = 0

	def getScore(self):
		return self.score


class NormalFood(Block):

	def __init__(self, x, y):
		super(NormalFood, self).__init__(x, y)

		self.score = 5


	def draw(self, painter):
		d = GlobalConfig.BlockDim

		painter.setPen(QtGui.QColor(0x000000))
		painter.setBrush(QtGui.QColor(0x000ff0))

		coords = []
		coords.append(QtCore.QPoint((self.x + 0.50) * d, (self.y + 0.35) * d))
		coords.append(QtCore.QPoint((self.x + 0.60) * d, (self.y + 0.5) * d))
		coords.append(QtCore.QPoint((self.x + 0.50) * d, (self.y + 0.65) * d))
		coords.append(QtCore.QPoint((self.x + 0.40) * d, (self.y + 0.5) * d))

		rhomb = QtGui.QPolygon(coords)

		painter.drawPolygon(rhomb)


class BonusFood(Block):

	def __init__(self, x, y):
		super(BonusFood, self).__init__(x, y)

		self.score = 10


	def draw(self, painter):
		d = GlobalConfig.BlockDim

		color = QtGui.QColor(0xff0000)
		painter.fillRect((self.x + 0.35) * d, (self.y + 0.35) * d , 0.3 * d, 0.3 * d, color)
