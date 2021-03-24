from re import match, sub, split as rsplit
from utils import error
from argparse import ArgumentParser, FileType
from heuristic import manhattan, hamming, euclidean

class Setting:
	def __init__(self):
		self.algorithm = str()
		self.heuristic = str()
		self.start = tuple()
		self.size = int()
		self.goal = tuple()
		self.parser()
		self.make_goal()
		self.h = self.choose_heuristic_f()
		self.cost_f = self.create_cost_f()
		test = self.is_solvable()
		if not self.is_solvable():
			error("Unsolvable")

	def parser(self):
		parser = ArgumentParser()
		parser.add_argument('-F', '--file', type=FileType('r'), help='N-puzzle file')
		parser.add_argument('-A', '--algorithm', default='astar', choices=['astar', 'greedy', 'uniform'], help='Choise algorithm for N-puzzle. Default: astar')
		parser.add_argument('-H', '--heuristic', default='manhattan', choices=['manhattan', 'hamming', 'euclidean'], help='Choise heuristic for N-puzzle. Default: manhattan')
		args = parser.parse_args()
		self.algorithm = args.algorithm
		self.heuristic = args.heuristic
		f = args.file.read()
		f = sub(r'#.*', '', f)
		first_line = True
		for elt in f.split('\n'):
			if match(r'^[ \t\n]*$', elt):
				pass
			elif first_line and match(r'^\d+$', elt):
				self.size = int(elt)
				first_line = False
			elif not first_line and match(r'^([ \t]*\d+[ \t]*){%d}$' % self.size, elt):
				self.start += tuple(int(i) for i in rsplit(r'[ \t\n]+', elt.strip()))
			else:
				error("Bad file")
		if self.size == 0 or self.size**2 != len(self.start):
			error("Bad file")

	def make_goal(self):
		length = self.size**2
		goal = [-1 for i in range(length)]
		x, ix, y, iy = 0, 1, 0, 0
		for cur in range(1, length):
			goal[x + y*self.size] = cur
			if x+ix == self.size or x+ix < 0 or (ix != 0 and goal[x + ix + y*self.size] != -1):
				iy, ix = ix, 0
			elif y+iy == self.size or y+iy < 0 or (iy != 0 and goal[x + (y+iy)*self.size] != -1):
				ix, iy = -iy, 0
			x += ix
			y += iy
			if cur == length - 1:
				goal[x + y*self.size] = 0
		self.goal = tuple(goal)

	def is_solvable(self):
		start = list(self.start)
		permutation = 0
		index0 = start.index(0)
		goal0 = self.goal.index(0)
		parity0 = abs(int(index0/self.size) - int(goal0/self.size)) + abs(index0%self.size - goal0%self.size)
		for i in range(1, self.size**2):
			i_npuzzle, i_goal = start.index(i), self.goal.index(i)
			if i_npuzzle != i_goal:
				start[i_npuzzle], start[i_goal] = start[i_goal], start[i_npuzzle]
				permutation += 1
		return permutation%2 == parity0%2
	
	def choose_heuristic_f(self):
		f = {
			'hamming': (hamming),
			'manhattan': (manhattan),
			'euclidean': (euclidean)
		}
		return f[self.heuristic]

	def create_cost_f(self):
		f = {
			'astar': (lambda g, puzzle: g + self.h(puzzle, self.goal, self.size)),
			'greedy': (lambda g, puzzle: self.h(puzzle, self.goal, self.size)),
			'uniform': (lambda g, puzzle: g)
		}
		return f[self.algorithm]
