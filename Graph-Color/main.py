import sys

# initialize each vertex with all possible colors
def initialize_colors(graph):
	colors = dict()
	for vertex in graph:
		colors[vertex] = ['Azul', 'Vermelho', 'Verde', 'Amarelo']

	return colors

def backtracking_recursive(graph, colors, map_colors):
	if len(map_colors) == len(graph):
		return True

	for vertex in graph:
		if vertex not in map_colors:
			break

	for color in colors:
		available = True
		for adjacent in graph[vertex]:
			if map_colors.get(adjacent) == color:
				available = False

		if available == True:
			map_colors[vertex] = color

			if backtracking_recursive(graph, colors, map_colors) == True:
				return True
			else:
				del map_colors[vertex]

	return False

def backtracking(graph):
	map_colors = dict()
	colors = ['Azul', 'Vermelho', 'Verde', 'Amarelo']

	if backtracking_recursive(graph, colors, map_colors) == True:
		return map_colors
	else:
		return []

input() # discard first line

graph = dict() # initialize the dict representing our graph

for line in sys.stdin:
	list = line.split(": ")	   #
	src = list[0]			   #
	dsts = list[1].split(", ") # input parsing

	graph[src] = []

	for i in range(len(dsts)):
		if i != (len(dsts) - 1):
			graph[src].append(dsts[i]) # add a new edge in the graph
		else:
			graph[src].append(dsts[i].split(".\n")[0]) # add a new edge in the graph

colors = initialize_colors(graph)

print(graph)
print('\n')
print(backtracking(graph))