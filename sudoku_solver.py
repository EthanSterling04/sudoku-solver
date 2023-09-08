import common

#helpful, but not needed
class variables:
	counter=0


def updateDomain(Domain, x, y, v, sudoku):
	#remove v from domain of all unassigned var locations that share constraints with x,y
	#Only look at empty cells and immidiate n
	for i in range(9):
		if sudoku[y][i] == 0:
			Domain[y][i][v - 1] = False
			if True not in Domain[y][i]:
				return False
		if sudoku[i][x] == 0:
			Domain[i][x][v - 1] = False
			if True not in Domain[i][x]:
				return False
		if sudoku[int(y/3)*3+int(i/3)][int(x/3)*3+i%3] == 0:
			Domain[int(y/3)*3+int(i/3)][int(x/3)*3+i%3][v - 1] = False
			if True not in Domain[int(y/3)*3+int(i/3)][int(x/3)*3+i%3]:
				return False
	return True

def copyDomain(Domain):
	newDomain = [[[True for v in range(9)] for x in range(9)] for y in range(9)]
	for y in range(9):
		for x in range(9):
			for v in range(9):
				newDomain[y][x][v] = Domain[y][x][v]
	return newDomain


def sudoku_backtracking(sudoku):
	variables.counter = 0
	
	def bt(sudoku):
		variables.counter += 1

		#if complete
		complete = True
		for y in range(9):
			for x in range(9):
				if sudoku[y][x] == 0:
					complete = False
					break
		if complete:
			return True
		
		#Fill in board
		else:
			#find next empty
			for y in range(9):
				for x in range(9):
					if sudoku[y][x] == 0:
						#for every possible value
						for v in range(1, 10):
							if common.can_yx_be_z(sudoku, y, x, v):
								sudoku[y][x] = v
								r = bt(sudoku)
								if r:
									return True
								else:
									sudoku[y][x] = 0
						return False
	
	bt(sudoku)
	return variables.counter



def sudoku_forwardchecking(sudoku):
	variables.counter = 0
	Domain  = [[[True for v in range(9)] for x in range(9)] for y in range(9)]
	for y in range(9):
			for x in range(9):
				for v in range (1, 10):
					if not common.can_yx_be_z(sudoku, y, x, v):
						Domain[y][x][v-1] = False


	def fc(sudoku, Domain):
		variables.counter += 1
		
		#if complete
		complete = True
		for y in range(9):
			for x in range(9):
				if sudoku[y][x] == 0:
					complete = False
					break
		if complete:
			return True
		
		#Fill in board
		else:
			#find next empty
			for y in range(9):
				for x in range(9):
					if sudoku[y][x] == 0:
						#for every possible value
						for v in range(1, 10):
							if common.can_yx_be_z(sudoku, y, x, v):
								oldDomain = copyDomain(Domain)
								sudoku[y][x] = v
								d = updateDomain(Domain, x, y, v, sudoku)
								if d:
									r = fc(sudoku, Domain)
									if r:
										return True
									else:
										sudoku[y][x] = 0
										Domain = copyDomain(oldDomain)
								else:
									sudoku[y][x] = 0
									Domain = copyDomain(oldDomain)
						return False
	
	fc(sudoku, Domain)
	return variables.counter
	
