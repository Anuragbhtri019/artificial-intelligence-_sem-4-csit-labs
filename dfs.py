class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs(node, target):
    if node is None:
        return False
    if node.value == target:
        return True
    for child in node.children:
        if dfs(child, target):
            return True
    return False

# Ask user for input
root_value = input("Enter the root node value: ")
root = Node(root_value)

nodes = {root_value: root}
current_node = root

while True:
    try:
        num_children = int(input(f"Enter the number of children for node '{current_node.value}': "))
        for _ in range(num_children):
            child_value = input(f"Enter child '{current_node.value}' child value: ")
            if child_value in nodes:
                print("Node value must be unique. Please enter a different value.")
                continue
            child = Node(child_value)
            current_node.children.append(child)
            nodes[child_value] = child
        next_node_value = input("Enter the next node to add (or 'done' if finished): ")
        if next_node_value.lower() == 'done':
            break
        if next_node_value not in nodes:
            print("Node not found. Please enter a valid node value.")
            continue
        current_node = nodes[next_node_value]
    except ValueError:
        print("Invalid input. Please enter a number for the number of children.")

# Ask user for node to find
target_node = input("Enter the node to find: ")

# Perform DFS
if dfs(root, target_node):
    print(f"Node '{target_node}' found in the tree!")
else:
    print(f"Node '{target_node}' not found in the tree!")

# DFS Traversal Order
print("DFS Traversal Order:", end=" ")
def dfs_traversal(node):
    if node is None:
        return
    print(node.value, end=" ")
    for child in node.children:
        dfs_traversal(child)

dfs_traversal(root)
print()  # For a new line after the traversal output