from collections import defaultdict
import heapq

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        # Cria grafo
        g = Grafo(n)

        # Adiciona arestas ao grafo já subdividindo
        for u, v, cnt in edges:
            g.adicionaAresta(u, v, cnt)

        return g.dijkstraAdaptado(0, maxMoves)


class Grafo:
    def __init__(self, k):
        self.k = k
        self.grafo = defaultdict(list)
        self.totalNos = k

    def adicionaAresta(self, u, v, cnt):
        noAtual = u
        for _ in range(cnt):
            self.grafo[noAtual].append((self.totalNos, 1))
            self.grafo[self.totalNos].append((noAtual, 1))
            noAtual = self.totalNos
            self.totalNos += 1
        self.grafo[noAtual].append((v, 1))
        self.grafo[v].append((noAtual, 1))

    def dijkstraAdaptado(self, origem, maxMoves):
        dist = {i: float('inf') for i in range(self.totalNos)} # Armazena as menores distancias conhecidas
        dist[origem] = 0
        minHeap = [(0, origem)]  # (distância, nó)
        alcance = defaultdict(int)

        while minHeap:
            d, u = heapq.heappop(minHeap)
            if d > dist[u]:
                continue
            for v, w in self.grafo[u]:
                newDist = d + w
                if newDist <= maxMoves: 
                    alcance[v] = min(maxMoves - dist[u], w)
                    if newDist < dist[v]:
                        dist[v] = newDist
                        heapq.heappush(minHeap, (newDist, v))

        # Conta o número de nós acessíveis dentro de maxMoves
        numNosAlcancaveis = sum(d <= maxMoves for d in dist.values())
        return numNosAlcancaveis


# # Teste
# sol = Solution()
# numNosAlcancaveis = sol.reachableNodes([[0, 1, 10], [0, 2, 1], [1, 2, 2]], 6, 3)

# print(f"\nO número de nós alcançáveis é: {numNosAlcancaveis}\n")
