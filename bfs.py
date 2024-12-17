graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'H'],
    'D': ['G', 'H'],
    'E': ['I'],
    'F': [],
    'G': ['I'],
    'H': [],
    'I': []
}

visited = []
queue = []

def bfs(visited, graph, node, goal):
    visited.append(node)
    queue.append(node)
    result = []

    while queue:
        m = queue.pop(0)
        result.append(m)
        
        if m == goal:
            break
            
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    if goal in result:
        print(f"Following is the Breadth-First Search to goal '{goal}'")
        print("->".join(result))
    else:
        print(f"Goal node '{goal}' is not reachable from the starting node.")

start_node = 'A'
goal_node = input("Enter the goal node for BFS traversal: ")
print(f"Starting BFS from node '{start_node}'...")
bfs(visited, graph, start_node, goal_node)