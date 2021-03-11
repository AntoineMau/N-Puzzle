def hamming(puzzle, goal, size):
	count = -1
	for i, j in zip(puzzle, goal):
		if i != j:
			count += 1
	return (count)

def manhattan(content, goal, size):
	heuri = 0
	for i in range(size ** 2):
		sta = content.index(i)
		obj = goal.index(i)
		objX, objY = int(obj/size), int(obj%size)
		staX, staY = int(sta/size), int(sta%size)
		heuri += abs(objX - staX) + abs(objY - staY)
	return heuri
