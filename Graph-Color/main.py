import sys
import collections

# initialize each vertex with all possible colors
def initialize_colors(graph):
	colors = dict()
	for vertex in graph:
		colors[vertex] = ['Azul', 'Vermelho', 'Verde', 'Amarelo']

	return colors

def backtracking_recursive(graph, graph_len, vertex_id, colors, map_colors,):
	if len(map_colors) == graph_len:
		return True

	vertex_adjacents = list(graph.values())[vertex_id]
	vertex_key = list(graph.keys())[vertex_id]

	for color in colors:
		available = True
		for adjacent in vertex_adjacents:
			if map_colors.get(adjacent) == color:
				available = False

		if available == True:
			map_colors[vertex_key] = color

			if backtracking_recursive(graph, graph_len, vertex_id + 1, colors, map_colors) == True:
				return True
			else:
				del map_colors[vertex_key]

	return False

def backtracking(graph):
	map_colors = dict()
	colors = ['Azul', 'Vermelho', 'Verde', 'Amarelo']

	if backtracking_recursive(graph, len(graph), 0, colors, map_colors) == True:
		return map_colors
	else:
		return []

input() # discard first line

graph = collections.OrderedDict() # initialize the dict representing our graph

for line in sys.stdin:
	elems = line.split(": ")	#
	src = elems[0]			    #
	dsts = elems[1].split(", ") # input parsing

	graph[src] = []

	for i in range(len(dsts)):
		if i != (len(dsts) - 1):
			graph[src].append(dsts[i]) # add a new edge in the graph
		else:
			graph[src].append(dsts[i].split(".\n")[0]) # add a new edge in the graph

colors = initialize_colors(graph)

print(graph)
print(backtracking(graph))