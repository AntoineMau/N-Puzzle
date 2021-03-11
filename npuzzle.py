class Npuzzle:
	def __init__(self, content, g, setting, parent):
		self.g = g
		self.h = setting.h(content, setting.goal, setting.size)
		self.cost = setting.cost_f(g, content)
		self.parent = parent
		self.content = content

	def next_move(self, size):
		index = self.content.index(0)
		l = list()
		col, line = index%size, int(index/size)
		if line != 0:
			l.append(self.swap(index, index-size))
		if line != size-1:
			l.append(self.swap(index, index+size))
		if col != 0:
			l.append(self.swap(index, index-1))
		if col != size-1:
			l.append(self.swap(index, index+1))
		return len(l), l

	def swap(self, i1, i2):
		lcontent = list(self.content)
		lcontent[i1], lcontent[i2] = lcontent[i2], lcontent[i1]
		return tuple(lcontent)

	def get_path(self):
		path = list()
		current = self
		while current:
			path.append(current.content)
			current = current.parent
		path.reverse()
		return path
