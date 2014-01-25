
class Node(object):
	
	def __init__(self, value):
		
		self.value = value
		self.augments = []
		self.oRand = 1
		self.gRand = 1
	
	
	def add(self, augm):
		toks = augm.split()
		
		name = toks[0]
		value = toks[1]
		
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
		
		self.augments.append((name, v))
		
		return v
	
	
	def get(self, augm):
		
		toks = augm.split()
		
		name = toks[0]
		value = tocks[1]
		
		augms = []
		for a in self.augments:
			if a[0] == name:
				if value is None or value == a[1]:
					augms.append(a)
		
		return augms

	
	def remove(self, augm):
		
		pass
	