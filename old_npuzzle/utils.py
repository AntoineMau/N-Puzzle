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

# def is_solvable(npuzzle, size):
# 	permutation = 0
# 	index0 = npuzzle.index('0')
# 	parity0 = (int(index0/size) + index0%size) % 2
# 	for i in range(size**2):
# 		if npuzzle[i] != str(i):
# 			swap(npuzzle, i, npuzzle.index(str(i)))
# 			permutation += 1
# 	return permutation%2 == parity0

def is_solvable(npuzzle, size, goal):
	permutation = 0
	index0 = npuzzle.index('0')
	goal0 = goal.index('0')
	parity0 = (abs(index0/size - goal0/size) + abs(index0%size - goal0%size))%2
	for i in range(size**2):
		if npuzzle.index(str(i)) != goal.index(str(i)):
			swap(npuzzle, goal.index(str(i)), npuzzle.index(str(i)))
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

def make_goal(size):
	t_size = size**2
	puzzle = [-1 for i in range(t_size)]
	x, ix, y, iy = 0, 1, 0, 0
	for cur in range(1, t_size):
		puzzle[x + y*size] = cur
		if x + ix == size or x + ix < 0 or (ix != 0 and puzzle[x + ix + y*size] != -1):
			iy, ix = ix, 0
		elif y + iy == size or y + iy < 0 or (iy != 0 and puzzle[x + (y+iy)*size] != -1):
			ix, iy = -iy, 0
		x += ix
		y += iy
		if cur == t_size - 1:
			puzzle[x + y*size] = 0
	return puzzle
