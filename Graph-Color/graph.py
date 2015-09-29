import sys
import collections

# Initialize each vertex with all possible colors.
def initialize_colors(graph):
	colors = dict()
	for vertex in graph:
		colors[vertex] = []

	return colors

# Recursive version of the coloring function.
def color_graph_recursive(
		graph, graph_len, possible_colors, used_colors,
		map_colors, attributions, flag='a', vertex_id=0):
	if len(map_colors) == graph_len:
		return True

	my_colored_states = []

	vertex_key = list(graph.keys())[vertex_id]
	vertex_adjacents = list(graph.values())[vertex_id]

	for color in possible_colors:
		available = True

		# Tests the adjacent vertices to see if the current color can
		# be used; if not, break to the next color.
		for adjacent in vertex_adjacents:
			if map_colors.get(adjacent) == color:
				available = False
				break

		if available == True:
			# Color myself to the current color.
			map_colors[vertex_key] = color
			attributions[0] += 1

			if flag != 'a':
				for adjacent in vertex_adjacents:
					if adjacent not in map_colors:
						if color not in used_colors[adjacent]:
							used_colors[adjacent].append(color)
							my_colored_states.append(adjacent)

							# Forward checking heuristic
							if (len(possible_colors) ==
							    	len(used_colors[adjacent])):
								available = False
								break

			if available == False:
				del map_colors[vertex_key]
				continue

			if flag == 'c' or flag == 'd':
				greatest = -1
				candidate = vertex_key  # Only considered when graph
										# is fully colored

				for vertex in graph:
					if (vertex not in map_colors and 
							len(used_colors[vertex]) > greatest):
						greatest = len(used_colors[vertex])
						candidate = vertex

				if flag == 'd':
					mvr = greatest
					greatest = -1
					for vertex in graph:
						if (vertex not in map_colors and
								len(used_colors[vertex]) == mvr and
								len(graph[vertex]) > greatest):
							greatest = len(graph[vertex])
							candidate = vertex

				if greatest != -1:
					next_vertex = list(graph.keys()).index(candidate)
				else:
				 	# Only enters here when the current vertex is the
				 	# last one to be colored. This means it is already
				 	# colored and the result is valid!
					return True
			else:
				next_vertex = vertex_id + 1

			if color_graph_recursive(
					graph, graph_len, possible_colors, used_colors,
					map_colors, attributions, flag, next_vertex):
				return True
			else:
				del map_colors[vertex_key]
				for state in my_colored_states:
					if color in used_colors[state]:
						used_colors[state].remove(color)

	return False

# Non-recursive coloring function that uses the recursive one.
def color_graph(graph, flag='a'):
	map_colors = dict()

	possible_colors = ['Azul', 'Vermelho', 'Verde', 'Amarelo']
	used_colors = initialize_colors(graph)
	attributions = [0]

	if color_graph_recursive(
			graph, len(graph), possible_colors,
			used_colors, map_colors, attributions, flag):
		return (map_colors, attributions)

# Print the resulting colored map in the specified format.
def print_result(colored_map, f=sys.stdout):
	for key, value in colored_map.items():
		print('%s: %s.' % (key, value), file=f)