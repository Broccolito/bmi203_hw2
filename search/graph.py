import networkx as nx
from collections import deque

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        In this implementation:

        * The graph is checked for emptiness at the beginning.
        * The existence of the start and end nodes in the graph is verified.
        * A breadth-first search is performed using a queue.
        * If an end node is provided, the algorithm keeps track of paths to each node and returns the path to the end node if found.
        * If no end node is provided, it returns the list of visited nodes in BFS order.
        * If a path to the end node does not exist, it returns None.
        """

        # Check if the graph is empty
        if not self.graph:
            return None

        # Check if the start node exists in the graph
        if start not in self.graph:
            return None

        # Check if the end node is provided and does not exist in the graph
        if end is not None and end not in self.graph:
            return None

        # Initialize variables
        visited = set()
        queue = deque([start])

        # Dictionary for storing paths
        paths = {start: [start]}

        while queue:
            node = queue.popleft()
            visited.add(node)

            # If end node is found
            if node == end:
                return paths[node]

            for neighbor in self.graph.neighbors(node):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    paths[neighbor] = paths[node] + [neighbor]

        # If end is None, return the BFS traversal order
        if end is None:
            return list(visited)

        # If no path to end exists
        return None

# g = Graph('tiny_network.adjlist')
# result = g.bfs('start_node') 
# print(result)