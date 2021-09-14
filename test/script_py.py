from os import system, popen
from argparse import ArgumentParser
from statistics import mean
import matplotlib.pyplot as plt

class Setting:
	def __init__(self):
		self.size = int()
		self.file_number = int()
		self.iteration = int()
		self.graph = bool()

	def parser(self):
		parser = ArgumentParser()
		parser.add_argument('file_number', type=int, help='Number of N-Puzzle created.')
		parser.add_argument('-s', '--size', type=int, default=3, help='N-Puzzle size.')
		parser.add_argument("-g", "--graph", action="store_true", default=False, help="Show graph.")
		args = parser.parse_args()
		self.size = args.size
		self.file_number = args.file_number
		self.graph = args.graph
		if self.size < 3:
			self.error('size')
		if self.file_number < 1:
			self.error('file_number')

	def error(self, type):
		tab = {
			'size': 'Error: N-Puzzle size must be greater then 2.',
			'file_number': 'Error: Iteration must be greater then 0.'
		}
		print(tab[type])
		exit(1)

class Process:
	def __init__(self, setting):
		self.size = setting.size
		self.graph = setting.graph
		self.names = list()
		self.iteration = setting.iteration
		self.file_number = setting.file_number
		self.algorithm = ['astar', 'greedy', 'uniform']
		self.heuristic = ['manhattan', 'hamming', 'euclidean']
		self.tab_algo = {'title': list(), 'data': list(), 'labels': ['Heuristic', 'Complex Time', 'Complex Size', 'Nb Mouve', 'Time']}
		self.tab_heuri = {'title': list(), 'data': list(), 'labels': ['Algorithm', 'Complex Time', 'Complex Size', 'Nb Mouve', 'Time']}

	def make_name(self):
		lenght = len(str(self.file_number))
		self.names = [f'npuzzle-{self.size}-{i:>0{lenght}d}.txt' for i in range(1, self.file_number + 1)]

	def make_npuzzle(self):
		for j, name in enumerate(self.names):
			self.progress_bar(j, self.file_number, 'generating', '')
			system(f'python3 ../generator.py -s 1000 {self.size} > {name}')
		self.progress_bar(1, 1, 'generating')

	def make_solution(self):
		i = int()
		result = dict()
		total = self.file_number*len(self.algorithm) * len(self.heuristic)
		for name in self.names:
			for algo in self.algorithm:
				result[algo] = dict()
				for heuri in self.heuristic:
					self.progress_bar(i, total, f'{name} {algo} {heuri}','')
					i += 1
					output = popen(f'python3 ../main.py -S {name} -A {algo} -H {heuri}').read().split(' ')
					result[algo][heuri] = {'complexity_time': list(), 'complexity_size': list(), 'nb_mouves': list(), 'time': list()}
					result[algo][heuri]['complexity_time'].append(int(output[0]))
					result[algo][heuri]['complexity_size'].append(int(output[1]))
					result[algo][heuri]['nb_mouves'].append(int(output[2]))
					result[algo][heuri]['time'].append(float(output[3]))
		self.progress_bar(i, total, f'{name} {algo} {heuri}')
		for i, algo in enumerate(self.algorithm):
			self.tab_algo['title'].append(algo)
			self.tab_algo['data'].append(list())
			for j, heuri in enumerate(self.heuristic):
				self.tab_algo['data'][i].append([heuri])
				for elt in result[algo][heuri]:
					self.tab_algo['data'][i][j].append(round(mean(result[algo][heuri][elt]), 5))
		for i, heuri in enumerate(self.heuristic):
			self.tab_heuri['title'].append(heuri)
			self.tab_heuri['data'].append(list())
			for j, algo in enumerate(self.algorithm):
				self.tab_heuri['data'][i].append([algo])
				for elt in [result[algo][heuri][elt] for elt in result[algo][heuri]]:
					self.tab_heuri['data'][i][j].append(round(mean(elt), 5))

	def progress_bar(self, done, total, name, end_car='\n'):
		print('\r', f'{name:34s}: {done/total*100:3.0f}%' , sep='', end=end_car, flush=True)

	def pprint(self):
		if self.graph:
			self.exec_graph(self.tab_algo)
			self.exec_graph(self.tab_heuri)
		else:
			print('Coucou, dsl pas de graph')

	def exec_graph(self, tab):
		ax = list()
		for i in range(3):
			ax.append(plt.subplots(1,1)[1])
		for i, elt in enumerate(ax):
			elt.axis('tight')
			elt.axis('off')
			the_table = elt.table(cellText=tab['data'][i],colLabels=tab['labels'],loc="center")
			elt.set_title(tab['title'][i])
		plt.show()

def main():
	setting = Setting()
	setting.parser()
	process = Process(setting)
	process.make_name()
	process.make_npuzzle()
	process.make_solution()
	process.pprint()
	exit(0)

if __name__ == '__main__':
	main()
