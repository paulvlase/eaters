
'''
# This program proposes the move-to-food operator in any direction
# that contains normal or bonus food.  If there is no food nearby, no
# instances of the operator will be proposed and the halt operator
# will be proposed.
'''

class MoveToFoodAgent(Agent):
	
	def proposePhase(self):
		pass
	
	def decisionPhase(self):
		pass
	
	def applyPhase(self):
		pass
	
	'''
	# Propose*move-to-food*normalfood
	# If there is normalfood in an adjacent cell, 
	#    propose move-to-food in the direction of that cell
	#    and indicate that this operator can be selected randomly.
	
	sp {propose*move-to-food
		(state <s> ^io.input-link.my-location.<dir>.content 
								<< normalfood bonusfood >>)
	-->
		(<s> ^operator <o> + =)
		(<o> ^name move-to-food
			 ^direction <dir>)}
	'''
	def propose_moveToFood(self):
		
		for io in self.state.getAugmentations('io'):
			for il in io.getAugmentations('^input-link'):
				for ml in il.getAugmentations('^my-location'):
					for di in ml.getAugmentations(''):
						for co in di.getAugmentations('content'):
							o = self.state.addAugmentation('^operator', '+=')
							o.addAugmentation('^name', 'move-to-food')
							o.addAugmentation('^direction', di.name)

	'''
	# Apply*move-to-food
	# If the move-to-food operator for a direction is selected,
	#    generate an output command to move in that direction.
	
	sp {apply*move-to-food
		(state <s> ^io.output-link <ol>
				   ^operator <o>)
		(<o> ^name move-to-food
			 ^direction <dir>)
	-->
		(<ol> ^move.direction <dir>)}
	'''
	def apply_moveToFood:
		
		for io in self.state.getAugmentations('io'):
			for ol in io.getAugmentations('output-link'):
				for o in self.state.getAugmentations('operator'):
					if o.hasAugmentation('^name', 'move-to-food'):
						for di in o.getAugmentation('^direction'):
							d = ol.addAugmentation('^move')
							d.addAugmentation(di.name)
	
	'''
	# Apply*move-to-food*remove-move:
	# If the move-to-food operator is selected,
	#    and there is a completed move command on the output link,
	#    then remove that command.
	
	sp {apply*move-to-food*remove-move
		(state <s> ^io.output-link <ol>
				   ^operator.name move-to-food)
		(<ol> ^move <move>)
		(<move> ^status complete)
	-->
		(<ol> ^move <move> -)}
	'''
	def apply_moveToFood_removeMove:
		
		for _io in self.state.getAugmentations('^io'):
			for _ol in self.getAugmentations('^output-link'):
				for _o in self.state.getAugmentations('^operator'):
					if _o.hasAugmentation('^name', 'move-to-food'):
						for _move in ol.getAugmentations('^move'):
							if _move.hasAugmentation('^status', 'complete'):
								ol.removeAugmentation('^move', _move)
