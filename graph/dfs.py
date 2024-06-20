# Graph representation using adjacency list
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u in self.adj_list:
            self.adj_list[u].append(v)
        else:
            self.adj_list[u] = [v]

    def dfs(self, start_vertex):
        visited = set()  # Set to keep track of visited vertices
        self._dfs_recursive(start_vertex, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex)  # Do something with the vertex (e.g., print it)

        if vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    self._dfs_recursive(neighbor, visited)


# Example usage
graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("C", "F")
graph.add_edge("E", "G")

graph.dfs("A")
