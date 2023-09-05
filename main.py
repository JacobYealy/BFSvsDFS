import csv
from collections import deque

# =============================================================================
# main.py
# Jacob Yealy
# Artificial Intelligence
#
# Description:
# This file takes an input CSV from the local directory and uses its contents
# to determine if a DFS or BFS algorithm can find the path from the start node
# to the end node.
#
# =============================================================================

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None # for backtrack

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, from_node, to_node):
        if from_node not in self.adj_list:
            self.adj_list[from_node] = []
        self.adj_list[from_node].append(to_node)

def breadth_first_search(graph, start_value, goal_value):
    """
        Perform Breadth-First Search (BFS) to find the shortest path from the start node to the goal node.

        Parameters:
        - graph: a Graph object that describes the layout of nodes and edges.
        - start_value: the value of the node from where the search starts.
        - goal_value: the value of the node where the search ends.

        Returns:
        - A list representing the shortest path from start_value to goal_value, or None if no path exists.
        """
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
    """
        Perform Depth-First Search (DFS) to find a path from the start node to the goal node.

        Parameters:
        - graph: a Graph object that describes the layout of nodes and edges.
        - start_value: the value of the node from where the search starts.
        - goal_value: the value of the node where the search ends.

        Returns:
        - A list representing a path from start_value to goal_value found by DFS, or None if no path exists.
        """
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

def load_graph_from_csv(file_name):
    """
        Load a graph from a CSV file and return it as a Graph object.

        Parameters:
        - file_name (str): The name of the CSV file containing the graph data.
                           The file should be formatted with each row representing an edge.
                           The first entry of each row is the 'from' node and next entries are to nodes.

        Returns:
        - Graph: A Graph object representing the loaded graph.

        Exceptions:
        - FileNotFoundError: If the specified file does not exist, a message is printed and the program exits.
        """
    graph = Graph()
    try:
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                from_node = row[0]
                to_nodes = [node for node in row[1:] if node]
                for to_node in to_nodes:
                    graph.add_edge(from_node, to_node)
        print("Loading file…")
        return graph
    except FileNotFoundError:
        print("File not found.")
        exit(1)


if __name__ == "__main__":
    file_name = input("Please enter a local csv file: ")
    graph = load_graph_from_csv(file_name)

    # Filter out non-integer keys from the adjacency list
    valid_keys = [node for node in graph.adj_list.keys() if node.isnumeric()]

    min_node = min(int(node) for node in valid_keys)
    max_node = max(int(node) for node in valid_keys)

    try:
        start_node = input(f"Start node ({min_node} – {max_node}): ")
        end_node = input(f"End Node ({min_node} – {max_node}): ")

        if not (min_node <= int(start_node) <= max_node) or not (min_node <= int(end_node) <= max_node):
            print("Node out of range.")
            exit(1)
    except ValueError:
        print(f"Invalid input. Please enter integers from {min_node} - {max_node}.")
        exit(1)


    bfs_path = breadth_first_search(graph, start_node, end_node)
    dfs_path = depth_first_search(graph, start_node, end_node)

    if bfs_path:
        print("BFS:")
        print(" – ".join(bfs_path))
    else:
        print("No path found in Breadth first search.")

    if dfs_path:
        print("DFS:")
        print(" – ".join(dfs_path))
    else:
        print("No path found in Depth-first search.")
