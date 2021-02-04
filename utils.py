from re import match, sub, split as rsplit
from argparse import ArgumentParser, FileType

def errno(error, detail = None):
	msg_error = {
		'bad file': 'Error: bad file for N-Puzzle.'
	}
	print(msg_error[error])
	exit(1)

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
		elif not first_line and match(r'^([ \t]*\d+[ \t]*){%d}$' % size, elt):
			content += rsplit(r'[ \t\n]+', elt.strip())
		else:
			errno('bad file', elt)
	if size*size != len(content):
		errno('bad file', elt)
	return size, content
