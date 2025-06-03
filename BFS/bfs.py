# BFS inplementation using recursion
from collections import defaultdict

def bfs_recursive(graph, queue, visited):
    if not queue:
        return
    node = queue.pop(0)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    bfs_recursive(graph, queue, visited)

# Example usage:
if __name__ == "__main__":
    # Sample graph
    graph = defaultdict(list)
    graph[0] = [1, 2]
    graph[1] = [0, 3, 4]
    graph[2] = [0]
    graph[3] = [1]
    graph[4] = [1, 5]
    graph[5] = [4]

    start_node = 0
    visited = set([start_node])
    queue = [start_node]
    print("BFS Traversal (recursive):")
    bfs_recursive(graph, queue, visited)