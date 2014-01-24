
from PyQt4 import QtCore, QtGui

from block import Block
from global_config import GlobalConfig


class NormalFood(Block):
	
	def draw(self, painter):
		d = GlobalConfig.BlockDim
		
		color = QtGui.QColor(0x0000ff)
		painter.fillRect(self.j * d + d / 4, self.i * d + d / 4, d / 2, d / 2, color)

class BonusFood(Block):
	
	def draw(self, painter):
		d = GlobalConfig.BlockDim
		
		color = QtGui.QColor(0xff0000)
		painter.fillRect(self.j * d + d / 4, self.i * d + d / 4, d / 2, d / 2, color)
