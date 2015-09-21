import sys
from graph import Graph

input() # discard first line

graph = Graph()

for line in sys.stdin:
	list = line.split(": ")
	
	src = list[0]
	dsts = list[1].split(", ")

	graph.add_vertex(src)

	for i in range(len(dsts)):
		if i != (len(dsts) - 1):
			graph.add_vertex(dsts[i]) # add a new vertex
			graph.add_edge({src, dsts[i]})
		else:
			graph.add_vertex(dsts[i].split(".\n")[0])
			graph.add_edge({src, dsts[i].split(".\n")[0]})
			
print(graph)