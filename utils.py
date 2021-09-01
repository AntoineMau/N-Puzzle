def error(index_error):
	list_error = {
		'Bad file': 'Error: Bad file',
		'Unsolvable': 'Error: Puzzle is unsolvable',
		'Under size': 'Error: Size must be ≥ 3',
		'Under shuffle': 'Error: Number of shuffle must be ≥ 0',
	}
	print(list_error[index_error])
	exit(0)

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

def swap(data, i1, i2):
	data[i1], data[i2] = data[i2], data[i1]
	return tuple(data)
