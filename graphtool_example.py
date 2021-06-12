from graph_tool.all import *
import random

def intro():
    g = Graph()
    vertexes = [g.add_vertex() for _ in range(200)]

    for vertex in vertexes:
        g.add_edge(vertex, random.choice(vertexes))

    graph_draw(g, vertex_text=g.vertex_index, output="two-nodes.pdf")

if __name__ == '__main__':
    intro()