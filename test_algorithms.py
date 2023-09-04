from main import breadth_first_search
from main import depth_first_search
import unittest
from main import load_graph_from_csv

# =============================================================================
# TestBFS
# Jacob Yealy
#
# Description:
# This class contains unit tests for the BFS algorithm.
# It tests paths that exist,
# the same start and end nodes, and invalid start nodes.
#
# Each test case is tested using the local 'BFS_DFS.csv' file.
# =============================================================================
class TestBFS(unittest.TestCase):

    def test_bfs_path_exists(self):
        graph = load_graph_from_csv('BFS_DFS.csv')
        start_node = '124'
        end_node = '56'
        expected_path = ['124', '88', '38', '97', '10', '56']
        result = breadth_first_search(graph, start_node, end_node)
        self.assertEqual(result, expected_path)

    def test_bfs_same_start_and_end(self):
        graph = load_graph_from_csv('BFS_DFS.csv')
        start_node = '1'
        end_node = '1'
        expected_path = ['1']
        result = breadth_first_search(graph, start_node, end_node)
        self.assertEqual(result, expected_path)

    def test_bfs_invalid_start_node(self):
        graph = load_graph_from_csv('BFS_DFS.csv')
        start_node = '300' #Node DNE
        end_node = '4'
        result = breadth_first_search(graph, start_node, end_node)
        self.assertIsNone(result)


# =============================================================================
# TestDFS
# Jacob Yealy
#
# Description:
# This class contains unit tests for the DFS algorithm.
# This test class checks for paths that exist, the same start and
# end nodes, and invalid start nodes.
# Each test case uses the information found in the local 'BFS_DFS.csv' file.
# =============================================================================
class TestDFS(unittest.TestCase):

    def test_dfs_path_exists(self):
        graph = load_graph_from_csv('BFS_DFS.csv')
        start_node = '124'
        end_node = '56'
        expected_path = ['124', '88', '38', '97', '10', '56']
        result = depth_first_search(graph, start_node, end_node)
        self.assertEqual(result, expected_path)

    def test_dfs_same_start_and_end(self):
        graph = load_graph_from_csv('BFS_DFS.csv')
        start_node = '1'
        end_node = '1'
        expected_path = ['1']
        result = depth_first_search(graph, start_node, end_node)
        self.assertEqual(result, expected_path)

    def test_dfs_invalid_start_node(self):
        graph = load_graph_from_csv('BFS_DFS.csv')
        start_node = '300'  # Node that does not exist
        end_node = '4'
        result = depth_first_search(graph, start_node, end_node)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()