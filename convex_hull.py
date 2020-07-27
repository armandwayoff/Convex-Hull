"""
* Convex Hull *
"""

import matplotlib.pyplot as plt
import networkx as nx
from random import randint
from math import atan


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def angle(v1, v2, v3):
    if v1.x == v2.x or v2.x == v3.x:
        return 90
    else:
        m1 = (v1.y - v2.y) / (v1.x - v2.x)
        m2 = (v2.y - v3.y) / (v2.x - v3.x)
        return atan(abs((m1 - m2) / (1 + m1 * m2)))

NUMBER_VERTICES = 10
NUMBER_CLUSTERS = 4
WIDTH = HEIGHT = 100  # dimension of the canvas
VERTEX_SIZE = 150

vertices = []
hull = []
G = nx.Graph()

print("* Convex Hull *")
print("Number of vertices :", NUMBER_VERTICES,
      "| Number of clusters :", NUMBER_CLUSTERS,
      "| Dimensions of the canvas : (" + str(WIDTH), ";", str(HEIGHT) + ")\n")

# creation of the vertices
for i in range(NUMBER_VERTICES):
    new_vertex = Vertex(randint(0, WIDTH), randint(0, HEIGHT))
    vertices.append(new_vertex)
    G.add_node(i, pos=(new_vertex.x, new_vertex.y))

abscissas = [v.x for v in vertices]
current_vertex = vertices[abscissas.index(min(abscissas))]
start = current_vertex
hull.append(current_vertex)
print(abscissas.index(min(abscissas)))

# initialisation
horizontal = Vertex(current_vertex.x + 10, current_vertex.y)
max_angle = 0
global next_vertex
for vertex in vertices:
    if vertex not in hull and angle(horizontal, current_vertex, vertex) > max_angle:
        max_angle = angle(horizontal, current_vertex, vertex)
        next_vertex = vertex
hull.append(next_vertex)
G.add_edge(vertices.index(current_vertex), vertices.index(next_vertex))
current_vertex = next_vertex

pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, node_size=VERTEX_SIZE, node_color='orange', with_labels=True)
plt.show()
