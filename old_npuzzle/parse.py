from re import match, sub, split as rsplit
from utils import errno
from argparse import ArgumentParser, FileType

def parse_option():
	parser = ArgumentParser()
	parser.add_argument('file', type=FileType('r'), help='N-puzzle file')
	parser.add_argument('--algo', default='0', type=int, choices=[0, 1, 2], help='Choise algorithm for N-puzzle. 0: Manhattan | 1: weighted A* | 2: euclidian')
	return parser.parse_args()

def parse(algo):
	args = parse_option()
	algo.set_algo(args.algo)
	f = args.file.read()
	f = sub(r'#.*', '', f)
	first_line = True
	content = []
	size = 0
	for elt in f.split('\n'):
		if match(r'^[ \t\n]*$', elt):
			pass
		elif first_line and match(r'^\d+$', elt):
			size = int(elt)
			first_line = False
		elif not first_line and match(r'^([ \t]*\d+[ \t]*){%d}$' % size, elt):
			content += rsplit(r'[ \t\n]+', elt.strip())
		else:
			errno('bad file', elt)
	if size == 0 or size*size != len(content):
		errno('bad file', elt)
	return size, content, 0, None, algo.exec_algo(content, size)
