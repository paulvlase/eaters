

class Flag(object):

	NONE = 0
	PLUS = 1
	EQUAL = 2


class Node(object):

	oRand = 1 # operator identifier
	sRand = 1 # state identifier
	iRand = 1 # general identifier

	def __init__(self, identifier, flags = Flag.NONE):

		self.identifier = identifier
		self.augments = {}
		self.flags = flags

	def add(self, augm):

		toks = augm.split()

		if len(toks) == 0:
			print('Wrong usage of add')
			return None

		attr = toks[0]

		idn = None
		flag = Flag.NONE


		if len(toks) > 1:

			if toks[1] == '+':
				flag = flag | Flag.PLUS

			else:
				idn = toks[1]

		if len(toks) > 2:

			if toks[2] == '+':
				flag = flag | Flag.PLUS

			elif toks[2] == '=':
				flag = flag | Flag.EQUAL

		if idn is None:

			if attr == '^state':
				idn = 'S' + str(Node.sRand)
				Node.sRand = Node.sRand + 1

			elif attr == '^operator':
				idn = 'O' + str(Node.oRand)
				Node.oRand = Node.oRand + 1

			else:
				idn = 'I' + str(Node.iRand)
				Node.iRand = Node.iRand + 1


		node = Node(idn, flag)
		if attr not in self.augments:
			self.augments[attr] = [node]

		else:
			self.augments[attr].append(node)

		print('set', self, augm)
		print('set', self, self.augments)
		#print('(%s %s %s)' % (self, attr, node))

		return node


	def get(self, augm = None):
		print('get', self, augm)
		print('get', self, self.augments)
		if augm == None:
			augms =  [(a, v) for a in self.augments.keys() for v in self.augments[a]]

			#for (a, v) in augms:
				#print('(%s %s %s)' % (self, a, v))

			return augms

		toks = augm.split()
		attr = toks[0]

		if len(toks) == 1:
			if attr in self.augments:
				return [(attr, v) for v in self.augments[attr]]
			else:
				return []


		if len(toks) == 2:
			val = toks[1]

			if attr == '^':
				return [(a, v) for a in self.augms.keys() for v in self.augments[attr] if v == val]

			else:
				return [(attr, v) for v in self.augments[attr] if v == val]

		return []


	def remove(self, augm):

		pass


	def __repr__(self):
		return self.identifier
