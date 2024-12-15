from queue import Queue

def bfs(graph, start):
    visited = []  # To keep track of visited nodes
    queue = Queue()  # Queue for BFS
    bfs_order = []  # To store the order of traversal

    # Start with the starting node
    queue.put(start)
    visited.append(start)

    while not queue.empty():
        current = queue.get()  # Dequeue a node
        bfs_order.append(current)

        # Explore all unvisited neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.put(neighbor)

    return bfs_order

# Example Usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
print("BFS Traversal Order:", bfs(graph, start_node))
