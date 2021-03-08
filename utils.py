def errno(error, detail = None):
	msg_error = {
		'bad file': 'Error: bad file for N-Puzzle.',
		'unsolvable': 'Error: N-Puzzle is unsolvable.',
	}
	print(msg_error[error])
	exit(0)

def swap(content, i1, i2):
	content[i1], content[i2] = content[i2], content[i1]
	return content

def is_solvable(npuzzle, size):
	permutation = 0
	index0 = npuzzle.index('0')
	parity0 = (int(index0/size) + index0%size) % 2
	for i in range(size**2):
		if npuzzle[i] != str(i):
			swap(npuzzle, i, npuzzle.index(str(i)))
			permutation += 1
	return permutation%2 == parity0

def place_it(opened, s):
	insert = False
	for i, elt in enumerate(opened):
		if elt.heuri + elt.cost >= s.heuri + s.cost:
			opened.insert(i, s)
			insert = True
			break
	if not insert:
		opened.append(s)
