from re import match, sub, split as rsplit
from argparse import ArgumentParser, FileType

def errno(error, detail = None):
	msg_error = {
		'bad file': 'Error: bad file for N-Puzzle.'
	}
	print(msg_error[error])
	exit(1)


class Npuzzle:
	def __init__(self, size, content):
		self.size = size
		self.content = content
	def __str__(self):
		return 'N-Puzzle\nSize: %d\n\nContent:%s' % (self.size, self.content)

def parse_option():
	parser = ArgumentParser()
	parser.add_argument('file', type=FileType('r'), help='N-puzzle file')
	return parser.parse_args()

def parse():
	args = parse_option()
	f = args.file.read()
	f = sub(r'#.*', '', f)
	first_line = True
	content = []
	for elt in f.split('\n'):
		if match(r'^[ \t\n]*$', elt):
			pass
		elif first_line and match(r'^\d+$', elt):
			size = int(elt)
			first_line = False
		elif not first_line and match(r'^(\d+[ \t\n]*){4}$', elt):
			content += rsplit(r'[ \t\n]+', elt)
		else:
			print(size)
			print('|%s|' % elt)
			errno('bad file', elt)
	print(content)
	npuzzle = Npuzzle(size, content)
	return npuzzle
