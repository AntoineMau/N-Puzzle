from argparse import ArgumentParser
from random import shuffle
from utils import swap, is_solvable

def parse():
	parser = ArgumentParser()
	parser.add_argument('size', type=int, default=3, help='N-puzzle size. Must be ≥ 3')
	parser.add_argument('-u', '--unsolvable', action='store_true', default=False, help='Generation an unsolvable puzzle')
	return(parser.parse_args())

def make_npuzzle(args):
	npuzzle = [str(i) for i in range(args.size**2)]
	while 1:
		shuffle(npuzzle)
		if is_solvable(npuzzle.copy(), args.size) != args.unsolvable:
			break
	return npuzzle

if __name__ == '__main__':
	args = parse()
	content = make_npuzzle(args)
	print ('# This puzzle is %s' % ('unsolvable' if args.unsolvable else 'solvable'))
	print ('%d' % args.size)
	for i in range(args.size**2):
		print('%s' % content[i], end='')
		print(' ', end='') if i%args.size != args.size-1 else print('')
	exit(1)
