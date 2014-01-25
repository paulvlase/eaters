
class Node(object):
	
	def __init__(self, value):
		
		self.value = value
		self.augments = []
		self.oRand = 1
		self.gRand = 1
	
	
	def add(self, name, value = '', flag = Flag.NOTHING):
		v = value
		if value is None:
			if name == '^operator':
				v = 'o' + str(self.rand)
				v = Node(v, flag)
				self.rand = self.rand + 1
			else:
				v = 'g' + str(self.rand)
				v = Node(v, flag)
				self.gRand = self.gRand + 1 
		
		self.augmentations.append((name, v))
		
		return v
	
	
	def get(self, name, value = None, flag = Flag.NOTHING):
		
		augms = []
		for augm in self.augments:
			if augm[0] == name:
				if value is None or value == augm[1]:
				augms.append(augm)
		
		return augms


class Flag(object):
	
	NOTHING = 0
	PLUS = 1
	EQUAL = 2
	