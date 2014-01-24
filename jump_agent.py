
class JumpAgent(Agent):
	
	def proposePhase(self):
		pass

	def decisionPhase(self):
		pass

	def applyPhase(self):
		pass

	'''
	sp {initialize*state*directions
		(state <ss> ^type state)
	-->
		(<ss> ^directions <n>   
			  ^directions <e>   
			  ^directions <s>   
			  ^directions <w>)
		(<n> ^value north ^opposite south)
		(<e> ^value east  ^opposite west)
		(<s> ^value south ^opposite north)
		(<w> ^value west  ^opposite east)}
	'''
	def initialize_state_directions(self):
		
		n = self.state.addAugmentation('^directions')
		e = self.state.addAugmentation('^directions')
		s = self.state.addAugmentation('^directions')
		w = self.state.addAugmentation('^directions')
		
		n.addAugmentation('^value', 'north')
		n.addAugmentation('^opposite', 'south')
		
		e.addAugmentation('^value', 'east')
		e.addAugmentation('^opposite', 'west')
		
		s.addAugmentation('^value', 'south')
		s.addAugmentation('^opposite', 'north')
	
		w.addAugmentation('^value', 'west')
		w.addAugmentation('^opposite', 'east')
	
	'''
	# Propose*jump:
	# If the content of a cell two steps away in a direction is not a wall, 
	#    propose jump in the direction of that cell, with the cell's content,
	#    and indicate that this operator can be selected randomly.

	sp {propose*jump
		(state <s> ^io.input-link.my-location.<dir>.<dir>.content 
				{ <content> <> wall })
	-->
		(<s> ^operator <o> +, =)
		(<o> ^name jump
			 ^direction <dir>
			 ^content <content>)} 
	'''
	def propose_jump:
		
		for io in self.state.getAugmentations('^io'):
			for il in io.getAugmentations('input-link'):
				for ml in il.getAugmentations('my-location'):
					for _dir in ml.getAugmentations(''):
						for _content in _dir.getAugmentations('_content'):
							if _content != 'wall':
								o = self.state.addAugmentation('^operator', '+, =')
								o.addAugmentation('^name', 'jump')
								o.addAugmentation('^content', _content)
	
	'''
	# Apply*move*jump
	# If the move or jump operator for a direction is selected,
	#    generate an output name to move in that direction.
	
	sp {apply*move
		(state <s> ^io.output-link <ol>
				   ^operator <o>)
		(<o> ^name { <name> << move jump >> }
			 ^direction <dir>)
	-->
		(<ol> ^<name>.direction <dir>)}  
	'''
	def apply_move_jump:
		
		for io in self.state.getAugmentations('^io'):
			for ol in io.getAugmentations('^output-link'):
				for o in self.state.getAugmentations('^operator'):
					 for _name in o.getAugmentations('^name', ('move', 'jump')):
						 for _dir in o.getAugmentations('^direction'):
							 d = ol.addAugmentation('^' + _name)
							 d.addAugmentation('^direction', _dir)
	
	'''
	# Apply*move*jump*remove-name:
	# If the move or jump operator is selected,
	#    and there is a completed name on the output link,
	#    then remove that name.

	sp {apply*move*remove-move
		(state <s> ^io.output-link <ol>
				   ^operator.name <name>)
		(<ol> ^<name> <direction>)
		(<direction> ^status complete)
	-->
		(<ol> ^<name> <direction> -)}
	'''
	def apply_move_jump_removeName:
		
		for io in self.state.getAugmentations('^io'):
			for ol in io.getAugmentations('^output-link'):
				for o in self.state.getAugmentations('^operator'):
					for _name in o.getAugmentations('^name'):
						for _direction in ol.getAugmentations('^' + _name):
							for v1 in _direction.getAugmentations('^status'):
								ol.removeAugmentation('^' + name, _direction)
	