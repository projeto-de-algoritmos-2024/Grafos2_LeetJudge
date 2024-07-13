from questao1584 import Solution
import unittest

class TestMinCostConnectPoints(unittest.TestCase):
    def test_exemple_1(self):
        s = Solution()
        saida = s.minCostConnectPoints([[3,12],[-2,5],[-4,1]])
        esperado = 18
        self.assertEqual(saida, esperado)
    
    def test_exemple_2(self):
        s = Solution()
        saida = s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])
        esperado = 20
        self.assertEqual(saida, esperado)


if __name__ == '__main__':
    unittest.main()
