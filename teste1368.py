import unittest
from Q1368 import Solution 

class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_minCost(self):
        grid = [[1, 1, 1],[1, 1, 1],[1, 1, 1]]
        expected_cost = 2 
        self.assertEqual(self.solution.minCost(grid), expected_cost)

    def test_minCost(self):
        grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
        expected_cost = 3  
        self.assertEqual(self.solution.minCost(grid), expected_cost)



if __name__ == "__main__":
    unittest.main()
