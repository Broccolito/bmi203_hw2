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

        """
        ### Method Description:

        Initial Checks:

        Check if the graph (self.graph) is empty. If it is, return None.
        Check if the start node exists in the graph. If not, return None.
        If the end node is provided, check if it exists in the graph. If it does not, return None.
        Initialization:

        Initialize a set visited to keep track of visited nodes.
        Initialize a queue queue and enqueue the start node.
        Create a dictionary paths to store paths from the start node to each node. Initialize it with the start node path as [start].

        BFS Traversal:

        While the queue is not empty:
        Dequeue a node from the queue and call it node.
        Add node to the visited set.
        If the node is the end node, return the path from start to end as found in paths.
        Iterate over each neighbor of node:
        If a neighbor is neither in the visited set nor in the queue, enqueue it and update its path in paths as the path to the current node plus the neighbor itself.

        Return Results:

        If end is None (not provided), return the list of nodes in the order they were visited.
        If no path to the end node was found (meaning the loop ended without returning), return None.
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

