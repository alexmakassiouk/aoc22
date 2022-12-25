from queue import Queue
from graph import Graph, Node
from math import inf

def bfs(G: Graph, s: Node):
    for u in G.nodes:
        if u != s:
            u.color = "WHITE"
            u.key = inf
    s.color = "GRAY"
    s.key = 0
    Q = Queue(1000)
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in u.adj:
            if v.color == "WHITE":
                v.color = "GRAY"
                v.key=u.key+1
                v.parent = u
                Q.put(v)
        u.color = "BLACK"

def print_path(G: Graph, s: Node, v: Node):
    if v==s:
        print(s.name)
    elif v.parent == None:
        print("No path exists")
    else:
        print_path(G,s,v.parent)
        print(v.name)


def main():
    n1 = Node("n1")
    n2 = Node("n2")
    n3 = Node("n3")
    n4 = Node("n4")
    n5 = Node("n5")
    n6 = Node("n6")

    n1.add_adj(n2)
    n1.add_adj(n3)
    n4.add_adj(n2)
    n4.add_adj(n3)
    n2.add_adj(n5)
    n5.add_adj(n6)

    g = Graph()
    g.add_node(n1)
    g.add_node(n2)
    g.add_node(n3)
    g.add_node(n4)
    g.add_node(n5)
    g.add_node(n6)

    bfs(g,n1)
    print("Success")
    print_path(g,n1,n6)
