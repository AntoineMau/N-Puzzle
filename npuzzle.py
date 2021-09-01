class Npuzzle:
	def __init__(self, content, g, setting, parent):
		self.g = g
		self.h = setting.h(content, setting.goal, setting.size)
		self.cost = setting.cost_f(g, content)
		self.parent = parent
		self.content = content

	def get_path(self):
		path = list()
		current = self
		while current:
			path.append(current.content)
			current = current.parent
		path.reverse()
		return path
