#!/usr/bin/python3

from utils import *
import time

class Npuzzle:
	def __init__(self, size, content, cost, parent, heuri):
		self.size = size
		self.cost = cost
		self.heuri = heuri
		self.parent = parent
		self.content = content

	def __str__(self):
		return 'N-Puzzle\nSize: %d\nContent: %s' % (self.size, self.content)

	def pprint(self):
		print('Cost: %d | Heuri: %d | C + H: %d' % (self.cost, self.heuri, self.cost+self.heuri))
		for i in range(len(self.content)):
			print('%s' % self.content[i], end='')
			print(' ', end='') if i%self.size != self.size-1 else print('')

class Queue:
	def __init__(self, npuzzle_start):
		self.closed = []
		self.opened = [npuzzle_start]

def p_matrice(content, size):
	for i in range(len(content)):
		print('%s' % content[i], end='')
		print(' ', end='') if i%size != size-1 else print('')
	print()

def expand(size, content):
	index = content.index('0')
	l = []
	if int(index/size) != 0:
		l.append(swap(content.copy(), index, index-size))
	if int(index/size) != size-1:
		l.append(swap(content.copy(), index, index+size))
	if int(index%size) != 0:
		l.append(swap(content.copy(), index, index-1))
	if int(index%size) != size-1:
		l.append(swap(content.copy(), index, index+1))
	return l

def process(npuzzle):
	if not is_solvable(npuzzle.content.copy(), npuzzle.size):
		errno('unsolvable')
	queue = Queue(npuzzle)
	finish = [str(i) for i in range(npuzzle.size ** 2)]
	while queue.opened:
		e = queue.opened[0]
		if e.content == finish:
			break
		else:
			queue.opened.pop(0)
			queue.closed.append(e)
			for s in expand(e.size, e.content):
				open_content = [elt.content for elt in queue.opened]
				close_content = [elt.content for elt in queue.closed]
				if s not in open_content and s not in close_content:
					queue.opened.append(Npuzzle(e.size, s, e.cost+1, e, exec_heuri(s, e.size)))
					queue.opened.sort(key=lambda x: x.cost+x.heuri)
				else:
					if s in open_content:
						closed = False
						s = queue.opened[open_content.index(s)]
					else:
						closed = True
						s = queue.closed[close_content.index(s)]
					if s.cost > e.cost + 1:
						s.cost = e.cost + 1
						s.parent = e
						if closed:
							queue.closed.remove(s)
							queue.opened.append(s)
							queue.opened.sort(key=lambda x: x.cost+x.heuri)
	return e

def print_finish(elem):
	if elem.parent:
		print_finish(elem.parent)
	print()
	for i in range(len(elem.content)):
		print('%s' % elem.content[i], end='')
		print(' ', end='') if i%elem.size != elem.size-1 else print('')

if __name__ == "__main__":
	start_time = time.time()

	npuzzle = Npuzzle(*parse())
	e = process(npuzzle)
	print_finish(e)
	print('step: %d' % e.cost)

	print("--- %s seconds ---" % (time.time() - start_time))
	exit(0)
