from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.adj_dict = defaultdict(list)

    def add_edge(self, u, v):
        if u in self.adj_dict:
            self.adj_dict[u].append(v)
        else:
            self.adj_dict[u] = [v]

    def dfs(self, start_vertex):
        visited = set()
        self._dfs(start_vertex, visited)

    def _dfs(self, vertex, visited: set):
        visited.add(vertex)

        print(vertex)

        for neighbor in self.adj_dict[vertex]:
            if neighbor not in visited:
                self._dfs(neighbor, visited)


# Example usage
graph = Graph()
graph.add_edge("a", "b")
graph.add_edge("a", "c")
graph.add_edge("b", "d")
graph.add_edge("b", "e")
graph.add_edge("c", "f")
graph.add_edge("e", "g")

graph.dfs("a")
