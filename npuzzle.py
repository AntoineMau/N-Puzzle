class Npuzzle:
	def __init__(self, content, g, setting, parent):
		self.g = g
		self.h = setting.h(content, setting.goal, setting.size)
		self.cost = setting.cost_f(g, content)
		self.parent = parent
		self.content = content

	def next_move(self, size):
		content = self.content.copy()
		index = content.index(0)
		l = []
		length = 0
		if int(index/size) != 0:
			l.append(self.swap(content.copy(), index, index-size))
			length += 1
		if int(index/size) != size-1:
			l.append(self.swap(content.copy(), index, index+size))
			length += 1
		if index%size != 0:
			l.append(self.swap(content.copy(), index, index-1))
			length += 1
		if index%size != size-1:
			l.append(self.swap(content.copy(), index, index+1))
			length += 1
		return length, l

	def swap(self, content, i1, i2):
		content[i1], content[i2] = content[i2], content[i1]
		return content

	def get_path(self):
		path = list()
		current = self
		while current:
			path.append(current.content)
			current = current.parent
		path.reverse()
		return path
