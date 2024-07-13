import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        distances = {node: float('inf') for node in range(1, n + 1)}
        distances[k] = 0
        min_heap = [(0, k)]  # (distância até o nó, nó)
        
        while min_heap:
            current_dist, current_node = heapq.heappop(min_heap)
            
            if current_dist > distances[current_node]:
                continue
            
            for neighbor, weight in graph[current_node]:
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))
        
        max_distance = max(distances.values())
        if max_distance == float('inf'):
            return -1
        else:
            return max_distance


