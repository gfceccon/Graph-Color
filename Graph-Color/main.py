import sys

# initialize each vertex with all possible colors
def initialize_colors(graph):
	colors = dict()
	for vertex in graph:
		colors[vertex] = ['Azul', 'Vermelho', 'Verde', 'Amarelo']

	return colors

def backtracking_recursive(graph, vertex_id, colors, map_colors):
	if vertex_id > len(graph):
		return False

	available = len(colors)

	for color in colors:
		for adjacent in graph[vertex_id]:
			if map_colors.get(adjacent) == color:
				available -= 1
				break

	if available > 0:
		map_colors[vertex_id].append(color)
		if len(map_colors) == len(graph):
			return True
		else:
			backtracking_recursive(graph, vertex_id + 1, colors, map_colors)
	else:
		return False

def backtracking(graph):
	map_colors = dict()
	colors = ['Azul', 'Vermelho', 'Verde', 'Amarelo']

	if backtracking_recursive(graph, 0, colors, map_colors) == True:
		return map_colors
	else:
		return 

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

print(graph)
colors = initialize_colors(graph)

result = backtracking(graph)
if result != False:
	print(result)
