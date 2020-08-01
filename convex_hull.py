"""
* Convex Hull *
"""

import matplotlib.pyplot as plt
import networkx as nx
from random import randint


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def cross_product(o, a, b):
    area = (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)
    if area < 0:
        return -1
    if area > 0:
        return 1
    return 0


def lowest_vertex_of(lst):
    a = [v.y for v in lst]
    return lst[a.index(min(a))]


NUMBER_VERTICES = 10
WIDTH = HEIGHT = 100  # dimension of the canvas
VERTEX_SIZE = 150

vertices = []
unvisited_vertices = []
hull = []
G = nx.Graph()

print("* Convex Hull *")
print("Number of vertices :", NUMBER_VERTICES,
      "| Dimensions of the canvas : (" + str(WIDTH), ";", str(HEIGHT) + ")\n")

# creation of the vertices
for i in range(NUMBER_VERTICES):
    new_vertex = Vertex(randint(0, WIDTH), randint(0, HEIGHT))
    vertices.append(new_vertex)
    G.add_node(i, pos=(new_vertex.x, new_vertex.y))

anchor = lowest_vertex_of(vertices)
print(anchor)

pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, node_size=VERTEX_SIZE, node_color='orange', with_labels=True)
plt.show()
