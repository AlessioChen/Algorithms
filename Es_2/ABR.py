from Node import Node


class ABR:

    def __init__(self):
        self.root = None

    def setRoot(self, key):  # crea un nodo padre
        self.root = Node(key)

    def insert(self, key):  # inserimento di un nuovo nodo
        # if self.find(key):
        #     return
        if self.root is None:  # albero vuoto
            self.setRoot(key)
        else:
            self.insert_node(self.root, key)  # albero non vuoto

    def insert_node(self, current_node, key):  # navigo l'albero per trovare la pos in maniera ricorsiva
        if key <= current_node.key:  # se la chiave è minore
            if current_node.left is not None:
                self.insert_node(current_node.left, key)
            else:
                current_node.left = Node(key)
        else:
            if current_node.right:
                self.insert_node(current_node.right, key)
            else:
                current_node.right = Node(key)

    def find(self, key):
        return self.find_node(self.root, key)

    def find_node(self, current_node, key):  # trova la presenza di una chiave nell'albero
        if current_node is None:
            return False
        elif key == current_node.key:
            return True
        elif key < current_node.key:
            return self.find_node(current_node.left, key)
        else:
            return self.find_node(current_node.right, key)

    def inorder(self):  # attraversamento in order dell'albero
        def _inorder(v):
            if v is None:
                return
            if v.left is not None:
                _inorder(v.left)
            print(v.key)
            if v.right is not None:
                _inorder(v.right)

        _inorder(self.root)

    def get_lenght(self):
        def _get_lenght(v):
            if v is None: return 0
            length_sx = _get_lenght(v.left)
            lenght_dx = _get_lenght(v.right)
            return 1 + max(length_sx, lenght_dx)

        return _get_lenght(self.root)


tree = ABR()
tree.insert(7)
tree.insert(2)
tree.insert(3)
tree.insert(3)

tree.insert(5)
tree.insert(7)
tree.insert(8)
tree.inorder()



