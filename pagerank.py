
class Graph:

	def __init__(self, num_nodes):
		self.num_nodes = num_nodes
		self.mapping = {k:i for i, k in enumerate(list('ABCDEFGHI'))}
		self.incoming_data = {k:[] for k in range(num_nodes)}
		self.outgoing_data = {k:[] for k in range(num_nodes)}
		self.graph = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

	def add_edge(self, u, v):
		u = self.mapping[u]
		v = self.mapping[v]

		self.outgoing_data[u].append(v) #  += 1
		self.incoming_data[v].append(u) # += 1
		self.graph[u][v] = 1

	def get_graph(self):
		return self.graph

def page_rank(graph, damping_factor=0.85, max_iters=20):
	df = damping_factor
	num_nodes = graph.num_nodes

	pr = {k: 1 for k in range(num_nodes)}

	for _ in range(max_iters):

		for page in pr.keys():
			val = 0

			for node in graph.incoming_data[page]:
				x = pr[node] / len(graph.outgoing_data[node])
				val += x

			pr[page] = (((1 - df)) + (df * val))

	return pr


if __name__ == '__main__':

	num_nodes = 9
	graph = Graph(num_nodes)
	graph.add_edge('A', 'D')
	graph.add_edge('A', 'B')
	graph.add_edge('B', 'D')
	graph.add_edge('C', 'D')
	graph.add_edge('E', 'D')
	graph.add_edge('F', 'D')
	graph.add_edge('G', 'D')
	graph.add_edge('H', 'E')
	graph.add_edge('I', 'C')

	pr = page_rank(graph, damping_factor=0.85, max_iters=20)
	mapping = {i:k for i, k in enumerate(list('ABCDEFGHI'))}

	print('Iterations: 20')
	print('Node\tPageRank')
	for node in pr.keys():
		print(mapping[node], '\t', round(pr[node], 3))
		# print('Page Rank for node %s is %.4f' % (mapping[node], pr[node]))

	print('\nScaled results:')
	print('Iterations: 20')
	print('Node\tPageRank')
	for node in pr.keys():
		print(mapping[node], '\t', round(pr[node]*38, 2))

