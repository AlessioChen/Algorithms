# classe che rappresenta un nodo
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = "Red"
        self.root = None

    def get(self):
        return self.key

    def set(self, key):
        self.key = key

    def getChildren(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children
