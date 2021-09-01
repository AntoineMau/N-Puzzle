from re import match, sub, split as rsplit
from utils import error
from argparse import ArgumentParser, FileType

class Setting:
	def __init__(self):
		self.algorithm = str()
		self.heuristic = str()
		self.start = tuple()
		self.size = int()
		self.goal = tuple()
		self.h = None
		self.cost_f = None

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
		if permutation%2 != parity0%2:
			error("Unsolvable")
