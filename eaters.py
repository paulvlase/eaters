#!/usr/bin/python
# -*- coding: utf-8 -*-

# File: eaters.py

import sys, random
from PyQt4 import QtCore, QtGui


from main_window import MainWindow
from placeholder import Placeholder

"""
	Paul v0.0:
	Fereastra simulatorului.
"""
class Simulator(QtGui.QMainWindow):
	
	def __init__(self):
		super(Simulator, self).__init__()
		
		self.initUI()
	
	
	def initUI(self):
		
		self.fname = QtCore.QString('')
		
		self.placeholder = None
		
		runAction = QtGui.QAction(QtGui.QIcon('new.png'), 'Run', self)
		runAction.setShortcut('Ctrl+N')
		runAction.setStatusTip('Run eaters')
		runAction.triggered.connect(self.runEaters)
		
		exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit eaters')
		exitAction.triggered.connect(self.exitEaters)
		
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(runAction)
		fileMenu.addAction(exitAction)
		
		#self.statusbar = self.statusBar()        
		#self.simMap.msg2Statusbar[str].connect(self.statusbar.showMessage)
		
		#self.simMap.start()
		self.setCentralWidget(MainWindow(self))
		
		self.center()
		self.setWindowTitle('Eaters')        
		self.show()
	
	
	def runEaters(self):
		
		QtCore.qDebug('eaters.Eaters.newMap')
		
		self.placeholder = Placeholder(self)
		
		self.setCentralWidget(self.placeholder)
	
	
	def exitEaters(self):
		
		QtCore.qDebug('eaters.Eaters.exitEaters')
		
		if self.saveMap() == True:
			QtGui.qApp.quit()
	
	
	def center(self):
		
		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width() - size.width()) / 2, 
			(screen.height() - size.height()) /2)


def main():
	
	app = QtGui.QApplication([])
	simulator = Simulator()    
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
