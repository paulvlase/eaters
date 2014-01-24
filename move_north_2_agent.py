
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
		
		for s in self.state.getAugmentations('^state'):
			for io in s.getAugmentations('^io'):
				for il in io.getAugmentations('input-link'):
					for e in il.getAugmentations('eater'):
						for x in e.getAugmentations('^x'):
							for y in e.getAugmentations('^y'):
								o = s.addAugmentation('^operator'), '+')
								o.addAugmentation('^name', 'move-north')
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
		
		for _s in self.state.getAugmentations('^state'):
			for _o in _s.getAugmentations('^operator'):
				for _name in _o.getAugmentations('^name', 'move-north'):
					for _io in _s.getAugmentations('^io'):
						for _ol in _io.getAugmentations('^output-link'):
							_move = _ol.addAugmentation('^move')
							_move.addAugmention('^direction', 'north')
	
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
	def apply_moveNorth_RemoveMove(self):
		
		for _s in self.state.getAugmentations('^state'):
			for _o in _s.getAugmentations('^operator'):
				for _name in _o.getAugmentations('^name', 'move-north'):
					for _io in s.getAugmentations('^io'):
						for _ol in _io.getAugmentations('output-link'):
							for _move in _ol.getAugmentations('^move'):
								for _a1 in _move.getAugmentations('^status'):
									_ol.removeAugmentation('^move', _move)
	