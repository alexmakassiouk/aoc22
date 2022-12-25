from math import inf


class Node:
    def __init__(self, x, y, elevation) -> None:
        self.key = None
        self.parent = None
        self.adj = []
        self.x = x
        self.y = y
        self.elevation = elevation
        self.name = str(y) + " " + str(x)
    def add_adj(self, n):
        self.adj.append(n)
        #n.adj.append(self)

class Graph:
    def __init__(self) -> None:
        self.nodes = []
        self.adj = {}
    def add_node(self, n: Node):
        self.nodes.append(n)
        self.adj[n] = n.adj
