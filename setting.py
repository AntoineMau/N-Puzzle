from re import match, sub, split as rsplit
from math import sqrt
from utils import error
from argparse import ArgumentParser, FileType

def hamming(puzzle, goal, size, total_size):
	heuri = 0
	for i in range(total_size):
		if puzzle[i] != goal[i]:
			heuri += 1
	return heuri

def manhattan(content, goal, size, total_size):
	heuri = 0
	for i in range(total_size):
		obj, sta = goal.index(i), content.index(i)
		objY, staY = obj%size, sta%size
		objX, staX = (obj-objY)/size, (sta-staY)/size
		heuri += abs(objX - staX) + abs(objY - staY)
	return heuri

def euclidean(content, goal, size, total_size):
	heuri = 0
	for i in range(total_size):
		obj, sta = goal.index(i), content.index(i)
		objY, staY = obj%size, sta%size
		objX, staX = (obj-objY)/size, (sta-staY)/size
		heuri += sqrt((objX-staX)**2 + (objY-staY)**2)
	return round(heuri)

def choose_heuristic_f(heuristic):
	f = {
		'hamming': (hamming),
		'manhattan': (manhattan),
		'euclidean': (euclidean)
	}
	return f[heuristic]

def create_cost_f(setting):
	f = {
		'astar': (lambda g, puzzle: g + setting.h(puzzle, setting.goal, setting.size, setting.total_size)),
		'greedy': (lambda g, puzzle: setting.h(puzzle, setting.goal, setting.size, setting.total_size)),
		'uniform': (lambda g, puzzle: g)
	}
	return f[setting.algorithm]

class Setting:
	def __init__(self):
		self.algorithm = str()
		self.heuristic = str()
		self.start = tuple()
		self.size = int()
		self.total_size = int()
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
				self.total_size = self.size**2
				first_line = False
			elif not first_line and match(r'^([ \t]*\d+[ \t]*){%d}$' % self.size, elt):
				self.start += tuple(int(i) for i in rsplit(r'[ \t\n]+', elt.strip()))
			else:
				error("Bad file")
		if self.size == 0 or self.total_size != len(self.start):
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
