def error(message):
	list_error = {
		'Bad file': 'Error: Bad file',
		'Unsolvable': 'Error: Puzzle is unsolvable'
	}
	print(list_error[message])
	exit(0)
