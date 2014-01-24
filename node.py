
class DataMapNode(object):
	
	def __init__(self, value):
		
		self.value = value
		self.augmentations[]
		self.oRand = 1
		self.gRand = 1
	
	def addAugmentation(self, name, value, flag):
		v = value
		if value is None:
			if name == '^operator':
				v = 'o' + str(self.rand)
				v = DataMapNode(v, flag)
				self.rand = self.rand + 1
			else:
				v = 'g' + str(self.rand)
				v = DataMapNode(v, flag)
				self.gRand = self.gRand + 1 
		
		self.augmentations.append((name, v))
		
		return v
	
	def hasAugmentation(self, name, value):
		
		for augm in augmentations:
			if augm[0] == name and augm[1] == value:
				return True
		
		return False
	
	
	def getAugmentations(self, name):
		
		augmens = []
		for augm in augmentations:
			if augm[0] == name:
				augments.append(augm)
		
		return augmens


class Flag(object):
	
	NOTHING = 0
	PLUS = 1
	EQUAL = 2