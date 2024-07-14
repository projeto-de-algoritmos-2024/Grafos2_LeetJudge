import heapq
from collections import defaultdict

class Dijkstra:
    def __init__(self, graph, n):
        self.graph = graph
        self.n = n
    
    def caminhoMaisBarato(self, k):
        distances = {node: float('inf') for node in range(1, self.n + 1)}
        distances[k] = 0
        min_heap = [(0, k)]  # (distância até o nó, nó)
        
        while min_heap:
            dist_atual, no_atual = heapq.heappop(min_heap)
            
            if dist_atual > distances[no_atual]:
                continue
            
            for vizinho , weight in self.graph[no_atual]:
                distance = dist_atual + weight
                if distance < distances[vizinho]:
                    distances[vizinho] = distance
                    heapq.heappush(min_heap, (distance, vizinho))
        
        max_distance = max(distances.values())
        if max_distance == float('inf'):
            return -1
        else:
            return max_distance

class Solution(object):
    def networkDelayTime(self, times, n, k):

        # Passo 1: Construir o grafo usando um defaultdict de listas
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Passo 2: Usar a classe Dijkstra para calcular o tempo mínimo de propagação do sinal
        dijkstra = Dijkstra(graph, n)
        return dijkstra.caminhoMaisBarato(k)

