
from agent import Agent
from datamap import Flag, Node

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
		
		for _s in self.state.get('^state'):
			for _t in s.get('^type', 'state'):
				_o = s.add('^operator', '', Flag.PLUS)
				_o.add('^name', 'move-north')
	
	
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
		
		for _s in self.state.get('^state'):
			for _o in _s.get('^operator'):
				for _n in _o.get('^name', 'move-north'):
					for _io in _s.get('^io'):
						for _ol in _io.get('^output-link'):
							for _ol in _io.get('^output-link'):
								_m = _ol.add('^move')
								_m.add('^direction', 'north')
