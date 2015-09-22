import sys
import time
import collections

# initialize each vertex with all possible colors
def initialize_colors(graph):
	colors = dict()
	for vertex in graph:
		colors[vertex] = []

	return colors

def color_graph_recursive(graph, graph_len, vertex_id, possible_colors, used_colors, map_colors, flag):
	if len(map_colors) == graph_len:
		return True

	vertex_key = list(graph.keys())[vertex_id]
	vertex_adjacents = list(graph.values())[vertex_id]

	if flag != 'a':
		this_used_colors = used_colors.copy()
	else:
		this_used_colors = used_colors

	for color in possible_colors:
		#if color in this_used_colors[vertex_key]:
		#	print("Pulou a cor %s de %s" % (color, vertex_key))
		#	continue

		if flag != 'a':
			this_used_colors = used_colors.copy()

		available = True
		for adjacent in vertex_adjacents:
			if map_colors.get(adjacent) == color:
				available = False
				break

		if available == True:
			map_colors[vertex_key] = color

			if flag != 'a':
				this_used_colors[vertex_key].append(color)
				for adjacent in vertex_adjacents:
					this_used_colors[adjacent].append(color)

					if adjacent not in map_colors and len(possible_colors) == len(this_used_colors[adjacent]):
						available = False

			if available == False:
				del map_colors[vertex_key]
				continue

			if color_graph_recursive(graph, graph_len, vertex_id + 1, possible_colors, this_used_colors, map_colors, flag) == True:
				return True
			else:
				del map_colors[vertex_key]

	return False

def color_graph(graph, flag):
	map_colors = dict()

	possible_colors = ['Azul', 'Vermelho', 'Verde', 'Amarelo']
	used_colors = initialize_colors(graph)

	if color_graph_recursive(graph, len(graph), 0, possible_colors, used_colors, map_colors, flag) == True:
		return map_colors
	else:
		return []

flag = input().split(" ")[1].split("\n")[0] # get the flag letter

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

start_time = time.time()
print(color_graph(graph, flag))
elapsed_time = time.time() - start_time
print("Time taken using '%s' flag: %ss" % (flag, elapsed_time))