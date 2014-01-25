
from agent import Agent
from datamap import	Node


'''
# This program proposes the move-to-food operator in any direction
# that contains normal or bonus food.  If there is no food nearby, no
# instances of the operator will be proposed and the halt operator
# will be proposed.
'''

class MoveToFoodAgent(Agent):

	def __init__(self, i, j):
		super(MoveToFoodAgent, self).__init__(i, j)

		self.color = 0xFF0000

	
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
		
		for _s in self.state.get('^state'):
			for _io in _s.get('^io'):
				for _il in _io.get('^input-link'):
					for _ml in _il.get('^my-location'):
						for _di in _ml.get(''):
							for _co in _di.get('^content'):
								o = _s.add('^operator o + =')
								o.add('^name move-to-food')
								o.add('^direction ' + di.name)
	
	
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
		
		for _s in self.state.get('^state'):
			for _io in _s.get('^io'):
				for _ol in _io.get('^output-link'):
					for _o in _s.get('^operator'):
						for _n in _o.get('^name move-to-food'):
							for _di in _o.get('^direction'):
								_d = _ol.add('^move')
								_d.add(di.name)
	
	
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
		
		for _s in self.state.get('^state'):
			for _io in _s.get('^io'):
				for _ol in _io.get('^output-link'):
					for _o in _s.get('^operator'):
						for _n in _o.get('^name move-to-food'):
							for _move in _ol.get('^move'):
								for _s in _move.get('^status complete'):
									_ol.remove('^move ' + _move)
