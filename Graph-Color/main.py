import sys
import time
import collections

from graph import color_graph, print_result

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

def initialize_results():
	results = dict()
	flags = ['a', 'b', 'c', 'd']

	for flag in flags:
		results[flag] = []

	return results

def test_performance(graph, n=10):
	# The next blocks of code colors the graph n times with each 
	# flag and counts the total time elapsed and attributions
	results = initialize_results()

	# Using 'a' flag
	attrib = 0
	start_time = time.time()
	for i in range(n):
		attrib += color_graph(graph, 'a')[1][0]
	results['a'].append((time.time() - start_time) / n)
	results['a'].append(attrib / n)

	# Using 'b' flag
	attrib = 0
	start_time = time.time()
	for i in range(n):
		attrib += color_graph(graph, 'b')[1][0]
	results['b'].append((time.time() - start_time) / n)
	results['b'].append(attrib / n)

	# Using 'c' flag
	attrib = 0
	start_time = time.time()
	for i in range(n):
		attrib += color_graph(graph, 'c')[1][0]
	results['c'].append((time.time() - start_time) / n)
	results['c'].append(attrib / n)

	# Using 'd' flag
	attrib = 0
	start_time = time.time()
	for i in range(n):
		attrib += color_graph(graph, 'd')[1][0]
	results['d'].append((time.time() - start_time) / n)
	results['d'].append(attrib / n)

	return results

# Main function
def main(argv=sys.argv):
	# In case of wrong list of arguments.
	if (len(argv) < 3 or len(argv) > 4):
		print('usage: %s input_file output_file [performance_file]' % argv[0])
		print('If performance_file is not specified, performance tests will not be run.')
		return False

	try:
		f = open(argv[1], 'r')  # Try to open the input file
	except OSError as e:
		print(e)
		return False
	else:
		# If successful, generate the graph from the file.
		graph, flag = parse_input(f)
		f.close()

	try:
		f = open(argv[2], 'w')  # Try to open the output file
	except OSError as e:
		print(e)
		return False
	else:
		# If successful, print the resulting colored graph.
		print_result(color_graph(graph, flag)[0], f)
		f.close()

	# If there is one performance file specified,
	# run the performance tests.
	if len(argv) == 4:
		results = test_performance(graph, 50)

		try:
			f = open(argv[3], 'w')
		except OSError as e:
			print(e)
			return False
		else:
			for flag in results:
				print("Results for '%s' flag:" % flag, file=f)
				print("\tAverage time taken to color graph: %.5fs"
					% results.get(flag)[0], file=f)
				print("\tAverage number of attributions: %.0f\n" 
					% results.get(flag)[1], file=f)
			f.close()

	return True

if __name__ == '__main__':
	main()