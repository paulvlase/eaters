
from agent import Agent
from datamap import	Node


class MoveNorthAgent(Agent):

	def __init__(self, i, j):
		super(MoveNorthAgent, self).__init__(i, j)

	def proposePhase(self):

		self.propose_moveNorth()

	def decisionPhase(self):
		pass

	def applyPhase(self):

		self.apply_moveNorth()

	'''
	# Propose*move-north:
	# If I exist, then propose the move-north operator.

	sp {propose*move-north
		(state <s> ^type state)
	-->
		(<s> ^operator <o> +)
		(<o> ^name move-north)}
	'''
	def propose_moveNorth(self):
		print('propose_moveNorth')

		for (a, _s) in self.wm.get('^state'):
			augms = _s.get('^type state')
			print('propose_moveNorth: ', augms)
			for (a, v) in _s.get('^type state'):
				_o = s.add('^operator +')
				_o.add('^name move-north')


	'''
	# Apply*move-north:
	# If the move-north operator is selected, then generate an output command to
	# move north.

	sp {apply*move-north
		(state <s> ^operator <o>
					^io <io>)
		(<io> ^output-link <ol>)
		(<o> ^name move-north)
	-->
		(<ol> ^move <move>)
		(<move> ^direction north)}


	## short cut version
	#sp {move-north*apply
	#   (state <s> ^operator.name move-north
	#              ^io.output-link <ol>)
	#-->
	#   (<ol> ^move.direction north)}
	'''
	def apply_moveNorth(self):
		print('apply_moveNorth')

		for (_a1, _s) in self.wm.get('^state'):
			for (_a2, _o) in _s.get('^operator'):
				for (_a3, _n) in _o.get('^name move-north'):
					for (_a4, _io) in _s.get('^io'):
						for (_a5, _ol) in _io.get('^output-link'):
							_m = _ol.add('^move')
							_m.add('^direction north')
