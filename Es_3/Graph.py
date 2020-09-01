from Node import Node
import numpy as np
import random


class Graph:
    def __init__(self, nodes_number):
        self.n = nodes_number
        self.time = 0
        self.nodes = []  # vettore dei nodi
        self.ad = np.zeros((self.n, self.n))  # matrice di adiacenza
        self.adt = np.zeros((self.n, self.n))  # matrice trasposta
        self.path = []  # contiene la soluzione del SCC
        self.rootSCC = []

        for i in range(0, self.n):
            self.nodes.append(Node())
            self.nodes[i].name = chr(ord("A") + i)

    def random_init(self, probability):
        for i in range(0, len(self.ad)):
            for j in range(0, len(self.ad)):
                r = random.randint(0, 100)
                if r <= probability and probability >= 0:
                    self.ad[i][j] = 1

        for i in range(0, len(self.ad)):
            self.ad[i][i] = 0

    def DFS(self):
        for i in range(0, len(self.nodes)):
            self.nodes[i].color = "White"
            self.nodes[i].z = -1
        self.time = 0
        for i in range(0, len(self.nodes)):
            if self.nodes[i].color == "White":
                self.DFS_visit(i, self.ad)

    def DFS_visit(self, node_index, matrix):
        self.nodes[node_index].color = "Gray"
        if self.nodes[node_index].d == 0:
            self.time += 1
            self.nodes[node_index].d = self.time

        for j in range(0, len(self.nodes)):
            if matrix[node_index, j] == 1 and self.nodes[j].color == "White":
                self.nodes[j].z = node_index
                self.DFS_visit(j, matrix)

        self.nodes[node_index].color = "Black"
        if self.nodes[node_index].f == 0:
            self.time += 1
            self.nodes[node_index].f = self.time
            if self.nodes[node_index].visited:
                self.path.insert(0, node_index)

    def DFS_trasposte(self):
        v = []
        for i in range(0, len(self.nodes)):
            max = -1
            for j in range(0, len(self.nodes)):
                if not self.nodes[j].visited:
                    if max == -1 or self.nodes[j].f > max:
                        max = self.nodes[j].f
                        max_index = j
            self.nodes[max_index].visited = True
            v.append(max_index)

        for i in range(0, len(self.nodes)):
            self.nodes[i].color = "White"
            self.nodes[i].d = 0
            self.nodes[i].f = 0
            self.nodes[i].z = -1
            self.time = 0

        for i in range(0, len(self.nodes)):
            a = v[i]
            if self.nodes[a].color == "White":
                self.DFS_visit(a, self.adt)
                self.rootSCC.append('SCC')

    def SCC(self):
        self.DFS()
        # self.print_graph(self.nodes)
        self.adt = np.transpose(self.ad)
        self.DFS_trasposte()

    def print_graph(self, nodes):
        for i in range(0, len(self.nodes)):
            print(self.nodes[i].name + " " + str(self.nodes[i].d) + " " + str(self.nodes[i].f))

    def print_scc_solution(self):
        count = 1
        print("--SCC COMPONENTS--")
        print("SCC N." + str(count))
        print(self.nodes[self.path[0]].name)
        for j in range(1, len(self.path)):
            prec = self.nodes[self.path[j - 1]]
            app = self.nodes[self.path[j]]
            if prec.d < app.d:
                print(app.name)
            else:
                count += 1
                print("SCC N." + str(count))
                print(app.name)
        return count
