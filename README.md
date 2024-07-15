# Bellman-Ford Algorithm for Finding Shortest Paths in a Graph

This Python script implements the Bellman-Ford algorithm for finding the shortest paths from a source vertex to all other vertices in a graph. The Bellman-Ford algorithm can handle graphs with negative weight edges but detects negative weight cycles.

## Description

The Bellman-Ford algorithm initializes distances from the source vertex to all other vertices as infinity and then iteratively relaxes these distances by considering all edges. It iterates \( |V| - 1 \) times, where \( |V| \) is the number of vertices in the graph, to ensure convergence. After that, it performs one additional pass to check for negative weight cycles.

## CustomGraph Class

The `CustomGraph` class provides methods to add edges to the graph, compute shortest paths using the Bellman-Ford algorithm from a specified source vertex, and display distances from the source vertex.

### Methods

- `__init__(self, num_vertices)`: Initializes a graph instance with a specified number of vertices.
- `add_edge(self, start, end, weight)`: Adds a directed edge from vertex `start` to vertex `end` with the specified `weight`.
- `display_distances(self, distances)`: Prints the distances of all vertices from the source vertex.
- `compute_shortest_paths(self, source)`: Computes the shortest paths from the `source` vertex using the Bellman-Ford algorithm.

### Example Usage

```python
class CustomGraph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []

    def add_edge(self, start, end, weight):
        self.edges.append([start, end, weight])

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

# Compute shortest paths from vertex 0 using Bellman-Ford algorithm
my_graph.compute_shortest_paths(0)
