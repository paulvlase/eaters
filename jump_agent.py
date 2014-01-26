
from agent import Agent
from datamap import	Node


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

		for _s in self.wm.get('^state'):
			for _t in _s.get('^type'):

				_n = self.wm.add('^directions')
				_e = self.wm.add('^directions')
				_s = self.wm.add('^directions')
				_w = self.wm.add('^directions')

				_n.add('^value', 'north')
				_n.add('^opposite', 'south')

				_e.add('^value', 'east')
				_e.add('^opposite', 'west')

				_s.add('^value', 'south')
				_s.add('^opposite', 'north')

				_w.add('^value', 'west')
				_w.add('^opposite', 'east')


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

		for _s in self.wm.get('^state'):
			for _io in _s.get('^io'):
				for _il in _io.get('^input-link'):
					for _ml in _il.get('^my-location'):
						for _dir in _ml.get(''):
							for _content in _dir.get('_content <> wall'):
								_o = _s.add('^operator o + =')
								_o.add('^name jump')
								_o.add('^content ' + _content)

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

		for _s in self.wm.get('^state'):
			for _io in _s.get('^io'):
				for _ol in _io.get('^output-link'):
					for _o in _s.get('^operator'):
						for _name in o.get('^name', ('move jump')):
							for _dir in _o.get('^direction'):
								_d = ol.add('^' + _name)
								_d.add('^direction ' + _dir)


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

		for _s in self.wm.get('^state'):
			for _io in _s.get('^io'):
				for _ol in _io.get('^output-link'):
					for _o in _s.get('^operator'):
						for _name in _o.get('^name'):
							for _direction in _ol.get('^' + _name):
								for _v1 in _direction.get('^status'):
									_ol.remove('^' + _name + ' ' + _direction)
