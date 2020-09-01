# classe che rappresenta il nodo
class Node:

    def __init__(self):
        self.d = 0  # tempo di scoperta
        self.f = 0  # tempo di fine
        self.color = None
        self.z = -1
        self.visited = False
        self.name = None