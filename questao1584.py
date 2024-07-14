import heapq

class Solution(object):
    def minCostConnectPoints(self, points):
        # Cria grafo
        k = len(points)
        g = Grafo(k)
        
        # Adiciona arestas entre todos os pares de pontos
        for i in range(k):
            for j in range(i + 1, k):
                custo = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                g.adicionaAresta(i, j, custo)
        
        # Encontra o custo mínimo usando o algoritmo de Prim
        custoMinimo = g.prim()
        
        return custoMinimo
    
class Grafo:
    def __init__(self, k):
        self.k = k
        self.grafo = [[] for _ in range(self.k)]

    def adicionaAresta(self, u, v, custo):
        self.grafo[u].append((v, custo))
        self.grafo[v].append((u, custo)) 

    def prim(self):
        # Inicializa o heap e os conjuntos de nós visitados e não visitados
        heap = [(0, 0)]  # (custo, nó)
        visitados = set()
        custoTotal = 0
        
        while heap and len(visitados) < self.k:
            custo, u = heapq.heappop(heap) # Pega o custo e nó de maior prioridade
            if u in visitados:
                continue
            visitados.add(u)
            custoTotal += custo
            
            for v, custo in self.grafo[u]:
                if v not in visitados:
                    heapq.heappush(heap, (custo, v))

        return custoTotal
