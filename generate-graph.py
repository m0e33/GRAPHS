from snap.snap import LoadEdgeList, TUNGraph, SaveEdgeList
import math

def intro():

    dblp_graph = LoadEdgeList(TUNGraph, "com-dblp.ungraph.txt", 0, 1)
    print("dblp-graph: Nodes %d, Edges %d" % (dblp_graph.GetNodes(), dblp_graph.GetEdges()))

    dblp_nodes = [node.GetId() for node in dblp_graph.Nodes()]

    print(dblp_graph.GetModularity(dblp_nodes))

    sub_dblp_graph = dblp_graph.GetRndSubGraph(math.ceil(dblp_graph.GetNodes() * 0.05))
    sub_dblp_nodes = [node.GetId() for node in sub_dblp_graph.Nodes()]

    SaveEdgeList(sub_dblp_graph, "0.05-com-dblp.ungraph.txt")
    print(sub_dblp_graph.GetModularity(sub_dblp_nodes))


if __name__ == '__main__':
    intro()