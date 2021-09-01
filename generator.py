from utils import error, next_move, make_goal
from random import choice
from argparse import ArgumentParser

class Generator:
	def __init__(self):
		self.size = int()
		self.solvable = bool()
		self.shuffle = int()
		self.goal = list()

	def parser(self):
		parser = ArgumentParser()
		parser.add_argument('size', type=int, default=3, help='N-puzzle size. Must be ≥ 3')
		parser.add_argument('-u', '--unsolvable', action='store_false', default=True, help='Generation an unsolvable puzzle')
		parser.add_argument('-s', '--shuffle', type=int, default=100, help='Number of shuffle')
		args = parser.parse_args()
		if args.size < 3 or args.shuffle < 0:
			error('Under size')
		if args.shuffle < 0:
			error('Under shuffle')
		self.size = args.size
		self.solvable = args.unsolvable
		self.shuffle = args.shuffle

	def make_shuffle(self):
		for i in range(self.shuffle):
			tab = next_move(self.goal, self.size)
			self.goal = choice(tab)

	def pprint(self):
		print('# This puzzle is ' + ('solvable' if self.solvable else 'unsolvable'))
		print(self.size)
		for i in range(len(self.goal)):
			print('%d' % self.goal[i], end=(' ' if i%self.size != self.size-1 else '\n'))

def main():
	generator = Generator()
	generator.parser()
	generator.goal = make_goal(generator.size)
	generator.make_shuffle()
	generator.pprint()

if __name__ == '__main__':
	main()
