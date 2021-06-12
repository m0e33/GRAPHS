from snap.snap import LoadEdgeList, TNGraph, gvlDot


def intro():

    # save and load from a text file
    email_graph = LoadEdgeList(TNGraph, "email-EU-core.txt", 0, 1)
    print("email_graph: Nodes %d, Edges %d" % (email_graph.GetNodes(), email_graph.GetEdges()))

    email_graph.DrawGViz(gvlDot, "grid5x3.png", "Grid 5x3")


if __name__ == '__main__':
    intro()