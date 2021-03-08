from math import sqrt

class Npuzzle:
	def __init__(self, size, content, cost, parent, heuri):
		self.size = size
		self.cost = cost
		self.heuri = heuri
		self.parent = parent
		self.content = content

	def __str__(self):
		return 'N-Puzzle\nSize: %d\nContent: %s' % (self.size, self.content)
	
	def p_matrice(self):
		for i in range(len(self.content)):
			print('%s' % self.content[i], end='')
			print(' ', end='') if i%self.size != self.size-1 else print('')

	def pprint(self):
		print('Cost: %d | Heuri: %d | C + H: %d' % (self.cost, self.heuri, self.cost+self.heuri))
		for i in range(len(self.content)):
			print('%s' % self.content[i], end='')
			print(' ', end='') if i%self.size != self.size-1 else print('')

class Queue:
	def __init__(self, npuzzle_start):
		self.closed = []
		self.opened = [npuzzle_start]

class Algorithm:
	def __init__(self):
		self.algo = [self.manhattan, self.weighted, self.euclidian]

	def set_algo(self, algo):
		self.exec_algo = self.algo[algo]

	# manhattan distance
	def manhattan(self, content, size):
		heuri = 0
		for i in range(size ** 2):
			sta = content.index(str(i))
			objX, objY = int(i/size), int(i%size)
			staX, staY = int(sta/size), int(sta%size)
			heuri += abs(objX - staX) + abs(objY - staY)
		return heuri

	# weighted A*
	def weighted(self, content, size):
		heuri = 0
		weight = 2
		for i in range(size ** 2):
			sta = content.index(str(i))
			objX, objY = int(i/size), int(i%size)
			staX, staY = int(sta/size), int(sta%size)
			heuri += abs(objX - staX) + abs(objY - staY)
		return heuri * weight

	# euclidian distance
	def euclidian(self, content, size):
		heuri = 0
		weight = 2
		for i in range(size ** 2):
			sta = content.index(str(i))
			objX, objY = int(i/size), int(i%size)
			staX, staY = int(sta/size), int(sta%size)
			heuri += round(sqrt((objX - staX)**2 + (objY - staY)**2))
		return heuri