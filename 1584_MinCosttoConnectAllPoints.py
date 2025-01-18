from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def c_distancia(ponto1, ponto2):
            return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])

        qtdpts = len(points)
        arestas = []

        for i in range(qtdpts):
            for j in range(i + 1, qtdpts):
                distancia = c_distancia(points[i], points[j])
                arestas.append((distancia, i, j))

        #Ordenar arestas por peso ASC
        arestas.sort()

        #UF
        nome_arvore = list(range(qtdpts))
        rank = [0] * qtdpts

        def find(x):
            if nome_arvore[x] != x:
                nome_arvore[x] = find(nome_arvore[x])
            return nome_arvore[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    nome_arvore[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    nome_arvore[rootX] = rootY
                else:
                    nome_arvore[rootY] = rootX
                    rank[rootX] += 1

        #Construir a Árvore Geradora Mínima (MST)
        custo_total = 0
        usadas = 0 #Num de arestas não descartadas

        for custo, u, v in arestas:
            if find(u) != find(v):
                union(u, v)
                custo_total += custo
                usadas += 1
                if usadas == qtdpts - 1:  #Todos os pontos conectados sem ciclos
                    break

        return custo_total