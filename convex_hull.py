"""
* Convex Hull *
Method : Andrew's monotone chain convex hull algorithm
"""

import matplotlib.pyplot as plt
import networkx as nx
from random import randint


# Code from https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain#Python
def convex_hull(points):
    points = sorted(set(points))

    if len(points) <= 1:
        return points

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


NUMBER_VERTICES = 50
WIDTH = HEIGHT = 100  # dimension of the canvas
VERTEX_SIZE = 150

vertices = []
G = nx.Graph()

print("* Convex Hull *")
print("Number of vertices :", NUMBER_VERTICES,
      "| Dimensions of the canvas : (" + str(WIDTH), ";", str(HEIGHT) + ")\n")

# creation of the vertices
for i in range(NUMBER_VERTICES):
    new_vertex = (randint(0, WIDTH), randint(0, HEIGHT))
    vertices.append(new_vertex)
    G.add_node(i, pos=(new_vertex[0], new_vertex[1]))

hull = [vertices.index(vertex) for vertex in convex_hull(vertices)]
for i in range(len(hull) - 1):
    G.add_edge(hull[i], hull[i + 1])
G.add_edge(hull[0], hull[-1])

pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, node_size=VERTEX_SIZE, node_color='blue', width=2)
plt.show()
