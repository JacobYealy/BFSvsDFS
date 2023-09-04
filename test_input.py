import unittest
from unittest.mock import patch, mock_open

from main import load_graph_from_csv

# =============================================================================
# Input Validation Tests
# Jacob Yealy
#
# Description:
# This class checks for cases of valid or invalid files.
# Since BFS_DFS.csv is already included locally, it is used to test functionality.
# The invalid file tests ensure that if a false file is submitted, it throws
# a FileNotFound error.
# =============================================================================
class TestInputValidation(unittest.TestCase):

    def test_valid_file(self):
        self.assertTrue(load_graph_from_csv("BFS_DFS.csv"))

    @patch('builtins.print')
    def test_invalid_file(self, mock_print):
        with self.assertRaises(SystemExit):
            load_graph_from_csv("BFS_DFS.txt")
        mock_print.assert_called_with("File not found.")

    @patch('builtins.print')
    def test_random_file(self, mock_print):
        with self.assertRaises(SystemExit):
            load_graph_from_csv("false.csv")
        mock_print.assert_called_with("File not found.")



if __name__ == '__main__':
    unittest.main()
