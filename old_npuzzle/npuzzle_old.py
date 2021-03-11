#!/usr/bin/python3

from time import time
from parse import parse
from utils import swap, errno, is_solvable, place_it
from all_class import Npuzzle, Queue, Algorithm

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

def process(npuzzle, queue, algo):
	if not is_solvable(npuzzle.content.copy(), npuzzle.size):
		errno('unsolvable')
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
					place_it(queue.opened, Npuzzle(e.size, s, e.cost+1, e, algo.exec_algo(s, e.size)))
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
							place_it(queue.opened, s)
	return e

def print_all_step(elem):
	if elem.parent:
		print_all_step(elem.parent)
	print()
	elem.p_matrice()

def print_finish(elem, queue, start_time):
	print_all_step(elem)
	print('step: %d' % elem.cost)
	print('number of elem past by opened: %d' % (len(queue.closed) + len(queue.opened)))
	print("--- %s seconds ---" % (time() - start_time))

if __name__ == "__main__":
	start_time = time()
	algo = Algorithm(goal)
	npuzzle = Npuzzle(*parse(algo))
	queue = Queue(npuzzle)
	e = process(npuzzle, queue, algo)
	print_finish(e, queue, start_time)
	exit(0)
