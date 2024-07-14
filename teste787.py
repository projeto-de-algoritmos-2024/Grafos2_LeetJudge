import unittest
from questao787 import Solution 

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        times = [[2,1,1],[2,3,1],[3,4,1]]
        n = 4
        k = 2
        self.assertEqual(self.sol.networkDelayTime(times, n, k), 2)

    def test_case2(self):
        times = [[1,2,1],[1,3,2],[2,4,1],[3,4,1]]
        n = 4
        k = 1
        self.assertEqual(self.sol.networkDelayTime(times, n, k), 2)

if __name__ == '__main__':
    unittest.main()
