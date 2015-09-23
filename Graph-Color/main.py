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

				if greatest != -1:
					next_vertex = list(graph.keys()).index(candidate)
				else:
				 	# Only enters here when the current vertix is the
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
def color_graph(graph, flag):
	map_colors = dict()

	possible_colors = ['Azul', 'Vermelho', 'Verde', 'Amarelo']
	used_colors = initialize_colors(graph)

	if color_graph_recursive(
			graph, len(graph), possible_colors, used_colors,
			map_colors, flag):
		return map_colors

# Parses the input and creates the graph from it.
def parse_input():
	flag = input().split(" ")[1].split("\n")[0]  # Grab the flag letter

	# Initialize the dict representing our graph.
	graph = collections.OrderedDict()

	for line in sys.stdin:
		elems = line.split(": ")	 # 
		src = elems[0]			     # Separates the vertix
		dsts = elems[1].split(", ")  # from its adjacents.

		graph[src] = []  # Initialize this vertex's adjencency list

		for i in range(len(dsts)):
			if i != (len(dsts) - 1):
				# Add a new edge for this vertix
				graph[src].append(dsts[i])
			else:
				# Add the last edge for this vertix (ends with '\n')
				graph[src].append(dsts[i].split(".\n")[0])

	return (graph, flag)

# Main function
def main():
	graph, flag = parse_input()

	# Colors the graph and counts the total time elapsed for that
	start_time = time.time()
	print(color_graph(graph, flag))
	elapsed_time = time.time() - start_time
	
	print("Time taken using '%s' flag: %ss" % (flag, elapsed_time))

if __name__ == '__main__':
	main()