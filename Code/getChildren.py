
'''
Method called by search algorithms to get the number of children at a state, state

'''

def get_children(maze, state):
	children = []
	if (maze[state[0]-1][state[1]] == 'c'):
		children.append((state[0]-1,state[1])) 
		
	if (maze[state[0]+1][state[1]] == 'c'):
		children.append((state[0]+1,state[1]))

	if (maze[state[0]][state[1]-1] == 'c'):
		children.append((state[0],state[1]-1))

	if (maze[state[0]][state[1]+1] == 'c'):	
		children.append((state[0],state[1]+1))

	return children
