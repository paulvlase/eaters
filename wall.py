
from PyQt4 import QtCore, QtGui

from block import Block
from global_config import GlobalConfig


class Wall(Block):

	def draw(self, painter):
		d = GlobalConfig.BlockDim

		color = QtGui.QColor(0x000000)
		painter.fillRect(self.x * d + 1, self.y * d + 1, d - 3, d - 3, color)