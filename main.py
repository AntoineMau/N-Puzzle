from queue import Queue
from setting import Setting
import time

def main():
	t = time.time()
	setting = Setting()
	queue = Queue(setting)
	queue.final()
	print(time.time() - t)

if __name__ == '__main__':
	main()
