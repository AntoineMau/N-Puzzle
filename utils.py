from re import match, sub, split as rsplit
from argparse import ArgumentParser, FileType

def errno(error, detail = None):
	msg_error = {
		'bad file': 'Error: bad file for N-Puzzle.',
		'unsolvable': 'Error: N-Puzzle is unsolvable.',
	}
	print(msg_error[error])
	exit(1)

def parse_option():
	parser = ArgumentParser()
	parser.add_argument('file', type=FileType('r'), help='N-puzzle file')
	return parser.parse_args()

def swap(content, i1, i2):
	content[i1], content[i2] = content[i2], content[i1]
	return content

def exec_heuri(content, size):
	heuri = 0
	for i in range(size ** 2):
		sta = content.index(str(i))
		objX, objY = int(i/size), int(i%size)
		staX, staY = int(sta/size), int(sta%size)
		heuri += abs(objX - staX) + abs(objY - staY)
	return heuri

def is_solvable(npuzzle, size):
	permutation = 0
	index0 = npuzzle.index('0')
	parity0 = (int(index0/size) + index0%size) % 2
	for i in range(size**2):
		if npuzzle[i] != str(i):
			swap(npuzzle, i, npuzzle.index(str(i)))
			permutation += 1
	return permutation%2 == parity0

def parse():
	args = parse_option()
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
	return size, content, 0, None, exec_heuri(content, size)
