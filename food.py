
from PyQt4 import QtCore, QtGui

from block import Block
from global_config import GlobalConfig


class NormalFood(Block):
	
	def draw(self, painter):
		d = GlobalConfig.BlockDim
		
		painter.setPen(QtGui.QColor(0x000000))
		painter.setBrush(QtGui.QColor(0x000ff0))
		
		coords = []
		coords.append(QtCore.QPoint((self.j + 0.50) * d, (self.i + 0.35) * d))
		coords.append(QtCore.QPoint((self.j + 0.60) * d, (self.i + 0.5) * d))
		coords.append(QtCore.QPoint((self.j + 0.50) * d, (self.i + 0.65) * d))
		coords.append(QtCore.QPoint((self.j + 0.40) * d, (self.i + 0.5) * d))
		
		rhomb = QtGui.QPolygon(coords)
		
		painter.drawPolygon(rhomb)


class BonusFood(Block):
	
	def draw(self, painter):
		d = GlobalConfig.BlockDim
		
		color = QtGui.QColor(0xff0000)
		painter.fillRect((self.j + 0.35) * d, (self.i + 0.35) * d , 0.3 * d, 0.3 * d, color)
