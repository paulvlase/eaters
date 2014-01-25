
from agent import Agent
from datamap import	Node


'''
# Corrected from move-north.soar so that operator applies more than once.
'''

class MoveNorth2Agent(Agent):

	def proposePhase(self):
		pass


	def decisionPhase(self):
		pass


	def applyPhase(self):
		pass
	
	
	'''
	# Propose*move-north:
	# If I am at some location, then propose the move-north operator.

	sp {propose*move-north
		(state <s> ^io.input-link.eater <e>)
		(<e> ^x <x> ^y <y>)
	-->
		(<s> ^operator <o> +)
		(<o> ^name move-north)
	}
	'''
	def propose_moveNorth(self):
		
		for _s in self.state.get('^state'):
			for _io in _s.get('^io'):
				for _il in _io.get('^input-link'):
					for _e in _il.get('^eater'):
						for _x in _e.get('^x'):
							for _y in _e.get('^y'):
								_o = s.add('^operator o +')
								_o.add('^name move-north')
	
	
	'''
	# Apply*move-north:
	# If the move-north operator is selected, then generate an output command to 
	# move north.
	
	sp {apply*move-north
		(state <s> ^operator.name move-north
				   ^io.output-link <ol>)
	-->
		(<ol> ^move.direction north)}
	'''
	def apply_moveNorth(self):
		
		for _s in self.state.get('^state'):
			for _o in _s.get('^operator'):
				for _n in _o.get('^name move-north'):
					for _io in _s.get('^io'):
						for _ol in _io.get('^output-link'):
							_move = _ol.add('^move')
							_move.add('^direction north')
	
	
	'''
	# Apply*move-north*remove-move
	# If the move-north successfully performs a move command, then remove
	# the command from the output-link

	sp {apply*move-north*remove-move
		(state <s> ^operator.name move-north
				   ^io.output-link <ol>)
		(<ol> ^move <move>)
		(<move> ^status complete)
	-->
		(<ol> ^move <move> -)}
	'''
	def apply_moveNorth_removeMove(self):
		
		for _s in self.state.get('^state'):
			for _o in _s.get('^operator'):
				for _n in _o.get('^name move-north'):
					for _io in _s.get('^io'):
						for _ol in _io.get('^output-link'):
							for _move in _ol.get('^move'):
								for _s in _move.get('^status'):
									_ol.remove('^move ' + _move)
	