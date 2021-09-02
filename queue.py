from utils import error, next_move
from heapq import heappush, heappop
from npuzzle import Npuzzle

class Queue:
	def __init__(self, setting):
		self.size = setting.size
		self.complexity_time = 0
		self.complexity_size = 0
		self.opened = OpenedQueue()
		self.opened.push(Npuzzle(setting.start, 0, setting, None), self)
		self.opened_hash = dict()
		self.closed = set()

	def solve(self, setting):
		while self.opened.tree:
			elt = self.opened.pop(self)
			####################################################################
			# if self.complexity_time > 100000:
			# 	print(elt.cost)
			# 	print(elt.h)
			# 	print(elt.g)
			# 	for i in range(self.size**2):
			# 		print('%2s' % elt.content[i], end='')
			# 		print(' ', end='') if i%self.size != self.size-1 else print('')
			# 	print()
			# 	exit(1)
			####################################################################
			self.closed.add(elt)
			moves = next_move(elt.content, self.size)
			for s in moves:
				s = Npuzzle(s, elt.g + 1, setting, elt)
				if s.content == setting.goal:
					return s
				if s.content in self.opened_hash:
					e = self.opened_hash[s.content]
					if s.g < e.g:
						s.parent = e.parent
						s.g = e.g
						s.cost = e.cost
				elif s.content not in self.closed:
					self.opened.push(s, self)
					self.opened_hash[s.content] = s
		return None

	def final(self):
		if self.solution:
			# print("Complexity in time:", self.complexity_time)
			# print("Complexity in size:", self.complexity_size)
			# print("Number of moves:", self.solution.g)
			# print("Solution:")
			############################ FAST PRINT ############################
			# for step in self.solution.get_path():
			# 	print(step)
			######################## GOOD LOOKING PRINT ########################
			# for nb, step in enumerate(self.solution.get_path()):
			# 	print('\nStep %d:' % nb)
			# 	for i in range(len(step)):
			# 		print('%2s' % step[i], end='')
			# 		print(' ', end='') if i%self.size != self.size-1 else print('')
			########################### SCRIPT PRINT ###########################
			print('%d;%d;%d;' % (self.complexity_time, self.complexity_size, self.solution.g), end='')

		else:
			error("Unsolvable")

class OpenedQueue:
	def __init__(self):
		self.tree = list()
		self.id = 0

	def push(self, npuzzle, queue):
		heappush(self.tree, (npuzzle.cost, self.id, npuzzle))
		self.id += 1
		queue.complexity_size += 1

	def pop(self, queue):
		queue.complexity_size -= 1
		queue.complexity_time += 1
		# print('complexity_size: ', queue.complexity_size)
		# print('complexity_time: ', queue.complexity_time)
		# print()
		return heappop(self.tree)[2]
