from utils import error, next_move
from heapq import heappush, heappop
from npuzzle import Npuzzle

class Queue:
	def __init__(self, setting):
		self.size = setting.size
		self.complexity_time = 0
		self.complexity_size = 1
		self.actual_size = 1
		self.opened = OpenedQueue()
		self.opened.push(Npuzzle(setting.start, 0, setting, None))
		self.opened_hash = dict()
		self.closed = set()

	def solve(self, setting):
		while self.opened.tree:
			elt = self.opened.pop()
			self.closed.add(elt)
			moves = next_move(elt.content, self.size)
			self.complexity_time += 1
			self.actual_size += len(moves)
			if self.actual_size > self.complexity_size:
				self.complexity_size = self.actual_size
			for s in moves:
				s = Npuzzle(s, elt.g + 1, setting, elt)
				if s.content == setting.goal:
					return s
				if s.content in self.closed:
					self.actual_size -= 1
				elif s.content in self.opened_hash:
					e = self.opened_hash[s.content]
					if s.g < e.g:
						s.parent = e.parent
						s.g = e.g
						s.cost = e.cost
					self.actual_size -= 1
				else:
					self.opened.push(s)
					self.opened_hash[s.content] = s
		return None

	def final(self):
		if self.solution:
			print("Complexity in time:", self.complexity_time)
			print("Complexity in size:", self.complexity_size)
			print("Number of moves:", self.solution.g)
			print("Solution:")
			# for step in self.solution.get_path():
			# 	print(step)
			# for nb, step in enumerate(self.solution.get_path()):
			# 	print('\nStep %d:' % nb)
			# 	for i in range(len(step)):
			# 		print('%2s' % step[i], end='')
			# 		print(' ', end='') if i%self.size != self.size-1 else print('')
		else:
			error("Unsolvable")

class OpenedQueue:
	def __init__(self):
		self.tree = list()
		self.id = 0

	def push(self, npuzzle):
		heappush(self.tree, (npuzzle.cost, self.id, npuzzle))
		self.id += 1

	def pop(self):
		return heappop(self.tree)[2]
