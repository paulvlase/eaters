
'''
############################ Move-north operator ############################
'''

class MoveNorthAgent(Agent):
	
	def proposePhase(self):
		pass
	
	def decisionPhase(self):
		pass
	
	def applyPhase(self):
		pass
	
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
		
		if self.state.hasAugmentation('^type', 'state'):
			
			o = self.state.addAugmentation('^operator', '', '+')
			o.addAugmentation('^name', 'move-north')

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
		
		os = 
		
		for o in self.state.getAugmentations('^operator')
			if o.hasAugmentation('^name', 'move-north')
				for io in self.state.getAugmentations('^io')
					for ol in io.getAugmentations('^output-link')
						for ol in io.getAugmentations('^output-link')
							m = ol.addAugmentation('^move')
							m.addAugmentation('^direction', 'north')
