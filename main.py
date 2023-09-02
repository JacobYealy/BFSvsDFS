import csv
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, from_node, to_node):
        if from_node not in self.adj_list:
            self.adj_list[from_node] = []
        self.adj_list[from_node].append(to_node)


def breadth_first_search(graph, start_value, goal_value):
    start_node = Node(start_value)
    goal_node = Node(goal_value)
    visited = set()
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()

        if current_node.value == goal_node.value:
            path = []
            while current_node:
                path.insert(0, current_node.value)
                current_node = current_node.parent
            return path

        visited.add(current_node.value)

        for neighbor in graph.adj_list.get(current_node.value, []):
            if neighbor not in visited:
                neighbor_node = Node(neighbor)
                neighbor_node.parent = current_node
                queue.append(neighbor_node)
                visited.add(neighbor)

    return None


def depth_first_search(graph, start_value, goal_value):
    start_node = Node(start_value)
    goal_node = Node(goal_value)
    visited = set()
    stack = [start_node]

    while stack:
        current_node = stack.pop()

        if current_node.value == goal_node.value:
            path = []
            while current_node:
                path.insert(0, current_node.value)
                current_node = current_node.parent
            return path

        visited.add(current_node.value)

        for neighbor in reversed(graph.adj_list.get(current_node.value, [])):
            if neighbor not in visited:
                neighbor_node = Node(neighbor)
                neighbor_node.parent = current_node
                stack.append(neighbor_node)
                visited.add(neighbor)

    return None


# Load graph from CSV
graph = Graph()
file_name = input("Please enter the file name and extension: ")

try:
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            graph.add_edge(row[0], row[1])
    print("Loading file…")
except FileNotFoundError:
    print("File not found.")
    exit(1)

# Get start and end nodes
try:
    start_node = input("Start node (1 – 200): ")
    end_node = input("End Node (1 – 200): ")

    if not (1 <= int(start_node) <= 200) or not (1 <= int(end_node) <= 200):
        print("Node ID out of range.")
        exit(1)
except ValueError:
    print("Invalid input. Please enter integers.")
    exit(1)

# Run BFS and DFS
bfs_path = breadth_first_search(graph, start_node, end_node)
dfs_path = depth_first_search(graph, start_node, end_node)

# Output results
if bfs_path:
    print("Breadth-first traversal")
    print(" – ".join(bfs_path))
else:
    print("No path found in Breadth-first traversal.")

if dfs_path:
    print("Depth-first Search")
    print(" – ".join(dfs_path))
else:
    print("No path found in Depth-first Search.")
