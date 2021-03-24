from math import sqrt

def manhattan(content, goal, size):
	heuri = 0
	for i in range(size ** 2):
		obj = goal.index(i)
		sta = content.index(i)
		objX, objY = int(obj/size), int(obj%size)
		staX, staY = int(sta/size), int(sta%size)
		heuri += abs(objX - staX) + abs(objY - staY)
	return heuri

def hamming(puzzle, goal, size):
	heuri = 0
	for i in range(size ** 2):
		if puzzle[i] != goal[i]:
			heuri += 1
	return heuri

def euclidean(content, goal, size):
	heuri = 0
	for i in range(size ** 2):
		obj = goal.index(i)
		sta = content.index(i)
		objX, objY = int(obj/size), int(obj%size)
		staX, staY = int(sta/size), int(sta%size)
		heuri += sqrt(abs(objX - staX)**2 + abs(objY - staY)**2)
	return round(heuri)
