from questao882 import Solution
import unittest

class TestReachableNodes(unittest.TestCase):
    def test_exemple_1(self):
        s = Solution()
        saida = s.reachableNodes([[0,1,10],[0,2,1],[1,2,2]],6,3)
        esperado = 13
        self.assertEqual(saida, esperado)

    def test_exemple_2(self):
        s = Solution()
        saida = s.reachableNodes([[0,1,4],[1,2,6],[0,2,8],[1,3,1]],10,4)
        esperado = 23
        self.assertEqual(saida, esperado)

    def test_exemple_3(self):
        s = Solution()
        saida = s.reachableNodes([[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]],17,5)
        esperado = 1
        self.assertEqual(saida, esperado)


if __name__ == '__main__':
    unittest.main()
