#!/usr/bin/python3

from time import time
from utils import make_goal
from queue import Queue
from setting import Setting, choose_heuristic_f, create_cost_f

def main():
	setting = Setting()
	setting.parser()
	setting.goal = tuple(make_goal(setting.size))
	setting.h = choose_heuristic_f(setting.heuristic)
	setting.cost_f = create_cost_f(setting)
	setting.is_solvable()
	queue = Queue(setting)
	if setting.start == setting.goal:
		queue.solution = queue.opened.pop()
	else:
		queue.solution = queue.solve(setting)
	queue.final()

if __name__ == '__main__':
	t = time()
	main()
	print(time() - t)
