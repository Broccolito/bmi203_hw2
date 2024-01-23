# write tests for bfs
import pytest
from search import Graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """

    g = Graph('./data/tiny_network.adjlist')
    result = g.bfs('31806696')
    expected_number_of_nodes = 30
    assert len(result) == expected_number_of_nodes
    
    pass

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """

    g = Graph('./data/citation_network.adjlist')
    start_node = 'Franklin Huang'
    end_node = '34912807'
    
    # Test for connected nodes
    path = g.bfs(start_node, end_node)
    assert path is not None
    assert path[0] == start_node
    assert path[-1] == end_node
    
    # Test for non-connected nodes
    non_connected_node = '492357816'  # Replace with an actual node that is not connected
    path = g.bfs(start_node, non_connected_node)
    assert path is None

    pass

def test_bfs_empty_graph():
    g = Graph('./data/empty_network.adjlist')  # Make sure this file represents an empty graph
    result = g.bfs('any_node')
    assert result is None

def test_bfs_nonexistent_start_node():
    g = Graph('./data/tiny_network.adjlist')  # Replace with a file that represents a normal graph
    result = g.bfs('nonexistent_node')
    assert result is None

def test_bfs_nonexistent_end_node():
    g = Graph('./data/tiny_network.adjlist')
    result = g.bfs('31806696', 'nonexistent_node')  # Replace 'start_node' with an actual node
    assert result is None

def test_bfs_unconnected_graph():
    g = Graph('./data/unconnected_network.adjlist')
    result = g.bfs('34916529')
    assert len(result) == 1

# # Example of a test case that is expected to fail and raise an exception
def test_bfs_invalid_file():
    with pytest.raises(Exception):
        Graph('invalid_file.adjlist')