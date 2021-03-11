from queue import Queue
from setting import Setting

def main():
	setting = Setting()
	queue = Queue(setting)
	queue.final()

if __name__ == '__main__':
	main()
