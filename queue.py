from npuzzle import Npuzzle

class Queue:
	def __init__(self, setting):
		self.size = setting.size
		self.complexity_time = 0
		self.complexity_size = 1
		self.actual_size = 1
		self.opened = list()
		self.opened_hash = dict()
		self.closed = set()
		self.opened.append(Npuzzle(setting.start, 0, setting, None))
		if setting.start == setting.goal:
			self.solution = self.opened.pop(0)
		else:
			self.solution = self.solve(setting)

	def solve(self, setting):
		while self.opened:
			elt = self.opened.pop(0)
			self.closed.add(elt)
			length, moves = elt.next_move(self.size)
			self.complexity_time += 1
			self.actual_size += length
			if self.actual_size > self.complexity_size:
				self.complexity_size = self.actual_size
			for s in moves:
				if s == setting.goal:
					return Npuzzle(s, elt.g + 1, setting, elt)
				if tuple(s) in self.closed:
					self.actual_size -= 1
				elif tuple(s) in self.opened_hash:
					s = Npuzzle(s, elt.g + 1, setting, elt)
					e = self.opened_hash[tuple(s.content)]
					if s.g < e.g:
						s.parent = e.parent
						s.g = e.g
						s.cost = e.cost
					self.actual_size -= 1
				else:
					s = Npuzzle(s, elt.g + 1, setting, elt)
					self.insert_elt(s)
					self.opened_hash[tuple(s.content)] = s
		return (None)

	def insert_elt(self, s):
		if not self.opened or s.cost > self.opened[-1].cost:
			self.opened.append(s)
		else:
			for i, elt in enumerate(self.opened):
				if s.cost <= elt.cost:
					self.opened.insert(i, s)
					break

	def final(self):
		if self.solution:
			print("Complexity in time:", self.complexity_time)
			print("Complexity in size:", self.complexity_size)
			print("Number of moves:", self.solution.g)
			print("Solution:")
			for step in self.solution.get_path():
				print(tuple(step))
			# for step in self.solution.get_path():
			# 	for i in range(len(step)):
			# 		print('%2s' % step[i], end='')
			# 		print(' ', end='') if i%self.size != self.size-1 else print('')
			# 	print()
		else:
			print("Error : The puzzle is unsolvable")
