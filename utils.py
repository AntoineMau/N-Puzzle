def error(index_error):
	list_error = {
		'Bad file': 'Error: Bad file',
		'Unsolvable': 'Error: Puzzle is unsolvable',
		'Under size': 'Error: Size must be ≥ 3',
		'Under shuffle': 'Error: Number of shuffle must be ≥ 0',
	}
	print(list_error[index_error])
	exit(1)

def swap(data, i1, i2):
	data[i1], data[i2] = data[i2], data[i1]
	return tuple(data)

def next_move(data, size):
	index = data.index(0)
	l = list()
	col, line = index%size, int(index/size)
	if line != 0:
		l.append(swap(list(data), index, index-size))
	if line != size-1:
		l.append(swap(list(data), index, index+size))
	if col != 0:
		l.append(swap(list(data), index, index-1))
	if col != size-1:
		l.append(swap(list(data), index, index+1))
	return l

def make_goal(size):
	cycle = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}
	total_size = size**2
	goal = [0] * total_size
	x, y, ix, iy = 0, 0, 1, 0
	for i in range(1, total_size):
		if (x+ix == size or y+iy == size or goal[x + ix + (y+iy)*size] != 0):
			ix, iy = cycle[(ix, iy)]
		goal[x + y*size] = i
		x += ix
		y += iy
	return goal
