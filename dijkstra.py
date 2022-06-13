class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printSol(self, dist):
		print("Vertex \t Distance from Source")
		for node in range(self.V):
			print(node, "\t\t", dist[node])


	def minDist(self, dist, sptSet):


		min = 1e7


		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

	def dijkstra_Algo(self, src):

		dist = [1e7] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			u = self.minDist(dist, sptSet)


			sptSet[u] = True


			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]

		self.printSol(dist)

g = Graph(5)
g.graph = [
        [0, 4, 0, 8,  0],
		[4, 0, 8, 11, 0],
		[0, 8, 0, 7,  2],
		[0, 7, 0, 9, 14],
		[0, 0, 9, 0, 10],
		]

g.dijkstra_Algo(0)
