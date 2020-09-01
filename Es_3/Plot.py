import matplotlib.pyplot as plt
import numpy as np


def plot(x, y, n):
    plt.title('SCC di {} nodi'.format(n))
    plt.xlabel("Probabilità")
    plt.ylabel("Numero di SCC")
    plt.plot(x, y)
    plt.savefig('SCC_{}Nodes.png'.format(n))
    plt.clf()

