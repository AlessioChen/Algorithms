from Node import Node
import sys


# classe che implementa l'albero Rosso Nero
class ARN:

    def __init__(self):
        self.TNULL = Node(-1)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def find(self, key):
        return self.find_node(self.root, key)

    def find_node(self, node, key):
        if node == self.TNULL or key == node.data:
            return node

        if key < node.data:
            return self.find_node(node.left, key)
        return self.find_node(node.right, key)

    # ruota a sinistra rispetto al nodo x
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # ruota a destra rispetto al nodo y
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):  # scorre l'albero fino alla radice e inserisce il nodo

        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = "Red"  # new node must be red

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        # if new node is a root node, simply return
        if node.parent is None:
            node.color = "Black"
            return

        # if the grandparent is None, simply return
        if node.parent.parent is None:
            return

        # Fix the tree
        self.RB_insert_fix_up(node)

    def RB_insert_fix_up(self, z):  # metodo che ci permette di bilanciare l'albero
        while z.parent.color == "Red":
            if z.parent == z.parent.parent.right:
                y = z.parent.parent.left  # uncle
                if y.color == "Red":
                    # case 3.1
                    y.color = "Black"
                    z.parent.color = "Black"
                    z.parent.parent.color = "Red"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        # case 3.2.2
                        z = z.parent
                        self.right_rotate(z)
                    # case 3.2.1
                    z.parent.color = "Black"
                    z.parent.parent.color = "Red"
                    self.left_rotate(z.parent.parent)
            else:
                y = z.parent.parent.right  # uncle

                if y.color == "Red":
                    # mirror case 3.1
                    y.color = "Black"
                    z.parent.color = "Black"
                    z.parent.parent.color = "Red"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        # mirror case 3.2.2
                        z = z.parent
                        self.left_rotate(z)
                    # mirror case 3.2.1
                    z.parent.color = "Black"
                    z.parent.parent.color = "Red"
                    self.right_rotate(z.parent.parent)
            if z == self.root:
                break
        self.root.color = "Black"

    def RB_print(self, node, indent, last):

        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "   "
            else:
                sys.stdout.write("L----")
                indent += "|   "

            s_color = "RED" if node.color == "Red" else "BLACK"
            print(str(node.key) + "(" + s_color + ")")
            self.RB_print(node.left, indent, False)
            self.RB_print(node.right, indent, True)

    def print(self):
        self.RB_print(self.root, "", True)

    def get_lenght(self):
        def _get_lenght(v):
            if v == self.TNULL: return 0
            length_sx = _get_lenght(v.left)
            lenght_dx = _get_lenght(v.right)
            return 1 + max(length_sx, lenght_dx)

        return _get_lenght(self.root)



tree = ARN()
tree.insert(20)
tree.insert(5)
tree.insert(2)
tree.insert(1)
tree.insert(34)
tree.insert(23)
tree.insert(9)
tree.insert(10)
tree.insert(4)
tree.insert(3)
tree.print()

print(tree.find(25).key)


