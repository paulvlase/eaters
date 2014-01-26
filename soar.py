
class Soar(object):

	def __init__(self, board, agents):

		self.board = board
		self.agents = agents

	def step(self):

		for agent in self.agents:
			raw_input()
			agent.inputPhase(self.board)
			raw_input()

		for agent in self.agents:
			agent.proposePhase()
			agent.decisionPhase()
			agent.applyPhase()

		for agent in self.agents:
			raw_input()
			agent.outputPhase(self.board)
			raw_input()
