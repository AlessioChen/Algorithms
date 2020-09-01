import time as timer
import numpy as np
from Graph import Graph
import Plot


def SCCCounter(prob_inc, nodes):
    x = np.arange(0, 101, prob_inc)

    sccCounter = []
    for p in range(0, 101, prob_inc):
        sccCount = 0
        for m in range(0, 10):
            g = Graph(nodes)
            g.random_init(p)
            g.SCC()
            sccCount += g.print_scc_solution()
            print(len(g.rootSCC))
        sccCounter.append(sccCount / 10)
    return x, sccCounter
