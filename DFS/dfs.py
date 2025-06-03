# write a program for DFS using recursion in python
from collections import defaultdict

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example usage:
if __name__ == "__main__":
    # Sample graph as adjacency list
    graph = defaultdict(list)
    graph[0] = [1, 2]
    graph[1] = [0, 3, 4]
    graph[2] = [0]
    graph[3] = [1]
    graph[4] = [1, 5]
    graph[5] = [4]

    print("DFS Traversal (recursive) starting from node 0:")
    dfs_recursive(graph, 0)