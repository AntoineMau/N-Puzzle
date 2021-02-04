#!/usr/bin/python3

from utils import parse

class Npuzzle:
	def __init__(self, size, content):
		self.size = size
		self.content = content

	def __str__(self):
		return 'N-Puzzle\nSize: %d\nContent: %s' % (self.size, self.content)

	def pprint(self):
		print('N-Puzzle')
		print('Size: %d' % self.size)
		for i in range(len(self.content)):
			print('%s' % self.content[i], end='')
			print(' ', end='') if i % self.size != self.size - 1 else print('')

class Node:
	def __init__(self, cost, parent, npuzzle, heuristique):
		self.cost = cost
		self.parent = parent
		self.npuzzle = npuzzle
		self.heuristique = heuristique

class Queue:
	def __init__(self, depart):
		self.closedList = []
		self.openList = [depart]

def process(npuzzle):
	node = Node(0, None, npuzzle, 0)
	queue = Queue(npuzzle.content)
	while Queue.openList:
		pass
	pass

if __name__ == "__main__":
	npuzzle = Npuzzle(*parse())
	npuzzle.pprint()
	process(npuzzle)
	exit(0)
