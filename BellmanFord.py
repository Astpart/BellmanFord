class CustomGraph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices  # Total number of vertices in the graph
        self.edges = []  # List to store edges

    # Add an edge
    def add_edge(self, start, end, weight):
        self.edges.append([start, end, weight])

    # Print the solution
    def display_distances(self, distances):
        print("Vertex Distance from Source")
        for i in range(self.num_vertices):
            print("{0}\t\t{1}".format(i, distances[i]))

    def compute_shortest_paths(self, source):
        distances = [float("Inf")] * self.num_vertices
        distances[source] = 0

        for _ in range(self.num_vertices - 1):
            for start, end, weight in self.edges:
                if distances[start] != float("Inf") and distances[start] + weight < distances[end]:
                    distances[end] = distances[start] + weight

        for start, end, weight in self.edges:
            if distances[start] != float("Inf") and distances[start] + weight < distances[end]:
                print("Graph contains a negative weight cycle")
                return

        self.display_distances(distances)

# Create a graph instance and add edges
my_graph = CustomGraph(5)
my_graph.add_edge(0, 1, 2)
my_graph.add_edge(0, 2, 4)
my_graph.add_edge(1, 3, 2)
my_graph.add_edge(2, 4, 3)
my_graph.add_edge(2, 3, 4)
my_graph.add_edge(4, 3, -5)

# Compute shortest paths from vertex 0
my_graph.compute_shortest_paths(0)
