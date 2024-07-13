import heapq
import sys
import ast

class Solution(object):
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # direita, esquerda, baixo, cima
        dist = [[sys.maxsize] * n for _ in range(m)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # (cost, x, y)
        
        while heap:
            cost, x, y = heapq.heappop(heap)
            if x == m - 1 and y == n - 1:
                return cost
            
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost + (1 if grid[x][y] != i + 1 else 0)
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(heap, (new_cost, nx, ny))
        
        return -1  
