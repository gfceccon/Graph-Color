import sys
import time
import collections

# initialize each vertex with all possible colors
def initialize_colors(graph):
	colors = dict()
	for vertex in graph:
		colors[vertex] = []

	return colors

# recursive version of the coloring function
def color_graph_recursive(graph, graph_len, vertex_id, possible_colors, used_colors, map_colors, flag):
	if len(map_colors) == graph_len:
		return True

	my_colored_states = []

	vertex_key = list(graph.keys())[vertex_id]
	vertex_adjacents = list(graph.values())[vertex_id]

	for color in possible_colors:
		available = True
		for adjacent in vertex_adjacents:			#
			if map_colors.get(adjacent) == color:	# tests the adjacent vertices to see
				available = False					# if the current color can be used;
				break								# if not, break to the next color

		if available == True: # if the current color is available, keep going
			map_colors[vertex_key] = color # color myself to the current color

			if flag != 'a':
				for adjacent in vertex_adjacents:
					if adjacent not in map_colors:
						if color not in used_colors[adjacent]:
							used_colors[adjacent].append(color)
							my_colored_states.append(adjacent)

							if len(possible_colors) == len(used_colors[adjacent]): # forward checking
								available = False
								break

			if available == False:
				del map_colors[vertex_key]
				continue

			if flag == 'c' or flag == 'd':
				greatest = -1
				candidate = vertex_key # only considered when graph is fully colored

				for vertex in graph:
					if vertex not in map_colors and len(used_colors[vertex]) > greatest:
						greatest = len(used_colors[vertex])
						candidate = vertex

				if greatest != -1:
					next_vertex = list(graph.keys()).index(candidate)
				else: 			# only enters here when the current vertix is the last one to be colored
					return True # this means it is already colored and the result is valid
			else:
				next_vertex = vertex_id + 1

			if color_graph_recursive(graph, graph_len, next_vertex, possible_colors, used_colors, map_colors, flag) == True:
				return True
			else:
				del map_colors[vertex_key]
				for state in my_colored_states:
					if color in used_colors[state]:
						used_colors[state].remove(color)

	return False

# non-recursive coloring function that uses the recursive one
def color_graph(graph, flag):
	map_colors = dict()

	possible_colors = ['Azul', 'Vermelho', 'Verde', 'Amarelo']
	used_colors = initialize_colors(graph)

	if color_graph_recursive(graph, len(graph), 0, possible_colors, used_colors, map_colors, flag) == True:
		return map_colors
	else:
		return []

# this function parses the input and creates the graph from it
def parse_input():
	flag = input().split(" ")[1].split("\n")[0] # get the flag letter

	graph = collections.OrderedDict() # initialize the dict representing our graph

	for line in sys.stdin:
		elems = line.split(": ")	#
		src = elems[0]			    #
		dsts = elems[1].split(", ") # input parsing

		graph[src] = [] # initialize this vertex's adjencency list

		for i in range(len(dsts)):
			if i != (len(dsts) - 1):
				graph[src].append(dsts[i]) # add a new edge in the graph
			else:
				graph[src].append(dsts[i].split(".\n")[0]) # add a new edge in the graph

	return (graph, flag)

graph, flag = parse_input()

start_time = time.time()
print(color_graph(graph, flag))
elapsed_time = time.time() - start_time # count time for color_graph function
print("Time taken using '%s' flag: %ss" % (flag, elapsed_time))