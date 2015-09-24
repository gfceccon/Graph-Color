import sys
import time
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
		map_colors, flag='a', vertex_id=0):
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
						if(vertex not in map_colors and len(used_colors[vertex]) == mvr):
							if(len(graph[vertex]) > greatest):
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
					graph, graph_len, possible_colors,
					used_colors, map_colors, flag, next_vertex):
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

	if color_graph_recursive(
			graph, len(graph), possible_colors, used_colors,
			map_colors, flag):
		return map_colors

# Parse the input and create the graph from it.
def parse_input(f=sys.stdin):
	# Grab the flag letter
	flag = f.readline().split(" ")[1].split("\n")[0]

	# Initialize the dict representing our graph.
	graph = collections.OrderedDict()

	for line in f:
		elems = line.split(": ")	 # 
		src = elems[0]			     # Separates the vertex
		dsts = elems[1].split(", ")  # from its adjacents.

		graph[src] = []  # Initialize this vertex's adjencency list

		for i in range(len(dsts)):
			if i != (len(dsts) - 1):
				# Add a new edge for this vertex
				graph[src].append(dsts[i])
			else:
				# Add the last edge for this vertex (ends with '\n')
				graph[src].append(dsts[i].split(".\n")[0])

	return (graph, flag)

# Print the resulting colored map in the specified format.
def print_result(colored_map, f=sys.stdout):
	for key, value in colored_map.items():
		print('%s: %s.' % (key, value), file=f)

# Main function
def main(argv=sys.argv):
	# In case of wrong list of arguments.
	if len(argv) != 3:
		print('usage: %s input_file output_file' % argv[0])
		return False

	# Open the input file and generate the graph from it.
	try:
		f = open(argv[1], 'r')
		graph, flag = parse_input(f)
		f.close()
	except OSError as e:
		print(e)
		return False

	# Open the output file, color the graph and count the total time.
	try:
		f = open(argv[2], 'w')
		start_time = time.time()
		print_result(color_graph(graph, flag), f)
		elapsed_time = time.time() - start_time
		f.close()
	except OSError as e:
		print(e)
		return False

	print("Time taken to color '%s' using '%s' flag: %.5fs" % 
			(argv[1], flag, elapsed_time))
	return True

if __name__ == '__main__':
	main()