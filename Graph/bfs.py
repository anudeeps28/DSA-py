from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Queue for BFS

    while queue:
        node = queue.popleft()  # Dequeue a node from queue
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node] - visited)


if __name__ == "__main__":
    graph = {0: {1, 2}, 1: {2}, 2: {0, 3}, 3: {3}}
    bfs(graph, 2)
