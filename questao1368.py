import heapq
import sys

class Dijkstra:
    def __init__(self, grid):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # direita, esquerda, baixo, cima
    
    def minDist(self):
        dist = [[sys.maxsize] * self.n for _ in range(self.m)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # (cost, x, y)
        
        while heap:
            cost, x, y = heapq.heappop(heap)
            if x == self.m - 1 and y == self.n - 1:
                return cost
            
            for i, (dx, dy) in enumerate(self.directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.m and 0 <= ny < self.n:
                    new_cost = cost + (1 if self.grid[x][y] != i + 1 else 0)
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(heap, (new_cost, nx, ny))
        
        return -1

class Solution(object):
    def minCost(self, grid):
        dijkstra = Dijkstra(grid)
        return dijkstra.minDist()

