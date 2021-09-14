from time import time
from utils import make_goal
from queue import Queue
from setting import Setting, choose_heuristic_f, create_cost_f

def main():
	t = time()
	setting = Setting()
	setting.parser()
	setting.goal = tuple(make_goal(setting.size))
	setting.h = choose_heuristic_f(setting.heuristic)
	setting.cost_f = create_cost_f(setting)
	setting.is_solvable()
	queue = Queue(setting)
	queue.solution = queue.opened.pop() if setting.start == setting.goal else queue.solve(setting)
	queue.final(setting.script, time() - t)
	exit(0)

if __name__ == '__main__':
	main()
