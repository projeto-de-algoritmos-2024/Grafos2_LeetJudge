from collections import defaultdict
import heapq


class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        g = Grafo(n)  # Inicializa um objeto Grafo com n nós

        # Adiciona as arestas ao grafo
        for u, v, custo in edges:
            g.adicionaAresta(u, v, custo)

        return g.dijkstraAdaptado(edges, maxMoves,n)
            

class Grafo:
    def __init__(self, k):
        self.k = k
        self.grafo = defaultdict(list)

    def adicionaAresta(self, u, v, custo):
        self.grafo[u].append((v, custo))
        self.grafo[v].append((u, custo))

    def dijkstraAdaptado(self, edges, maxMoves, n):
        dis = [float('inf')]*n
        dis[0] = 0
        heap = [(0,0)]
        visitados = [False]*n

        movimentos = defaultdict(lambda:0)

        result = 0
        while heap:
            distancia, no = heapq.heappop(heap)

            # Pula o no se ele já foi visitado ou a distancia é maior que o maximo de movimentos
            if visitados[no] or distancia > maxMoves: 
                continue

            result += 1
            visitados[no] = True
            movimentosRestantes = maxMoves - distancia

            for noVizinho, distanciaVizinho in self.grafo[no]:

                movimentos[(no, noVizinho)] = min(distanciaVizinho, movimentosRestantes)

                novaDistancia = distancia + distanciaVizinho + 1

                if novaDistancia < dis[noVizinho]:
                    dis[noVizinho] = novaDistancia
                    heapq.heappush(heap,(novaDistancia, noVizinho))

        for i, j, distancia in edges:
            total = movimentos[(i,j)] + movimentos[(j,i)]
            if total > distancia: 
                total = distancia
            result += total

        return result
